# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots[
    "test_ballot_comparison_container_manifest 1"
] = """Container,Tabulator,Batch Name,Ballot Number,Imprinted ID,Ticket Numbers,Already Audited,Audit Board
CONTAINER1,TABULATOR1,BATCH1,1,1-1-1,0.243550726331576894,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,5,1-1-5,0.327122451546285118,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,6,1-1-6,"0.091744824569257250,0.214593396079380408,0.471470931332575569,0.596999178541725020",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,7,1-1-7,0.497842509493126247,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,8,1-1-8,0.179880514969156451,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,9,1-1-9,"0.443721405572776973,0.531330159552583225",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,10,1-1-10,0.071833944794077772,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,11,1-1-11,0.398162355887676054,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,12,1-1-12,"0.182964652423852944,0.376609738540939151,0.536655036756398571",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,13,1-1-13,0.321180720503738896,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,14,1-1-14,0.161906334584190250,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,16,1-1-16,0.568342051457579515,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH1,19,1-1-19,0.025724786095896671,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,2,1-2-2,0.125871889047705889,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,3,1-2-3,"0.126622033568908859,0.570682515619614792",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,6,1-2-6,0.027302801514320711,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,7,1-2-7,0.581808979838659398,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,10,1-2-10,0.604837095286587721,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,11,1-2-11,0.032687309857572166,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,13,1-2-13,"0.129049852648786112,0.260448685596731168,0.477034033790054328",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,17,1-2-17,0.199373873544016677,N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,19,1-2-19,"0.318639014395146776,0.544524818824451799",N,Audit Board #1
CONTAINER1,TABULATOR1,BATCH2,20,1-2-20,"0.102145476881105551,0.476548471668041956",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,4,2-1-4,"0.148343827282863044,0.584898211099346783",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,5,2-1-5,0.248291164718415707,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,6,2-1-6,"0.387599967981498767,0.600402765819029283",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,7,2-1-7,"0.310900605635630249,0.460867359610658993",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,8,2-1-8,"0.317833202400291186,0.427093702949299834",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,9,2-1-9,"0.248927906005441061,0.514641964224033422",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,11,2-1-11,"0.177578804041449803,0.297545892806758777",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,12,2-1-12,"0.475070514662067897,0.554161269425017640,0.575285685981292025",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,13,2-1-13,0.312279893865807310,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,14,2-1-14,0.330144673213460464,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,15,2-1-15,0.006700879199748225,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,16,2-1-16,0.102205830606785931,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,17,2-1-17,"0.563937721070225377,0.589397030583691885",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,18,2-1-18,"0.105786652871978736,0.487569072091825961",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH1,19,2-1-19,0.514174044934793758,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,1,2-2-1,0.607927957276839128,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,2,2-2-2,"0.053992217600758631,0.528652598036440834",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,3,2-2-3,0.255119157791673311,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,4,2-2-4,"0.064984443990590400,0.069414660569975443",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,5,2-2-5,"0.442956417641278897,0.492638838970333256",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,6,2-2-6,"0.300053574780458718,0.539920212714138536",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,7,2-2-7,0.073079363492779630,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,8,2-2-8,"0.129163188267875849,0.368668769558186913",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,9,2-2-9,0.172020648710088147,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,12,2-2-12,0.389519543150236623,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,13,2-2-13,0.281713658987415416,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,14,2-2-14,0.159872307903683761,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,15,2-2-15,"0.017856797084428910,0.165441877715613399,0.420734545343474178",N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,17,2-2-17,0.581175142999588842,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,18,2-2-18,0.426702167475473151,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,19,2-2-19,0.104242501240585214,N,Audit Board #1
CONTAINER1,TABULATOR2,BATCH2,20,2-2-20,"0.049754289383712287,0.527386444549160771",N,Audit Board #1
CONTAINER2,TABULATOR1,BATCH3,1,1-3-1,"0.104960245880765828,0.105681911382037805,0.443226233256406766,0.598178776084261874",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,2,1-3-2,0.009464169703578658,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,6,1-3-6,0.220262468746465609,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,7,1-3-7,0.460890185876098427,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,8,1-3-8,"0.014246627323528638,0.057091554592472947",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,9,1-3-9,"0.207147400254629563,0.209934744187520019,0.497054846511573727",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,12,1-3-12,"0.295905762263528395,0.464555516330570517,0.585333009775445118",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,13,1-3-13,0.008481195646651660,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,14,1-3-14,0.255108015380531329,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,15,1-3-15,"0.139318472161278805,0.480284184853948623",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,18,1-3-18,0.407601027364173688,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH3,19,1-3-19,0.255050426391377387,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,1,1-4-1,"0.338739898622344504,0.566411714962113470",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,2,1-4-2,"0.072136306370783664,0.444302163376821793",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,3,1-4-3,0.018064599389368317,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,6,1-4-6,"0.024273506122438730,0.385565938928334329,0.401496395885341524",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,7,1-4-7,0.352766525233692388,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,10,1-4-10,0.433191424954367856,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,11,1-4-11,0.072933239735786720,N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,13,1-4-13,"0.291339346598810066,0.346455669759093066,0.594714063005615126",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,15,1-4-15,"0.092846186144181855,0.449914009935623240",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,16,1-4-16,"0.162094922726252772,0.573178043302147465",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,17,1-4-17,"0.078352552730653041,0.245203325403628507,0.295626562310946592,0.350352733366311893",N,Audit Board #2
CONTAINER2,TABULATOR1,BATCH4,20,1-4-20,0.408449640447320649,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,1,2-3-1,0.397115260083866994,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,2,2-3-2,"0.044752657465679659,0.381927727584107064",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,3,2-3-3,"0.364923944308970284,0.580401759702358539",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,4,2-3-4,"0.252681413137222291,0.354332805847331872",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,5,2-3-5,"0.139596473713290533,0.510584699386446222,0.523008509625454409",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,8,2-3-8,0.067414590610384464,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,9,2-3-9,0.447447897877003135,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,10,2-3-10,0.248516399499413387,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,11,2-3-11,0.300202788713518359,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,12,2-3-12,0.215260131236910684,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,13,2-3-13,"0.172602119697808574,0.371003707244644998",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,17,2-3-17,"0.231597160412902215,0.447420460341185811",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH3,18,2-3-18,0.592563483281696769,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,1,2-4-1,"0.430363272313598410,0.593871532788906682",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,3,2-4-3,"0.036001046192521398,0.385665346156177707",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,4,2-4-4,0.249393728544838676,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,5,2-4-5,0.446527530320687239,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,6,2-4-6,"0.035950930636736620,0.375422571804708154,0.460487981474601570",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,7,2-4-7,0.582912610252033630,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,9,2-4-9,0.304085581138115000,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,10,2-4-10,0.483439326984888295,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,11,2-4-11,0.410473817943784644,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,12,2-4-12,0.532899652596481404,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,13,2-4-13,"0.178879967748620034,0.428651608765827294,0.500322269272083047",N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,15,2-4-15,0.280383857151013100,N,Audit Board #2
CONTAINER2,TABULATOR2,BATCH4,19,2-4-19,0.061230760400140955,N,Audit Board #2
"""

