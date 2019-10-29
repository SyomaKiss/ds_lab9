# ds_lab9

### rs.status()

```rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T21:43:07.272Z"),
	"myState" : 2,
	"term" : NumberLong(5),
	"syncingTo" : "mongo1:27017",
	"syncSourceHost" : "mongo1:27017",
	"syncSourceId" : 0,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572385380, 1),
			"t" : NumberLong(5)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T21:43:00.704Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572385380, 1),
			"t" : NumberLong(5)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T21:43:00.704Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572385380, 1),
			"t" : NumberLong(5)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572385380, 1),
			"t" : NumberLong(5)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T21:43:00.704Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T21:43:00.704Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572385320, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572385320, 1),
	"members" : [
		{
			"_id" : 0,
			"name" : "mongo1:27017",
			"ip" : "172.31.40.99",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 18317,
			"optime" : {
				"ts" : Timestamp(1572385380, 1),
				"t" : NumberLong(5)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572385380, 1),
				"t" : NumberLong(5)
			},
			"optimeDate" : ISODate("2019-10-29T21:43:00Z"),
			"optimeDurableDate" : ISODate("2019-10-29T21:43:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T21:43:07.268Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T21:43:06.599Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572382078, 1),
			"electionDate" : ISODate("2019-10-29T20:47:58Z"),
			"configVersion" : 1
		},
		{
			"_id" : 1,
			"name" : "mongo2:27017",
			"ip" : "172.31.3.145",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 25576,
			"optime" : {
				"ts" : Timestamp(1572385380, 1),
				"t" : NumberLong(5)
			},
			"optimeDate" : ISODate("2019-10-29T21:43:00Z"),
			"syncingTo" : "mongo1:27017",
			"syncSourceHost" : "mongo1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "mongo3:27017",
			"ip" : "172.31.42.168",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 920,
			"optime" : {
				"ts" : Timestamp(1572385380, 1),
				"t" : NumberLong(5)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572385380, 1),
				"t" : NumberLong(5)
			},
			"optimeDate" : ISODate("2019-10-29T21:43:00Z"),
			"optimeDurableDate" : ISODate("2019-10-29T21:43:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T21:43:05.485Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T21:43:05.659Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongo1:27017",
			"syncSourceHost" : "mongo1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572385380, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572385380, 1)
}
```

### rs.config()

```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongo1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongo2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongo3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db84db2407f1ca69724f7a1")
	}
}
```
![before](images/img1.png)

# AFTER
### rs.status()
```
rs0:PRIMARY> rs.status()
{
	"set" : "rs0",
	"date" : ISODate("2019-10-29T21:53:07.679Z"),
	"myState" : 1,
	"term" : NumberLong(6),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572385983, 1),
			"t" : NumberLong(6)
		},
		"lastCommittedWallTime" : ISODate("2019-10-29T21:53:03.723Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572385983, 1),
			"t" : NumberLong(6)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-29T21:53:03.723Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572385983, 1),
			"t" : NumberLong(6)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572385983, 1),
			"t" : NumberLong(6)
		},
		"lastAppliedWallTime" : ISODate("2019-10-29T21:53:03.723Z"),
		"lastDurableWallTime" : ISODate("2019-10-29T21:53:03.723Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572385923, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572385923, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-29T21:45:02.642Z"),
		"termAtElection" : NumberLong(6),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572385500, 1),
			"t" : NumberLong(5)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572385500, 1),
			"t" : NumberLong(5)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-29T21:45:03.710Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-29T21:45:05.082Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "mongo1:27017",
			"ip" : "172.31.40.99",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-29T21:53:03.228Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T21:45:02.680Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "mongo2:27017",
			"ip" : "172.31.3.145",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 26176,
			"optime" : {
				"ts" : Timestamp(1572385983, 1),
				"t" : NumberLong(6)
			},
			"optimeDate" : ISODate("2019-10-29T21:53:03Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572385502, 1),
			"electionDate" : ISODate("2019-10-29T21:45:02Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "mongo3:27017",
			"ip" : "172.31.42.168",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 1520,
			"optime" : {
				"ts" : Timestamp(1572385983, 1),
				"t" : NumberLong(6)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572385983, 1),
				"t" : NumberLong(6)
			},
			"optimeDate" : ISODate("2019-10-29T21:53:03Z"),
			"optimeDurableDate" : ISODate("2019-10-29T21:53:03Z"),
			"lastHeartbeat" : ISODate("2019-10-29T21:53:06.916Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-29T21:53:07.331Z"),
			"pingMs" : NumberLong(1),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "mongo2:27017",
			"syncSourceHost" : "mongo2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572385983, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572385983, 1)
}
rs0:PRIMARY>
```

### rs.config()

```
rs0:PRIMARY> rs.config()
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "mongo1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "mongo2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "mongo3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5db84db2407f1ca69724f7a1")
	}
}
```
![after](images/img2.png)



