import { useState, useEffect } from 'react'
import { toast } from 'react-toastify'
import { api } from '../utilities'

export enum FileProcessingStatus {
  READY_TO_PROCESS = 'READY_TO_PROCESS',
  PROCESSING = 'PROCESSING',
  PROCESSED = 'PROCESSED',
  ERRORED = 'ERRORED',
}

export interface IFileInfo {
  file: {
    name: string
    uploadedAt: string
  } | null
  processing: {
    status: FileProcessingStatus
    startedAt: string | null
    completedAt: string | null
    error: string | null
  } | null
}

export interface IBallotManifestInfo extends IFileInfo {
  numBallots: number | null
  numBatches: number | null
}

export enum JurisdictionRoundStatus {
  NOT_STARTED = 'NOT_STARTED',
  IN_PROGRESS = 'IN_PROGRESS',
  COMPLETE = 'COMPLETE',
}

export interface IJurisdiction {
  id: string
  name: string
  ballotManifest: IBallotManifestInfo
  currentRoundStatus: {
    status: JurisdictionRoundStatus
    numSamples: number
    numSamplesAudited: number
    numBallots: number
    numBallotsAudited: number
  } | null
}

export const prettifyStatus = (processing: IFileInfo['processing']): string => {
  if (!processing) return 'No manifest uploaded'
  switch (processing.status) {
    case FileProcessingStatus.ERRORED:
      return `Manifest upload failed: ${processing.error}`
    case FileProcessingStatus.PROCESSED:
      return 'Manifest received'
    default:
      return 'No manifest uploaded'
  }
}

const useJurisdictions = (electionId: string, refreshId?: string) => {
  const [jurisdictions, setJurisdictions] = useState<IJurisdiction[]>([])
  useEffect(() => {
    ;(async () => {
      try {
        const response: { jurisdictions: IJurisdiction[] } = await api(
          `/election/${electionId}/jurisdiction`
        )
        setJurisdictions(response.jurisdictions)
      } catch (err) {
        toast.error(err.message)
      }
    })()
  }, [electionId, refreshId])
  return jurisdictions
}

export default useJurisdictions