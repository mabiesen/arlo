import { useEffect, useCallback, useState } from 'react'
import { api } from '../utilities'

export interface IAuditSettings {
  state: string | null
  electionName: string | null
  online: boolean | null
  randomSeed: string | null
  riskLimit: number | null
  auditType: 'BALLOT_POLLING' | 'BATCH_COMPARISON' | 'BALLOT_COMPARISON'
  auditMathType: 'BRAVO' | 'MINERVA' | 'SUPERSIMPLE' | 'MACRO'
  auditName: string
}

interface INewSettings {
  state: IAuditSettings['state']
  electionName: IAuditSettings['electionName']
  online: IAuditSettings['online']
  randomSeed: IAuditSettings['randomSeed']
  riskLimit: IAuditSettings['riskLimit']
}

const useAuditSettings = (
  electionId: string,
  refreshId?: string
): [IAuditSettings | null, (arg0: INewSettings) => Promise<boolean>] => {
  const [settings, setSettings] = useState<IAuditSettings | null>(null)

  const getSettings = useCallback(async (): Promise<IAuditSettings | null> => {
    return api<IAuditSettings>(`/election/${electionId}/settings`)
  }, [electionId])

  const updateSettings = async (
    newSettings: INewSettings
  ): Promise<boolean> => {
    const oldSettings = await getSettings()
    const mergedSettings = {
      ...oldSettings,
      ...newSettings,
    }
    const response = await api(`/election/${electionId}/settings`, {
      method: 'PUT',
      body: JSON.stringify(mergedSettings),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    return !!response
  }

  useEffect(() => {
    ;(async () => {
      const newSettings = await getSettings()
      setSettings(newSettings)
    })()
  }, [getSettings, refreshId])
  return [settings, updateSettings]
}

export default useAuditSettings
