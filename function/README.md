# Azure Queues and Service Bus queues - compared and contrasted

This article analyzes the cost effectiveness of choosen Azure web app and the Azure function

- Your application must store over 80 GB of messages in a queue, where the messages have a lifetime shorter than 7 days.

- Your application wants to track progress for processing a message inside of the queue. This is useful if the worker processing a message crashes. A subsequent worker can then use that information to continue from where the prior worker left off.

- You require server side logs of all of the transactions executed against your queues.

- Your solution must be able to receive messages without having to poll the queue. With Service Bus, this can be achieved through the use of the long-polling receive operation using the TCP-based protocols that Service Bus supports.

- You would like to be able to publish and consume batches of messages.

- You require full integration with the Windows Communication Foundation (WCF) communication stack in the .NET Framework.

## Predict the monthly cost of each Azure Resource

The tables in the following sections provide the prediction of monthly cost analysis of each Azure Resources.

| Azure Resources       | Specs|  Monthly Cost |
| --------------------- |----------------- |-|
| Storage account  |Block Blob Storage, General Purpose V1, LRS Redundancy, 1,000 GB Capacity - Pay as you go, 100 Storage transactions | $24.04 |  
| Service Bus  |Standard tier: 1, 1 Hybrid Connect listener(s) + 0 overage per GB, 1 relay hour(s), 1 relay message(s)| $19.70  |   
| App Service (Shared Instance) | Standard Tier; 1 S1 (1 Core(s), 1.75 GB RAM, 50 GB Storage) x 1 Month; Linux OS | $74.05   |   
| Azure Database for PostgreSQL |Single Server Deployment, Basic Tier, 1 Gen 5 (2 vCore) x 1 Month, 5 GB Storage, 100 GB Additional Backup storage - LRS redundancy  | $77.08|   
| Push-style API        | | **No**  |     
| Receive mode          | |  ffff   |
| Exclusive access mode | |**Lease-based**  |  
| Lease/Lock duration   | |**30 seconds (default) |  
| Lease/Lock precision  | |**Message level**<br/><br/>| 
| Batched receive       | |**Yes**<br/><br/>| 
| Batched send          | |**No**   |  