snapshots[
    "test_ballot_comparison_container_manifest 2"
] = """######## ELECTION INFO ########\r
Election Name,State\r
Test Election,CA\r
\r
######## CONTESTS ########\r
Contest Name,Targeted?,Number of Winners,Votes Allowed,Total Ballots Cast,Tabulated Votes\r
Contest 1,Targeted,1,1,360,Choice 1-1: 160; Choice 1-2: 160\r
\r
######## AUDIT SETTINGS ########\r
Audit Name,Audit Type,Risk Limit,Random Seed,Online Data Entry?\r
Test Audit test_ballot_comparison_container_manifest,BALLOT_COMPARISON,10%,1234567890,Yes\r
\r
######## AUDIT BOARDS ########\r
Jurisdiction Name,Audit Board Name,Member 1 Name,Member 1 Affiliation,Member 2 Name,Member 2 Affiliation\r
J1,Audit Board #1,,,,\r
J1,Audit Board #2,,,,\r
J1,Audit Board #3,,,,\r
J2,Audit Board #1,,,,\r
J2,Audit Board #2,,,,\r
J2,Audit Board #3,,,,\r
\r
######## ROUNDS ########\r
Round Number,Contest Name,Targeted?,Sample Size,Risk Limit Met?,P-Value,Start Time,End Time,Audited Votes\r
1,Contest 1,Targeted,360,No,,DATETIME,,Choice 1-1: 0; Choice 1-2: 0\r
\r
######## SAMPLED BALLOTS ########\r
Jurisdiction Name,Container,Tabulator,Batch Name,Ballot Position,Imprinted ID,Ticket Numbers: Contest 1,Audited?,Audit Result: Contest 1,CVR Result: Contest 1,Discrepancy: Contest 1\r
J1,CONTAINER1,TABULATOR1,BATCH1,1,1-1-1,Round 1: 0.243550726331576894,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,5,1-1-5,Round 1: 0.327122451546285118,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,6,1-1-6,"Round 1: 0.091744824569257250, 0.214593396079380408, 0.471470931332575569, 0.596999178541725020",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,7,1-1-7,Round 1: 0.497842509493126247,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,8,1-1-8,Round 1: 0.179880514969156451,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,9,1-1-9,"Round 1: 0.443721405572776973, 0.531330159552583225",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,10,1-1-10,Round 1: 0.071833944794077772,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,11,1-1-11,Round 1: 0.398162355887676054,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,12,1-1-12,"Round 1: 0.182964652423852944, 0.376609738540939151, 0.536655036756398571",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,13,1-1-13,Round 1: 0.321180720503738896,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,14,1-1-14,Round 1: 0.161906334584190250,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,16,1-1-16,Round 1: 0.568342051457579515,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH1,19,1-1-19,Round 1: 0.025724786095896671,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,2,1-2-2,Round 1: 0.125871889047705889,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,3,1-2-3,"Round 1: 0.126622033568908859, 0.570682515619614792",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,6,1-2-6,Round 1: 0.027302801514320711,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,7,1-2-7,Round 1: 0.581808979838659398,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,10,1-2-10,Round 1: 0.604837095286587721,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,11,1-2-11,Round 1: 0.032687309857572166,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,13,1-2-13,"Round 1: 0.129049852648786112, 0.260448685596731168, 0.477034033790054328",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,17,1-2-17,Round 1: 0.199373873544016677,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,19,1-2-19,"Round 1: 0.318639014395146776, 0.544524818824451799",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR1,BATCH2,20,1-2-20,"Round 1: 0.102145476881105551, 0.476548471668041956",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,4,2-1-4,"Round 1: 0.148343827282863044, 0.584898211099346783",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,5,2-1-5,Round 1: 0.248291164718415707,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,6,2-1-6,"Round 1: 0.387599967981498767, 0.600402765819029283",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,7,2-1-7,"Round 1: 0.310900605635630249, 0.460867359610658993",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,8,2-1-8,"Round 1: 0.317833202400291186, 0.427093702949299834",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,9,2-1-9,"Round 1: 0.248927906005441061, 0.514641964224033422",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,11,2-1-11,"Round 1: 0.177578804041449803, 0.297545892806758777",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,12,2-1-12,"Round 1: 0.475070514662067897, 0.554161269425017640, 0.575285685981292025",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,13,2-1-13,Round 1: 0.312279893865807310,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,14,2-1-14,Round 1: 0.330144673213460464,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,15,2-1-15,Round 1: 0.006700879199748225,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,16,2-1-16,Round 1: 0.102205830606785931,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,17,2-1-17,"Round 1: 0.563937721070225377, 0.589397030583691885",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,18,2-1-18,"Round 1: 0.105786652871978736, 0.487569072091825961",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH1,19,2-1-19,Round 1: 0.514174044934793758,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,1,2-2-1,Round 1: 0.607927957276839128,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.053992217600758631, 0.528652598036440834",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,3,2-2-3,Round 1: 0.255119157791673311,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,4,2-2-4,"Round 1: 0.064984443990590400, 0.069414660569975443",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,5,2-2-5,"Round 1: 0.442956417641278897, 0.492638838970333256",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,6,2-2-6,"Round 1: 0.300053574780458718, 0.539920212714138536",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,7,2-2-7,Round 1: 0.073079363492779630,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,8,2-2-8,"Round 1: 0.129163188267875849, 0.368668769558186913",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,9,2-2-9,Round 1: 0.172020648710088147,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,12,2-2-12,Round 1: 0.389519543150236623,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,13,2-2-13,Round 1: 0.281713658987415416,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,14,2-2-14,Round 1: 0.159872307903683761,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,15,2-2-15,"Round 1: 0.017856797084428910, 0.165441877715613399, 0.420734545343474178",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,17,2-2-17,Round 1: 0.581175142999588842,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,18,2-2-18,Round 1: 0.426702167475473151,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,19,2-2-19,Round 1: 0.104242501240585214,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER1,TABULATOR2,BATCH2,20,2-2-20,"Round 1: 0.049754289383712287, 0.527386444549160771",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,1,1-3-1,"Round 1: 0.104960245880765828, 0.105681911382037805, 0.443226233256406766, 0.598178776084261874",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,2,1-3-2,Round 1: 0.009464169703578658,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,6,1-3-6,Round 1: 0.220262468746465609,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,7,1-3-7,Round 1: 0.460890185876098427,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,8,1-3-8,"Round 1: 0.014246627323528638, 0.057091554592472947",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,9,1-3-9,"Round 1: 0.207147400254629563, 0.209934744187520019, 0.497054846511573727",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,12,1-3-12,"Round 1: 0.295905762263528395, 0.464555516330570517, 0.585333009775445118",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,13,1-3-13,Round 1: 0.008481195646651660,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,14,1-3-14,Round 1: 0.255108015380531329,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,15,1-3-15,"Round 1: 0.139318472161278805, 0.480284184853948623",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,18,1-3-18,Round 1: 0.407601027364173688,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH3,19,1-3-19,Round 1: 0.255050426391377387,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,1,1-4-1,"Round 1: 0.338739898622344504, 0.566411714962113470",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,2,1-4-2,"Round 1: 0.072136306370783664, 0.444302163376821793",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,3,1-4-3,Round 1: 0.018064599389368317,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,6,1-4-6,"Round 1: 0.024273506122438730, 0.385565938928334329, 0.401496395885341524",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,7,1-4-7,Round 1: 0.352766525233692388,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,10,1-4-10,Round 1: 0.433191424954367856,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,11,1-4-11,Round 1: 0.072933239735786720,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,13,1-4-13,"Round 1: 0.291339346598810066, 0.346455669759093066, 0.594714063005615126",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,15,1-4-15,"Round 1: 0.092846186144181855, 0.449914009935623240",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,16,1-4-16,"Round 1: 0.162094922726252772, 0.573178043302147465",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,17,1-4-17,"Round 1: 0.078352552730653041, 0.245203325403628507, 0.295626562310946592, 0.350352733366311893",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR1,BATCH4,20,1-4-20,Round 1: 0.408449640447320649,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,1,2-3-1,Round 1: 0.397115260083866994,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,2,2-3-2,"Round 1: 0.044752657465679659, 0.381927727584107064",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,3,2-3-3,"Round 1: 0.364923944308970284, 0.580401759702358539",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,4,2-3-4,"Round 1: 0.252681413137222291, 0.354332805847331872",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,5,2-3-5,"Round 1: 0.139596473713290533, 0.510584699386446222, 0.523008509625454409",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,8,2-3-8,Round 1: 0.067414590610384464,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,9,2-3-9,Round 1: 0.447447897877003135,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,10,2-3-10,Round 1: 0.248516399499413387,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,11,2-3-11,Round 1: 0.300202788713518359,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,12,2-3-12,Round 1: 0.215260131236910684,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,13,2-3-13,"Round 1: 0.172602119697808574, 0.371003707244644998",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,17,2-3-17,"Round 1: 0.231597160412902215, 0.447420460341185811",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH3,18,2-3-18,Round 1: 0.592563483281696769,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,1,2-4-1,"Round 1: 0.430363272313598410, 0.593871532788906682",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,3,2-4-3,"Round 1: 0.036001046192521398, 0.385665346156177707",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,4,2-4-4,Round 1: 0.249393728544838676,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,5,2-4-5,Round 1: 0.446527530320687239,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,6,2-4-6,"Round 1: 0.035950930636736620, 0.375422571804708154, 0.460487981474601570",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,7,2-4-7,Round 1: 0.582912610252033630,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,9,2-4-9,Round 1: 0.304085581138115000,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,10,2-4-10,Round 1: 0.483439326984888295,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,11,2-4-11,Round 1: 0.410473817943784644,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,12,2-4-12,Round 1: 0.532899652596481404,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,13,2-4-13,"Round 1: 0.178879967748620034, 0.428651608765827294, 0.500322269272083047",NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,15,2-4-15,Round 1: 0.280383857151013100,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J1,CONTAINER2,TABULATOR2,BATCH4,19,2-4-19,Round 1: 0.061230760400140955,NOT_AUDITED,,"Choice 1-1, Choice 1-2",\r
J2,,TABULATOR1,BATCH1,1,1-1-1,Round 1: 0.476019554092109137,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,2,1-1-2,"Round 1: 0.511105635717372621, 0.583472201399663519",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,3,1-1-3,Round 1: 0.242392535590495322,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,4,1-1-4,Round 1: 0.510637350641069900,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,5,1-1-5,Round 1: 0.501493985166491093,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,8,1-1-8,"Round 1: 0.125187013140863705, 0.186081288325398929",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,9,1-1-9,"Round 1: 0.334207510511737572, 0.424319475812277273",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,10,1-1-10,"Round 1: 0.234849952195438448, 0.417970927720345384",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,11,1-1-11,"Round 1: 0.335064007888300888, 0.340996102462229247",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,14,1-1-14,"Round 1: 0.261821315820962886, 0.592956904743188068",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,17,1-1-17,"Round 1: 0.035284097923720086, 0.303323047074814525",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,18,1-1-18,"Round 1: 0.380219283788015669, 0.485648902369102608",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,19,1-1-19,Round 1: 0.175633907608523470,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,21,1-1-21,Round 1: 0.407935823531871324,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,22,1-1-22,"Round 1: 0.358956715816896365, 0.542088484964092704",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,24,1-1-24,Round 1: 0.167464754356813104,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,25,1-1-25,Round 1: 0.409474073760554783,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,26,1-1-26,Round 1: 0.479552190490587272,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,29,1-1-29,Round 1: 0.529969995152051267,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,30,1-1-30,Round 1: 0.112773310820062372,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,31,1-1-31,Round 1: 0.208330941495224037,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,32,1-1-32,"Round 1: 0.449944031234436358, 0.587821530419282706",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,33,1-1-33,Round 1: 0.118872869218633156,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,34,1-1-34,"Round 1: 0.322576807489487889, 0.381153319066954782, 0.532288346115445426",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,36,1-1-36,"Round 1: 0.033047000431731126, 0.244583870262260132, 0.541385402027460067",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,38,1-1-38,"Round 1: 0.296786818243812972, 0.346099186186996541, 0.455867784023509508",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,39,1-1-39,"Round 1: 0.439082589870627663, 0.511535095220129086",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,41,1-1-41,"Round 1: 0.148132577388464219, 0.340495795973035830, 0.522439318423295626",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,42,1-1-42,Round 1: 0.212991326138100249,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,43,1-1-43,Round 1: 0.240183731597963005,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,44,1-1-44,"Round 1: 0.284246361745720990, 0.408131055027015813",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,45,1-1-45,Round 1: 0.483156039773208586,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,46,1-1-46,Round 1: 0.112386170641044905,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,47,1-1-47,Round 1: 0.578072521957780372,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH1,49,1-1-49,"Round 1: 0.002880564051612223, 0.216588221944451209, 0.565629561399962707",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,1,1-2-1,"Round 1: 0.200269401620671924, 0.588219390083415326",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,3,1-2-3,Round 1: 0.556310137163677574,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,5,1-2-5,Round 1: 0.335128720082782913,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,6,1-2-6,Round 1: 0.255851779068617351,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,9,1-2-9,Round 1: 0.550019246682817134,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,10,1-2-10,Round 1: 0.592239179049270648,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,11,1-2-11,"Round 1: 0.251282454083900554, 0.319835246353096388, 0.398402262052188108, 0.433673663819186867, 0.565325261324054241",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,17,1-2-17,Round 1: 0.515300311772300733,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,18,1-2-18,Round 1: 0.324999143565994221,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,21,1-2-21,Round 1: 0.157409870257554908,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,23,1-2-23,"Round 1: 0.314469592580976433, 0.518004926452552259",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,24,1-2-24,"Round 1: 0.095999272503848903, 0.599701743226749245",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,25,1-2-25,Round 1: 0.586109675457053870,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,26,1-2-26,Round 1: 0.260935346546061099,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,27,1-2-27,Round 1: 0.523672489892825561,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,28,1-2-28,Round 1: 0.537990547079202759,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,30,1-2-30,Round 1: 0.362971605520646737,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,31,1-2-31,Round 1: 0.196644208196207459,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,32,1-2-32,Round 1: 0.491363015931819301,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,33,1-2-33,"Round 1: 0.062853954571512320, 0.311811197044415409, 0.572096877087233580",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,34,1-2-34,"Round 1: 0.142832859029728968, 0.565662616541529811",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,36,1-2-36,"Round 1: 0.190827791505672354, 0.363374503103466114, 0.586268170434938724",NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,37,1-2-37,Round 1: 0.308660387565970553,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,41,1-2-41,Round 1: 0.478144247745635838,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,44,1-2-44,Round 1: 0.480624736156944816,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,45,1-2-45,Round 1: 0.397296039018811886,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,46,1-2-46,Round 1: 0.216836336789038884,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,48,1-2-48,Round 1: 0.559079674929673309,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,49,1-2-49,Round 1: 0.243597388394066461,NOT_AUDITED,,,\r
J2,,TABULATOR1,BATCH2,50,1-2-50,Round 1: 0.509376553653981092,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,1,2-1-1,Round 1: 0.174827909206366766,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,5,2-1-5,Round 1: 0.253868945804680190,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,10,2-1-10,Round 1: 0.183845534305502591,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,11,2-1-11,Round 1: 0.184091347518858067,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,12,2-1-12,Round 1: 0.473762077966488943,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,13,2-1-13,"Round 1: 0.463911403327801083, 0.478886353497674138",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,15,2-1-15,Round 1: 0.102547883957417408,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,16,2-1-16,"Round 1: 0.596914117213201020, 0.604261557732108474, 0.606329660695034502",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,17,2-1-17,Round 1: 0.484431122578305392,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,20,2-1-20,Round 1: 0.110093378367287998,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,21,2-1-21,"Round 1: 0.318051657751695039, 0.469340057505201478, 0.581385706467256721",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,24,2-1-24,"Round 1: 0.097221063483106748, 0.216069107742591473, 0.435454963522845368",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,27,2-1-27,Round 1: 0.330121156354710204,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,28,2-1-28,"Round 1: 0.000308070760244463, 0.476452889056142113",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,30,2-1-30,Round 1: 0.552205933826374149,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,33,2-1-33,"Round 1: 0.156485875522184003, 0.487912460420789715",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,35,2-1-35,Round 1: 0.462636330282825262,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,36,2-1-36,Round 1: 0.002470081598074708,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,38,2-1-38,Round 1: 0.366453282215648288,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,39,2-1-39,Round 1: 0.435498889965574284,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,42,2-1-42,Round 1: 0.276918666579378911,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,43,2-1-43,"Round 1: 0.204596396087436469, 0.228670816604046792",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,44,2-1-44,Round 1: 0.553250150964599060,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,45,2-1-45,Round 1: 0.476694010051945716,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,46,2-1-46,Round 1: 0.470573657126071951,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,47,2-1-47,Round 1: 0.548661663344416171,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,49,2-1-49,Round 1: 0.497896097476605193,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH1,50,2-1-50,Round 1: 0.080650928407955553,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,1,2-2-1,Round 1: 0.185417954749015145,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,2,2-2-2,"Round 1: 0.252054739518646128, 0.297145021317217438",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,3,2-2-3,"Round 1: 0.179114059650472941, 0.443867094961314498, 0.553767880261132538",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,4,2-2-4,Round 1: 0.583133559190710795,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,5,2-2-5,"Round 1: 0.462119987445142117, 0.593645562906652185",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,6,2-2-6,Round 1: 0.414184312862040881,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,9,2-2-9,Round 1: 0.447599261777145722,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,11,2-2-11,"Round 1: 0.250665144751160671, 0.258202051231038729",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,12,2-2-12,Round 1: 0.073500696710547386,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,14,2-2-14,"Round 1: 0.497028461661599238, 0.505850110404388289, 0.534595514875242114",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,15,2-2-15,Round 1: 0.127905826632783042,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,16,2-2-16,"Round 1: 0.321474593451909340, 0.363117127085779029, 0.600674679152988562",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,17,2-2-17,Round 1: 0.099639716476785535,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,18,2-2-18,"Round 1: 0.310761655408463036, 0.323623988797199132, 0.361751737266048034, 0.553316604496940311",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,21,2-2-21,"Round 1: 0.183598492644290687, 0.452025881596314978, 0.553486129413447630",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,22,2-2-22,Round 1: 0.399417167287101667,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,24,2-2-24,"Round 1: 0.254713483413602723, 0.519011395038289762",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,25,2-2-25,Round 1: 0.577357702257486608,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,26,2-2-26,Round 1: 0.361183631251847107,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,27,2-2-27,"Round 1: 0.599695787698543334, 0.605483927779177915",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,31,2-2-31,"Round 1: 0.285848417071806894, 0.392061463705112035, 0.398834278274307803",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,33,2-2-33,Round 1: 0.471697932506336915,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,34,2-2-34,"Round 1: 0.025432662687164598, 0.312681839495626376",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,35,2-2-35,Round 1: 0.499180245955838164,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,36,2-2-36,Round 1: 0.356120105875928110,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,38,2-2-38,Round 1: 0.196959175122632514,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,44,2-2-44,"Round 1: 0.075387549784560452, 0.467775592407713539",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,45,2-2-45,Round 1: 0.562831537934447857,NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,47,2-2-47,"Round 1: 0.279396215658234839, 0.523916751996056335",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,48,2-2-48,"Round 1: 0.524819562318245006, 0.577523249886514950",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,49,2-2-49,"Round 1: 0.117383068698164606, 0.538997034797609266, 0.556321033336187185",NOT_AUDITED,,,\r
J2,,TABULATOR2,BATCH2,50,2-2-50,Round 1: 0.163979608353662975,NOT_AUDITED,,,\r
"""