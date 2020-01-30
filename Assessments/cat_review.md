# Availability review

## Application design
1. Are multiple instances of the app/database running?
    - Risks
      - Individual virtual machines (VMs) become single points of congestion.
      - Database becomes a single point of failure.
    - Recommendations
      - Deploy the application in multiple Azure paired regions.
      - Use auto-failover and active geo-replication for SQL Database.
      - Use Azure Managed Database Services for turnkey global distribution.
      - Deploy multiple instances of the web app.
2. Are there different SLAs for application components?
    - Risks
      - Not decomposing services based on their SLAs makes it difficult to manage these services for their availability.
    - Recommendations
      - Consider adopting a microservices architecture.
3. Is there a message broker?
    - Risks
      - Transactions may get lost during congestion/load while waiting to get processed.
    - Recommendations
      - Use Service Bus Queues between the front end and back end.
4. How’s throttling implemented?
    - Risks
      - Load continues to hit the application running with stretched resources, affecting even further loss of available resources.
    - Recommendations
      - Use the Throttling pattern. 

## Deployment and maintenance
5. Are multiple datacenters (DCs) used?
    - Risks
      - An outage in one region brings down application availability.
    - Recommendations
      - Deploy multiple instances of the web app.
      - Deploy the application in multiple Azure paired regions.
6. Is deployment and testing implemented?
    - Risks
      - Manual deployment can add human error, bringing down availability.
      - Untested deployment process poses a risk to availability.
    - Recommendations
      - Use Continuous Integration and Delivery with Visual Studio Team Services (VSTS).
7. Are staging/production or rolling updates used?
    - Risks
      - Applications becomes unavailable when a new version is rolled into production.
    - Recommendations
      - Use staging slots in Azure App Service.
8. Is the application deployed using any technologies or methods to maintain high availability?
    - Risks
      - Applications becomes unavailable during planned/unplanned maintenance.
    - Recommendations
      - Use an App Service plan that offers multiple instances.
      - Use virtual machine scale set.
      - Deploy multiple instances of the web app.

### Data management
9. Is geo-replication of storage implemented?
    - Risks
      - Application becomes unavailable in case of outage or unavailability of storage.
    - Recommendations
      - Use Azure Storage replication.
10. Is geo-replication of databases implemented?
    - Risks
      - Application becomes unavailable in case of outage or unavailability of primary database.
    - Recommendations
      - Utilize auto-failover and active geo-replication for SQL Database.
      - Use Azure Managed Database Services for turnkey global distribution.
11. How’s consistency and concurrency implemented?
    - Risks
      - Transactions are queued, affecting application availability when load starts to increase.
    - Recommendations
      - Practice appropriate consistency and isolation level while making database connection.
12. Are backup/restore operations scheduled and tested?
    - Risks
      - Unscheduled and untested backup/restore operations are a risk to continued availability if they do not meet the recovery point objective (RPO).
    - Recommendations
      - Employ Azure to Azure Site Recovery.

### Errors and failures
13. Are request timeouts configured?
    - Risks
      - Very short timeouts can cause excessive retry operations for services and resources that have considerable latency.
      - Very long timeouts can cause blocking if a large number of requests are queued, waiting for a service or resource to respond.
    - Recommendations
      - Set SQL Connection timeout to 30s.
      - Use guidance on troubleshoot, diagnose, and prevent SQL connection errors and transient errors for SQL Database.
14. How are transient network/other errors handled? Is there a Retry pattern?
    - Risks
      - Application becomes unavailable during a transient error.
    - Recommendations
      - Use the Retry pattern.
15. Is the Circuit Breaker pattern implemented?
    - Risks
      - Failure in one part of the system can lead to cascading failures, resulting in many operations becoming blocked while holding onto critical system resources, such as memory, database connections.
    - Recommendations
      - Use the Circuit Breaker pattern.
16. Are application components decomposed and used?
    - Risks
      - Inability to detect and avoid sending requests to failed instances minimizes availability.
    - Recommendations
      - Utilize Application Gateway health monitoring.
      - Use Azure Traffic Manager health probing.
17. Is the CQRS (Command and Query Responsibility Segregation) pattern implemented?
    - Risks
      - Command (INSERT/UPDATE) and Query (SELECT) operations target the same resource (database) affecting availability.
    - Recommendations
      - Use the CQRS pattern in Azure.

### Monitoring and disaster recovery
18. Are errors/failures captured and reported?
    - Risks
      - Inability to provide sufficient data to enable operations staff to determine the cause, mitigate the situation, and ensure availability.
    - Recommendations
      - Use Azure Log Analytics for a detailed reporting on errors and failures.
      - Employ Service Map and Application Map for coherent error/failure reporting.
19. Are health probes implemented?
    - Risks
      - Inability to validate response, measure latency, and extract information on availability.
    - Recommendations
      - Use Application Gateway health monitoring.
      - Utilize Azure Traffic Manager health probing.
20. Are failover/fallback processes orchestrated?
    - Risks
      - Undetected system and operation changes affect availability.
    - Recommendations
      - Use Azure to Azure Site Recovery.
21. What monitoring tools are used?
    - Risks
      - Inability to provide sufficient data to enable operations staff to determine the cause, mitigate the situation, and ensure availability.
    - Recommendations
      - Use Azure Monitor to monitor services/infrastructure.
      - Build a customized Azure dashboard.
      - Review monitoring Azure applications and resources guidance.


# Scalability review


## Application design
1. Are you using the Microservices pattern?
    - Risks
      - Inability to distribute application components to maximize the use of each compute unit.
    - Recommendations
      - Consider adopting a microservices architecture.
2. Are you using queues?
    - Risks
      - Inability to route requests and balance application load.
    - Recommendations
      - Employ the Load Levelling pattern using Azure queues/topics.
3. Have you identified a correlation between scaled-up instances (web and SQL)?
    - Risks
      - Possibility of negative impact due to limitation imposed by lack of resources in some part of the overall application.
    - Recommendations
      - Identify a correlation between app instance scaling and database scaling units.
4. Is there client affinity?
    - Risks
      - Possibility of overhead in storing, retrieving, and maintaining state information.
    - Recommendations
      - Avoid using Application Request Routing (ARR) Affinity in the App Service Environment (ASE).
5. What provisions are in place when the load on the application increases?
    - Risks
      - Possibility of delay in additional resources/capacity increase.
    - Recommendations
      - Use Autoscaling guidance.
      - Implement autoscale for services.
6. Are you using background jobs?
    - Risks
      - Possibility of application becoming unresponsive and not taking requests.
    - Recommendations
      - Review background jobs guidance.
      - Use Azure Logic Apps to create and schedule regularly running tasks.

## Data management
7. Are you using multiple databases or sharding?
    - Risks
      - Possibility of poor query performance, complex scalability, poor management, and poor availability.
    - Recommendations
      - Implement partitioning guidance to meet scalability requirements.
8. How are you implementing data consistency?
    - Risks
      - Inability to improve scalability by reducing time needed for data synchronization.
    - Recommendations
      - Use Data Consistency Primer guidance.
      - Ensure appropriate consistency and isolation level while making database connections.
9. Are you using data batch operations?
    - Risks
      - Inability to reduce chatty operations with database/services.
    - Recommendations
      - Use batch queries over multiple and frequent queries.
10. Are you using queues/cache?
    - Risks
      - Possibility of services becoming overwhelmed causing escalating failure.
      - Inability to reduce load on database that generates and serves data.
    - Recommendations
      - Review caching guidance.
      - Use the Queue-Based Load Leveling pattern.
      - Use Service Bus Queue/topic.
      - Employ Azure Redis Cache to cache frequently used data.
11. Are you using offline data processing?
    - Risks
      - Inability to serialize/deserialize XML/JSON data and store it in native database datatype making it difficult to scale.
    - Recommendations
      - Consider using Azure Cosmos DB for storing XML/JSON documents.
12. Have you optimized database queries/indexes?
    - Risks
      - Possibility of poor query/database performance.
    - Recommendations
      - Review Query Tuning guidance.
      - Utilize automatic tuning in Azure SQL Database.
      - Use Azure Managed Database Services for automatic tuning.
13. Do you have plans for data growth and retention?
    - Risks
      - Possibility of increased latency, and reduced application throughput and performance.
    - Recommendations
      - Manage future growth with options provided by Azure SQL Database.
      - Use Azure Managed Database Services for built-in security, automatic monitoring, threat detection, automatic tuning, and turnkey global distribution.
14. Are you using a content delivery network (CDN)?
    - Risks
      - Inability to reduce server load for dynamically generated content for each request.
    - Recommendations
      - Review content delivery network guidance.
      - Utilize cache control headers when applicable.

### Implementation
15. Are you using the async/await pattern?
    - Risks
      - Possibility of locking the thread while accessing resources with higher latency, limited I/O, or network bandwidth.
    - Recommendations
      - Use the Asynchronous Programming pattern available in your programming language.
16. What is your locking approach?
    - Risks
      - Possibility of poor performance from services with high latency.
    - Recommendations
      - Ensure appropriate consistency and isolation level while making database connection.
17. Are you using data compression?
    - Risks
      - Inability to reduce load on the network.
    - Recommendations
      - Use GZip compression in web.config.
      - Utilize bundling and minification.
18. Are you using connection pooling?
    - Risks
      - Inability to limit connection resources.
    - Recommendations
      - Use SQL Database connection pooling.
19. Have you conducted performance profiling and load testing?
    - Risks
      - Inability to determine if application performs and scales as expected.
    - Recommendations
      - Run VSTS load testing for regular stress testing to identify and fix hotspots.

# Resiliency review


## Requirements
1. Are resiliency requirements (SLA, RPO, and others) documented/desired in the new system?
    - Risks
      - Incorrect documentation leads to a system design that may not meet the customer's expectations.
    - Recommendations
      - Review resiliency requirements guidance.

## Application design
2. Is failure mode analysis (FMA) performed?
    - Risks
      - Inability to identify what types of failures an application might experience, capture the potential effects and impacts of each type of failure on the application, and identify recovery strategies.
    - Recommendations
      - Perform failure mode analysis to identify possible failures, impacts, and recovery strategies.
3. Are multiple app service instances deployed?
    - Risks
      - Individual VMs become single points of congestion.
      - Database becomes a single point of failure.
    - Recommendations
      - Utilize an App Service plan that offers multiple instances.
      - Use virtual machine scale sets.
      - Deploy multiple instances of the web app.
4. What provisions are in place when the load on the application increases?
    - Risks
      - Possibility that the application's services will fail if they become saturated with user requests.
    - Recommendations
      - Implement autoscale for services.
5. Is load balancing implemented?
    - Risks
      - Inability to distribute an application's requests to healthy service instances by removing unhealthy instances from rotation.
    - Recommendations
      - Adopt Load Balancer to distribute the load on the application.
      - Use Azure Traffic Manager.
6. Is the application deployed using RAID clusters to maintain high availability?
    - Risks
      - Inability to serve user requests when an instance of a service goes down.
    - Recommendations
      - Deploy the application in multiple Azure paired regions.
      - Deploy multiple instances of the web app.
7. Is multi-DC set up implemented?
    - Risks
      - Inability to serve user requests when a site goes down.
    - Recommendations
      - Use business continuity and disaster recovery (BCDR): Azure paired regions.
8. Are health probes/checks implemented for load balancers (LB) and application gateway (AGW)?
    - Risks
      - Inability to prevent user requests going to faulty instance of service.
    - Recommendations
      - Use the Health Endpoint Monitoring pattern.
9. Are third-party services monitored?
    - Risks
      - Inability to gauge the effect of third-party services on the application.
    - Recommendations
      - Review monitoring and diagnostics guidance.
      - Utilize Analytics in Application Insights to predict reliability issues and monitor third-party SLAs.
10. Are third-party services SLAs bound?
    - Risks
      - Inability to serve user requests when third-party service goes down.
    - Recommendations
      - Implement the Health Endpoint Monitoring pattern.
11. Are Retry and Circuit Breaker patterns used?
    - Risks
      - Inability to serve user requests when remote service communication fails.
    - Recommendations
      - Use the Retry pattern and Circuit Breaker pattern.
      - Use resiliency strategies and asynchronous programming with async and await.

### Data management
12. Are storage and database services replicated/fail-over?
    - Risks
      - Inability to serve user requests when storage and/or database service fails.
    - Recommendations
      - Use Azure Storage replication and SQL Database active geo-replication to ensure that the application's data requirements are satisfied.
      - Employ Azure Managed Database Services for turnkey global distribution.
13. Is the user account for the production database and backup separate?
    - Risks
      - A single user can maliciously delete _all_ data (original and backup) resulting in compromised backup.
    - Recommendations
      - Keep user permissions separate between production and backup data.
14. Are failover and fallback processes orchestrated/tested?
    - Risks
      - Inability to verify that an operator following the processes can successfully fail over and fail back the data source.
    - Recommendations
      - Use auto-failover and active geo-replication for SQL Database.
      - Employ Azure Managed Database Services for built-in resiliency.
15. Is data backup validated?
    - Risks
      - Inability to validate data integrity, schema, and queries of the backup.
    - Recommendations
      - Use automatic SQL Database backups.

### Security
16. Is web application firewall (WAF) and distributed denial-of- service (DDoS) protection enabled?
    - Risks
      - Inability to distinguish true user requests from malicious user requests.
    - Recommendations
      - Use WAF in front of a web app.
      - Review Azure DDoS Protection guidance.
      - Utilize Azure Key Vault to manage secrets, such as _connectionstring._
17. Is role-based access control (RBAC) implemented?
    - Risks
      - Possibility of someone purposely or accidentally deleting resources making application unavailable.
    - Recommendations
      - Use RBAC with Azure AD for Azure subscription.
      - Utilize Azure Security Center for threat detection and protection.

### Testing
18. Are the failover and failback processes tested?
    - Risks
      - Uncertainty on application services coming back online in a synchronized manner.
    - Recommendations
      - Use Azure Site Recovery failback process for servers.
19. Is fault-injection testing done?
    - Risks
      - Uncertainty on ability to recover from all types of faults, alone and in combination.
      - Uncertainty on cascading failures in system.
    - Recommendations
      - Test the application by simulating or triggering real failures, such as deleting certificates, artificially consuming system resources, or deleting a storage source.
20. Is performance testing done?
    - Risks
      - Uncertainty on application behavior in production under real load and fully deployed.
    - Recommendations
      - Use load testing with VSTS to identify application behavior under load.

### Deployment
21. Is the release process automated and documented?
    - Risks
      - Possibility of an operator deploying a bad update or improperly configuring settings for an application.
    - Recommendations
      - Use VSTS release management for end-to-end traceability.
      - Utilize VSTS history and auditing for a consolidated view of changes to code and infrastructure.
22. Are blue/green or canary release deployment techniques used?
    - Risks
      - Possibility of users not being redirected to production code in the event of a failure.
    - Recommendations
      - Use the blue/green or canary release deployment technique.
23. Is the deployment process logged and audited?
    - Risks
      - Inability to determine which version of an application is causing a problem after a new release.
    - Recommendations
      - Use VSTS release management for end-to-end traceability.
      - Utilize VSTS history and auditing for a consolidated view of changes to code and infrastructure.
24. Do you have a rollback plan?
    - Risks
      - Inability to go back to a last- known good version and minimize downtime.
    - Recommendations
      - Use App Service deployment slots to fall back on last-known good menu.
      - Run VSTS conditional rollback.

### Operations
25. Have you implemented alerting and monitoring?
    - Risks
      - Inability to detect failures in an application and alert an operator to fix them.
    - Recommendations
      - Review monitoring and diagnostics guidance.
      - Review monitoring Azure applications and resources guidance.
26. Are remote API/SQL call statistics available to the app team?
    - Risks
      - Inability to have an instantaneous view into the health of an application and reveal issues in the services.
    - Recommendations
      - Employ usage analysis with Application Insights.
27. Do you track retries for transient errors?
    - Risks
      - Possibility of an issue or failure remaining hidden by an application's retry logic.
    - Recommendations
      - Review retry service-specific guidance.
28. Have you assigned operators for system alerts?
    - Risks
      - Possibility of unidentified issues becoming critical.
    - Recommendations
      - Use action groups to ensure people receive alerts.
29. Are multiple people trained for monitoring?
    - Risks
      - Possibility of a single person being unavailable, resulting in a single point of failure.
    - Recommendations
      - Train multiple people on Azure Monitor.
      - Send alerts and notifications to multiple recipients.
30. Are your Azure subscription/service limits documented and known within the team?
    - Risks
      - Possibility of poor customer experience when hit with subscription limits.
    - Recommendations
      - Review Azure subscription limits.
31. Are VM sizes appropriate for your workload?
    - Risks
      - Possibility of application experiencing capacity issues when VMs approach their limit.
    - Recommendations
      - Use VSTS load testing for regular stress testing to identify and fix capacity hotspots.
32. Is the DB/SQL tier right for your workload?
    - Risks
      - Possibility of data use getting throttled.
    - Recommendations
      - Review SQL Database options and performance guidance.
      - Use Azure Managed Database Services for built-in automatic tuning.
33. Is the process to contact Azure support understood by your team?
    - Risks
      - Possibility of prolonged downtime as support process is navigated for the first time.
    - Recommendations
      - Understand Azure support plans.
      - Refer to Azure support FAQs.
      - Familiarize your team with Azure support.

### Telemetry
34. Do you collect all telemetric information?
    - Risks
      - Possibility of not having sufficient information for issues while they are actively serving users.
    - Recommendations
      - Use Azure Application Insights to log and monitor application events and exceptions.
35. Have you used the async pattern for logging?
    - Risks
      - Possibility of logging operations blocking application code.
    - Recommendations
      - Use the asynchronous programming with async and await pattern.
36. Do you have correlated log information across tiers?
    - Risks
      - Inability of tracking user requests across multiple tiers/Azure services.
    - Recommendations
      - Use Service Map and Application Map for logs across multiple components.

# DevOps review


## Culture
1. Do all stakeholders have a single view of goals and timelines?
    - Risks
      - Possibility of conflict over resources, purposes, goals, and priorities.
    - Recommendations
      - Adopt VSTS Agile as a single source of truth for all stakeholders to avoid mismatched expectations and to give an accurate picture of the current status.
2. Have you automated build, test, and deployment?
    - Risks
      - Inability to know what each team member is doing and should be doing in the future.
    - Recommendations
      - Utilize VSTS continuous testing.
      - Use VSTS Test Case Management for documenting and fixing bugs after test execution.
      - Practice VSTS Unit, Integration, and UAT testing for code coverage.
3. Have you implemented continuous improvement?
    - Risks
      - Inability to quickly identify issues, escalate, fix, and confirm resolution.
    - Recommendations
      - Use VSTS dashboards and VSTS Power BI integration for data-driven reporting and improvement.
4. Do you have documented operations?
    - Risks
      - Inability to understand design, architecture, tools, processes, and code.
    - Recommendations
      - Track ideas to implementation using VSTS work-item tracking.
      - Implement DevOps using VSTS.
5. How do you share knowledge within the team?
    - Risks
      - Inability to keep knowledge organized and quickly discoverable.
    - Recommendations
      - Use VSTS Wiki to distribute information, share knowledge, and collaborate.

## Development
6. Do you have a production-like environment for dev/test?
    - Risks
      - Inability to test and diagnose problems.
    - Recommendations
      - Use VSTS load testing with cloud scale and mimic real- life, peak-usage scenario.
7. Do you have existing scripts for deployment?
    - Risks
      - Possibility of needing manual tasks or detailed technical knowledge of application.
    - Recommendations
      - Employ Azure Resource Manager and VSTS to implement infrastructure-as- code model.
8. Are you using application instrumentation for insight?
    - Risks
      - Inability to understand application health, performance, or errors.
    - Recommendations
      - Use Azure Monitor, Azure Advisor, Azure Service Health, Activity Log, Azure Application Insights, Log Analytics, ExpressRoute monitor, Service Map, availability tests, and general monitoring Azure applications and resources.
9. Are you tracking technical debt?
    - Risks
      - Possibility of shortcuts and non-optimal code with respect to the release schedule.
    - Recommendations
      - Track technical debt using SonarQube with Visual Studio Team Services (VSTS).
10. How do you push updates to production?
    - Risks
      - Inability to reduce cycle time for production release.
    - Recommendations
      - Use feature toggles and canary releases.
      - Utilize App Service deployment slots to safely deploy applications.

### Testing
11. Have you automated testing?
    - Risks
      - Possibility of tedious and error-prone manual testing.
    - Recommendations
      - Review development and test guidance.
      - Use VSTS continuous testing.
      - Use VSTS Test Case Management for documenting and fixing bugs after test execution.
      - Practice VSTS Unit, Integration, and UAT testing for code coverage.
12. How do you test in production?
    - Risks
      - Inability to determine if code is working as expected.
    - Recommendations
      - Use App Service deployment slots for testing in production.
13. How do you manage performance, load, and stress testing?
    - Risks
      - Inability to detect serious performance issues.
    - Recommendations
      - Practice VSTS load testing with cloud scale.
14. How do you manage capacity testing?
    - Risks
      - Inability to determine resource limitations.
    - Recommendations
      - Use VSTS load testing for regular stress testing to identify and fix resource limitations.
15. Are you doing penetration testing?
    - Risks
      - Inability to determine possible vulnerabilities and attacks.
    - Recommendations
      - Request a penetration test for your application.
16. Do you have BCP (Business Continuity Process)/DR (Disaster Recovery) drills?
    - Risks
      - Inability to determine business continuity.
    - Recommendations
      - Review guidance on disaster recovery for Azure applications.
      - Use Azure Site Recovery drills.

### Release
17. Have you automated release and deployment?
    - Risks
      - Inability to release consistent deployments quickly and reliably.
    - Recommendations
      - Use VSTS Release Management for continuous delivery of software at a faster pace and with lower risk.
18. Do you use continuous integration (CI)?
    - Risks
      - Inability to let developers work on a single codebase and find bugs early.
    - Recommendations
      - Employ VSTS continuous integration to build, test, and deploy applications quickly.
19. Do you use continuous delivery (CD)?
    - Risks
      - Inability to deliver tested production code in a very short time.
    - Recommendations
      - Use VSTS continuous delivery to deploy tested code automatically.
20. Do you document/log changes in deployment?
    - Risks
      - Possibility of confusion and versioning conflict.
    - Recommendations
      - Use VSTS extensions to create documentation from source code.
      - Utilize VSTS history and auditing for a consolidated view of changes to code and infrastructure.
21. How do you prevent infrastructure changes after deployment?
    - Risks
      - Inability to determine ad- hoc changes and their impact.
    - Recommendations
      - Use VSTS access management to grant or restrict access to resources and features you want to control.
      - Use Azure Automation Change Tracking.

### Monitoring
22. How do you monitor the health of your application/services?
    - Risks
      - Inability to determine application health and status.
    - Recommendations
      - Use Azure Monitor, Azure Advisor, Azure Service Health, Activity Log, Azure Application Insights, Log Analytics, ExpressRoute monitor, Service Map, availability tests, and general monitoring Azure applications and resources.
23. How do you correlate logs?
    - Risks
      - Inability to have a cohesive view of issues.
      - Inability to have an up-to- date picture of system health.
    - Recommendations
      - Use Azure Log Analytics for viewing data for a particular application.
      - Utilize Service Map and Application Map for logs across multiple components.
24. Are there automated alerts and notifications?
    - Risks
      - Inability to detect patterns or conditions that indicate potential or current issues and send alerts to address them.
    - Recommendations
      - Create, view, and manage alerts using Azure Monitor.
      - Use Log Analytics Alerts based on conditions in Log Analytics data.
25. How do you monitor assets and resources for expiration?
    - Risks
      - Inability to determine services or features that depend on the expiration of resources.
    - Recommendations
      - Use Azure VM expire and certificate monitoring.

### Management
26. Are there manual activities to automate?
    - Risks
      - Possibility of error-prone manual handling of repetitive operations.
    - Recommendations
      - Use Azure Automation for complete control during deployment, operations, and decommissioning of workloads and resources.
27. Do you have existing scripts for deployment?
    - Risks
      - Inability to minimize the amount of manual configuration needed to provision resources.
    - Recommendations
      - Utilize Azure Resource Manager templates and scripts for automated resource provisioning.
28. Are you planning to use containers?
    - Risks
      - Inability to create self- contained packages, including all dependencies and files needed to run the application, which simplifies the deployment.
    - Recommendations
      - Use VSTS hosted CI/CD for containers to create and deploy containers.
29. Do you have an operations manual?
    - Risks
      - Inability to refer to any documented operations scenarios and mitigation plans during a failure or other disruption in service.
    - Recommendations
      - Use Azure Operations Management Suite (OMS) for process automation.
30. Do you have on-call procedures documented?
    - Risks
      - Inability to refer to on-call duties, schedules, and procedures.
    - Recommendations
      - Employ third-party extensions such as Remedy OnDemand to notify on-call responders for critical VSTS work items.
31. Do you have escalation procedures documented?
    - Risks
      - Inability to deal with outages, including identifying support contacts and escalation paths.
    - Recommendations
      - Practice agile planning and portfolio management with VSTS for a full view of the work escalation and decomposition of tasks.
32. How do you implement configuration management?
    - Risks
      - Inability to plan, create, and record configuration changes and make them visible to operations.
    - Recommendations
      - Employ VSTS configuration management for visibility to dev and operations teams.
      - Use PowerShell DSC for configuration management.
33. Do you have an Azure support plan?
    - Risks
      - Inability to understand details of the plan, how the support process works, getting service limits changed, and opening support tickets.
    - Recommendations
      - Understand Azure support plans.
      - Refer to Azure Support FAQs.
34. Have you implemented RBAC?
    - Risks
      - Inability to manage access to resources and enforce security principles.
    - Recommendations
      - Use role-based access control (RBAC) to grant access based on Azure Active Directory identities and groups.
35. Do you use a bug-tracking system?
    - Risks
      - Possibility of missed items, duplicate work, or introduction of additional problems.
    - Recommendations
      - Utilize VSTS bug tracking tool for establishing links between code and bugs.
      - Use Bugzilla integration with VSTS.
36. Do you audit and track changes in code and infrastructure?
    - Risks
      - Inability to track and audit changes (code, infrastructure, configuration, documentation, and scripts).
    - Recommendations
      - Employ VSTS history and auditing for a consolidated view of changes to code and infrastructure.

# Security review


## Network boundary security
1. How do you implement DDoS protection?
    - Risks
      - Potential of smaller-scale attack that doesn't trip the platform-level protection.
    - Recommendations
      - Use Azure DDoS Protection to prevent volumetric attacks, protocol attacks, and resource (application)-layer attacks.
2. How do you configure public IPs for which traffic is passed in, and how and where it's translated?
    - Risks
      - Inability to provision VMs with private IP addresses for protection.
    - Recommendations
      - Use Azure Firewall for built-in high availability and unrestricted cloud scalability.
      - Utilize Azure IP address to determine which traffic is passed in, and how and where it's translated on to the virtual network.
3. How do you isolate network traffic?
    - Risks
      - Inability to ensure VMs and communication between them remains private within a network boundary.
    - Recommendations
      - Use Azure Virtual Network to allow VMs to securely communicate with each other, the Internet, and on- premises networks.
4. How do you configure traffic flow between multiple application tiers?
    - Risks
      - Inability to define different access policies based on the workload types, and to control traffic flows between them.
    - Recommendations
      - Employ Azure Virtual Network Subnet to designate separate address spaces for different elements or “tiers” within the workload, define different access policies, and control traffic flows between the tiers.
5. How do you route network traffic through security appliances for security boundary policy enforcement, auditing, and inspection?
    - Risks
      - Inability to define communication paths between different tiers within a network boundary.
    - Recommendations
      - Use Azure Virtual Network User Defined Routes (UDR) to control next hop for traffic between Azure, on-premises, and Internet resources through virtual appliance, virtual network gateway, virtual network, or Internet.
6. Do you use firewalls, load balancers, and intrusion detection systems (IDS)/intrusion prevention systems (IPS)?
    - Risks
      - Possibility of not being able to select comprehensive solutions for secure network boundaries.
    - Recommendations
      - Use Network Appliances from Azure Marketplace to deploy a variety of preconfigured network virtual appliances.
      - Utilize Application Gateway WAF to detect and protect against common web attacks.

### Network security
7. How do you segment the larger address space into subnets?
    - Risks
      - Inability to allow or deny inbound network traffic to, or outbound network traffic from, within larger network space.
    - Recommendations
      - Use network security groups (NSGs) to allow or deny traffic to and from single IP address, to and from multiple IP addresses, or even to and from entire subnets.
8. How do you control routing behavior between VM connectivity?
    - Risks
      - Inability to customize the routing configuration.
    - Recommendations
      - Employ Azure Virtual Network User Defined Routes (UDR) to customize the routing configuration for deployments.
9. How do you implement forced tunneling?
    - Risks
      - Potential of outbound connections from any VM increasing attack surface area leveraged by attackers.
    - Recommendations
      - Utilize forced tunneling to ensure that connections to the Internet go through corporate network security devices.
10. How do you implement enhanced levels of security (firewall, IPS/IDS, antivirus, vulnerability management, botnet protection) on top of network-level controls?
    - Risks
      - Inability to enable security for other OSI model layers other than network and transport layer.
    - Recommendations
      - Use Azure Marketplace to provision devices for higher levels of network security than with network-level access controls.
11. How do you establish cross- premises connectivity?
    - Risks
      - Potential of access to company’s information assets on-premises.
    - Recommendations
      - Use Azure site-to-site VPN or ExpressRoute to set up cross- premises connectivity to on- premises networks.
12. How do you implement global load balancing?
    - Risks
      - Inability to make services available even when datacenters might become unavailable.
    - Recommendations
      - Utilize Azure Traffic Manager to load balance connections to services based on the location of the user and/or other criteria.
13. How do you disable RDP/SSH access to virtual machines?
    - Risks
      - Potential for attackers to use brute force techniques to gain access and launch other attacks.
    - Recommendations
      - Disable RDP/SSH access to Azure Virtual Machines and use VPN/ExpressRoute to access these virtual machines for remote management.
14. How do you prevent, detect, and respond to threats?
    - Risks
      - Inability to have a single pane of visibility to prevent, detect, and respond to threats.
    - Recommendations
      - Employ Azure Security Center for increased visibility into, and control over, the security of Azure resources, integrated security monitoring, and policy management across Azure subscriptions.
15. How do you monitor and diagnose conditions of the network?
    - Risks
      - Inability to understand, diagnose, and gain insights to the network in Azure.
    - Recommendations
      - Use Network Watcher to understand, diagnose, and gain insights to the network in Azure.
16. How do you gain access to real- time performance information at the packet level?
    - Risks
      - Inability to investigate an issue in detail for better diagnoses.
    - Recommendations
      - Utilize packet capture to set alerts and gain access to real- time performance information at the packet level.
17. How do you gather data for compliance, auditing, and monitoring the network security profile?
    - Risks
      - Inability to build a deeper understanding of the network traffic pattern.
    - Recommendations
      - Use network security group flow logs to gather data for compliance, auditing, and monitoring of your network security profile.
18. How do you diagnose VPN connectivity issues?
    - Risks
      - Inability to identify the issue and use the detailed logs for further investigation.
    - Recommendations
      - Use Network Watcher troubleshooter to diagnose most common VPN gateway and connections issues.

### Database security
19. How do you restrict database access? Do you use a firewall?
    - Risks
      - Inability to grant access to databases based on the originating IP address of each request.
    - Recommendations
      - Use firewall rules to restrict database access.
      - Utilize Virtual Network service endpoints to secure databases to only your virtual networks.
20. How do you enable database authentication?
    - Risks
      - Inability to prove a user’s identity.
    - Recommendations
      - Use database authentication.
      - Employ Azure Managed Database Services for built-in security, automatic monitoring, threat detection, automatic tuning, and turnkey global distribution.
21. Do you use encryption for data protection?
    - Risks
      - Potential threat of malicious activity.
    - Recommendations
      - Protect data using encryption.
      - Use Storage Encryption, Disk Encryption, and SQL Encryption to encrypt data in Azure.
22. How do you protect data in transit?
    - Risks
      - Susceptibility for man-in- the-middle attacks, eavesdropping, and session hijacking.
    - Recommendations
      - Use Azure site-to-site VPN or ExpressRoute or application- level SSL/TLS for protection.
23. How do you perform database auditing?
    - Risks
      - Inability to maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies.
    - Recommendations
      - Enable database auditing.
      - Use Azure Managed Database Services for built-in security, automatic monitoring, threat detection, automatic tuning, and turnkey global distribution.
24. How do you monitor database threat detection?
    - Risks
      - Inability to identify suspicious database activities, potential vulnerabilities, and SQL injection attacks, as well as anomalous database access patterns.
    - Recommendations
      - Enable database threat detection.

### Data storage security
25. Do you use Azure Multi-Factor Authentication (MFA) for verifying a user’s identity?
    - Risks
      - Risk of credential theft attack, which may lead to data compromise.
    - Recommendations
      - Use Azure AD MFA to secure data and application access without added hassles for customers.
      - Enforce MFA.
26. Do you use RBAC to assign permissions to users, groups, and applications at a certain scope?
    - Risks
      - Risk of giving more privileges than necessary to users, leading to data compromise by having some users having access to data that they shouldn’t have in the first place.
    - Recommendations
      - Use role-based access control (RBAC).
27. Do you encrypt Windows and Linux virtual machine (VM) disks?
    - Risks
      - Risk of data integrity issues, such as malicious or rogue users stealing data and compromised accounts gaining unauthorized access to data.
    - Recommendations
      - Use Azure Disk Encryption to protect and safeguard data to meet organizational security and compliance commitments.
      - Encrypt Azure Virtual Machines.
28. How do you implement key management for data protection?
    - Risks
      - Risk of attackers gaining access to the secret keys to decrypt the data and potentially have access to confidential information.
    - Recommendations
      - Use Azure Key Vault to safeguard cryptographic keys and other secrets used by cloud apps and services.
      - Use Hardware Security Modules.
29. How do you secure workstations for endpoint protection?
    - Risks
      - Risk of attacker compromising workstation and leveraging a user’s credentials to gain access to organizational data.
    - Recommendations
      - Use Azure Information Protection to secure email, documents, and sensitive data shared outside the company.
      - Manage with Secure Workstations.
30. How do you enforce file-level data encryption?
    - Risks
      - Risk of data leakage and lack of business insights monitor for abuse and prevent malicious access to files.
    - Recommendations
      - Use Azure Managed Disks for persistent and secure disk storage for Azure virtual machines.
      - Enforce file-level data encryption.

### Identity management and access control security
31. Do you use a centralized identity management system?
    - Risks
      - Risk of increased administrative overhead in managing accounts, increasing the likelihood of mistakes and security breaches.
    - Recommendations
      - Centralize identity management.
32. How have you enabled Single Sign-On (SSO)?
    - Risks
      - Exposure to scenarios where users have multiple passwords, increasing the likelihood of users reusing passwords or using weak passwords.
    - Recommendations
      - Enable Single Sign-On (SSO).
33. Do you use self-service password reset and password management?
    - Risks
      - Susceptibility to a higher call volume to the service desk due to password issues.
    - Recommendations
      - Deploy password management.
34. Do you enforce multi-factor authentication (MFA) for users?
    - Risks
      - Risk of not complying with industry standards, such as PCI DSS version 3.2 and credential theft type of attack, such as Pass-the- Hash (PtH).
    - Recommendations
      - Enforce MFA for users.
35. Have you implemented role- based access control (RBAC)?
    - Risks
      - Risk of giving more privileges than necessary to users, leading to data compromise by having some users having access to data that they shouldn’t have in the first place.
    - Recommendations
      - Use RBAC.
36. How do you control how resources are created? Do you use governance?
    - Risks
      - Susceptibility to users that may abuse the service by creating more resources than they need.
    - Recommendations
      - Control resource creation using Resource Manager.
37. How do you enforce identity control to access software-as-a- service (SaaS) apps? How do you guide developers on securely integrating apps with the identity management system?
    - Risks
      - Risk of a credential-theft type of attack, such as weak authentication and session management described in Open Web Application Security Project (OWASP) Top 10.
    - Recommendations
      - Guide developers to leverage identity capabilities for SaaS apps.
38. How do you actively monitor for suspicious activities?
    - Risks
      - Risk of compromised user credentials and suspicious activities occurring using these credentials.
    - Recommendations
      - Actively monitor for suspicious activities.
39. How do you manage, monitor, and control access of admin account holders?
    - Risks
      - Risk of compromised admin accounts negating the value of all the other measures taken to ensure the confidentiality and integrity of data.
    - Recommendations
      - Limit and constrain administrative access.

### Operational security
40. How do you harden systems?
    - Risks
      - Exposure of service endpoints that are not required for installed applications.
    - Recommendations
      - Use Security Compliance Manager to import the current configuration by using either group policies based on Active Directory or configuration of a “golden master” reference machine by using the LocalGPO tool. You can then import the local group policy into Security Compliance Manager.
41. How do you manage antimalware?
    - Risks
      - Risk of malware infecting machines.
    - Recommendations
      - Install and manage antimalware.
42. How do you deploy and test a backup solution?
    - Risks
      - Exposure to data loss. • Use Azure Backup to address backup requirements.
43. How do you actively monitor all resources?
    - Risks
      - Inability to visualize, query, route, archive, and take action on the metrics and logs coming from resources.
    - Recommendations
      - Utilize Azure Monitor to get the granular, up-to-date monitoring data all in one place.
      - Use monitoring services.
44. How do you manage and protect your infrastructure?
    - Risks
      - Exposure to gathering data from multiple security and management systems.
    - Recommendations
      - Utilize Azure Monitor to get the granular, up-to-date monitoring data all in one place.
      - Review monitor, manage, and protect cloud infrastructure guidance.
45. How do you collect and process data about resources (security event log, Windows firewall log, antimalware assessment)?
    - Risks
      - Inability to prevent, detect, and respond to threats.
    - Recommendations
      - Use Operations Management Suite (OMS) Security and Audit Solution to collect and processes data about resources.
46. How do you trace requests, analyze usage trends, and diagnose issues?
    - Risks
      - Inability to trace requests, analyze usage trends, and diagnose issues with your storage account.
    - Recommendations
      - Use Azure Security Center for security management and advanced threat protection across hybrid cloud workloads.
      - Review trace requests, analyze usage trends, and diagnose issues guidance.
47. Have you defined security policies according to your company’s security needs, and tailored it to the type of applications or sensitivity of the data?
    - Risks
      - Inability to correlate information from multiple sources to identify threats.
    - Recommendations
      - Use Azure Security Center for security management and advanced threat protection across hybrid cloud workloads.
      - Review Prevent, detect, and respond to threats guidance.
48. How do you implement secure deployment using proven DevOps tools?
    - Risks
      - Potential of unproductive and inefficient enterprises and teams.
    - Recommendations
      - Use Secure DevOps Kit for Azure to build and deploy applications on Azure with security integrated at every step.

# Management tools review


## Monitoring
1. Do you get proactively notified of critical conditions and take corrective action?
    - Risks
      - Risk of critical conditions going unnoticed.
    - Recommendations
      - Use Azure alerts to get proactive notifications.
      - Employ action groups to notify recipients to respond to alerts.
2. How do you combine different kinds of data into a single pane?
    - Risks
      - Inability to combine metrics, activity, usage, and logs for unified monitoring.
    - Recommendations
      - Use Azure dashboards to combine data into a single pane and share it with multiple stakeholders.
3. How do you do additional visualizations and make them available to others within and outside of your organization?
    - Risks
      - Inability to look at monitoring from multiple perspectives and dissecting logs.
    - Recommendations
      - Export Log Analytics data to Power BI to create additional visualizations.
4. How do you monitor the collection of metrics, activity logs, and diagnostic logs?
    - Risks
      - Inability to track when new resources are created/modified, or to monitor performance statistics with trending and detailed analysis.
    - Recommendations
      - Use Azure Monitor for collection of metrics, activity logs, and diagnostic logs.
5. How do you monitor resource configuration and usage telemetry? Do you generate best-practice recommendations from usage?
    - Risks
      - Inability to improve performance, security, and availability.
    - Recommendations
      - Utilize Azure Advisor for monitoring resource configuration and usage telemetry, and to get personalized recommendations based on best practices.
6. How do you identify issues with underlying services that affect your application?
    - Risks
      - Inability to proactively take steps to know about application unavailability and notify application users about it.
    - Recommendations
      - Use Azure Service Health to identify issues with services affecting application and plan for scheduled maintenance.
7. How do you monitor configuration changes, service health incidents, and other similar events?
    - Risks
      - Risk of configuration changes and health incidents going unnoticed.
    - Recommendations
      - Utilize Activity Log for detecting configuration changes, health incidents, better utilization, and autoscale operations.
8. How do you monitor availability, performance, and usage of applications?
    - Risks
      - Inability to achieve deep insights, quickly identify and diagnose errors, and make informed choices on application maintenance and improvements.
    - Recommendations
      - Use Azure Application Insights to monitor availability, performance, and usage of application.
9. Do you analyze logs using query language?
    - Risks
      - Inability to form a complete picture of the operating environment.
    - Recommendations
      - Use Log Analytics to collect data from a variety of resources into a single repository and analyze it using a powerful query language.
10. How do you monitor third-party services (containers, SQL)?
    - Risks
      - Inability to monitor third- party services and their impact on application unavailability.
    - Recommendations
      - Employ Management solutions for monitoring third-party solutions, such as Container Monitoring and Azure SQL Analytics.
11. How do you monitor and diagnose different network scenarios?
    - Risks
      - Inability to detect reachability, latency, and network topology changes between the VM and the endpoint.
    - Recommendations
      - Use Network Watcher for scenario-based monitoring.
12. How do you monitor security, performance, and operations-related insights based on DNS servers?
    - Risks
      - Inability to detect clients that try to resolve malicious domain names, stale resource records, request load on DNS servers, and dynamic DNS registration failures.
    - Recommendations
      - Utilize DNS Analytics for gathering security, performance and operations-related insights of DNS servers.
13. How do you test the reachability of applications and detect performance bottlenecks across on- premises, carrier networks, and cloud/private datacenters?
    - Risks
      - Inability to correlate application delivery with network performance, detect precise location of degradation along the path between the user and the application, and test application reachability from multiple user locations across the globe.
    - Recommendations
      - Employ Service Endpoint Monitoring for testing reachability of applications and detect performance bottlenecks across on- premises, carrier networks and cloud/private data centers.
14. Do you gather insight by analyzing virtual machines with their different processes and dependencies on other computers and external processes?
    - Risks
      - Inability to visualize interconnected systems delivering critical services mapping servers, processes, and ports.
    - Recommendations
      - Use Service Map to gain insight by analyzing virtual machines with their different processes and dependencies on other computers and external processes.
15. How do you monitor connectivity across public clouds, datacenters, and on-premises environments?
    - Risks
      - Inability to detect traffic blackholing, routing errors, and issues that conventional network monitoring methods can’t detect.
    - Recommendations
      - Adopt Network Performance Monitor (NPM) for monitoring across public clouds, datacenters, and on- premises.
16. How do you monitor ExpressRoute circuits?
    - Risks
      - Inability to detect loss and latency across various VNets, monitor all paths
    (including redundant paths),
    troubleshoot transient and
    point-in-time network
    issues, determine a specific
    cause degrading
    performance, track
    throughput per virtual
    network, and see
    ExpressRoute system state
    from a previous point in
    time.
    - Recommendations
      - Use ExpressRoute Monitor for monitoring connectivity and performance of ExpressRoute circuits.

### Configuration
17. How do you automate frequent, time-consuming, and error-prone management tasks?
    - Risks
      - Inability to reduce errors, boost efficiency, and lower operational costs.
    - Recommendations
      - Use automation runbooks with hybrid runbook worker to unify management by orchestrating across on- premises environments.
      - Use webhooks to provide a way to fulfill requests and ensure continuous delivery and operations by triggering automation from ITSM, DevOps, and monitoring systems.
18. How do you monitor and automatically update machine configuration?
    - Risks
      - Inability to automatically receive configurations, conform to the desired state, and report back on compliance.
    - Recommendations
      - Use Azure Automation State Configuration to provide configuration management required for enterprise environments.
19. How do you schedule deployments to orchestrate the installation of updates within a defined maintenance window? How do you get visibility into update compliance?
    - Risks
      - Inability to quickly assess the status of available updates on all agent computers and manage the process of installing required updates for servers.
    - Recommendations
      - Employ Update Management to manage VM updates in Azure, on- premises, or in other cloud providers.
20. How do you monitor resource configuration and usage telemetry? Do you generate best-practice recommendations from usage?
    - Risks
      - Inability to get personalized recommendations to help manage the Azure environment.
    - Recommendations
      - Use Azure Advisor to follow best practices to optimize Azure deployments and analyze your resource configuration and usage telemetry.
21. How do you identify opportunities to reduce overall cost?
    - Risks
      - Inability to identifying idle and underutilized resources.
    - Recommendations
      - Adopt Advisor cost recommendations to optimize and reduce overall Azure spend.
22. How do you generate recommendations with proposed actions inline?
    - Risks
      - Inability to improve speed and responsiveness of applications.
    - Recommendations
      - Review Advisor performance recommendations and Advisor high-availability recommendations for proposed actions inline.
23. How do you deploy, manage, and monitor a solution as a group rather than handling its components individually?
    - Risks
      - Inability to apply common lifecycle to interdependent application parts that can be deployed or deleted in a single action.
    - Recommendations
      - Use Azure Resource Manager to define the dependencies between resources so they're deployed in the correct order.
24. How do you repeatedly deploy solutions throughout the development lifecycle?
    - Risks
      - Lack of confidence that resources are deployed in a consistent state.
    - Recommendations
      - Utilize Azure Resource Manager deployment modes to provision all resources specified in the template.
25. Do you manage infrastructure through declarative templates rather than scripts?
    - Risks
      - Inability to make deployments consistent and repeatable across environments.
    - Recommendations
      - Use Azure Resource Manager templates to ensure that investments for one location are reusable in another.
26. How do you define dependencies between resources so they're deployed in the correct order?
    - Risks
      - Inability to evaluate dependencies between resources and deploy them in their dependent order.
    - Recommendations
      - Use Azure Resource Manager templates to define dependencies for resources that are deployed in the same template.
27. How do you apply access control to all services?
    - Risks
      - Inability to provide fine- grained access management of resources.
    - Recommendations
      - Use Azure Resource Manager RBAC to manage access to Azure resources, what users can do with those resources, and to what areas they have access.
28. How do you apply tags to resources to logically organize all the resources in your subscription?
    - Risks
      - Inability to associate resources with the appropriate department, customer, and environment.
    - Recommendations
      - Utilize resource tags to logically organize Azure resources by categories.
29. Do you clarify your organization's billing by viewing costs for a group of resources?
    - Risks
      - Inability to organize resources for billing or management.
    - Recommendations
      - Use resource tags for the purposes of chargebacks.
30. How do you implement recurring application actions?
    - Risks
      - Inability to create, maintain, and invoke scheduled work for apps.
    - Recommendations
      - Employ Azure Scheduler to declaratively describe actions to run in the cloud, on-premises, or with another provider.
31. How do manage daily pruning of logs, performing backups, and other maintenance tasks?
    - Risks
      - Inability to set multiple one- time and recurring schedules.
    - Recommendations
      - Adopt Azure Scheduler jobs for a wide variety of business scenarios.
32. Do you have browser-based command-line experience for management tasks?
    - Risks
      - Inability to manage Azure resources without the overhead of installing, versioning, and maintaining a machine.
    - Recommendations
      - Use Azure Cloud Shell for an interactive, browser- accessible shell for managing Azure resources.
33. How do you plan to switch between Bash and PowerShell?
    - Risks
      - Inability to integrate with open-source tooling, such as Terraform, Ansible, and Chef InSpec.
    - Recommendations
      - Use Azure Cloud Shell tools for deep integration with open-source tooling.
34. How do you securely authenticate for instant access to resources?
    - Risks
      - Inability to provide secure and automatic authentication account access.
    - Recommendations
      - Use Cloud Shell to secure automatic authentication for the Azure CLI 2.0 and Azure PowerShell.
35. How do you stay connected to your resources regardless of time or location?
    - Risks
      - Inability to keep track of Azure resources when on the go.
    - Recommendations
      - Download the Azure mobile app and stay connected to Azure resources—anytime, anywhere.

### Governance
36. How do you monitor usage and spending?
    - Risks
      - Inability to provide a view to people with different responsibilities (financial controller, executives, project owners) in your organization.
    - Recommendations
      - Use Cost Management metrics with dashboards to view key cost metrics and business-trend highlights to help make important business decisions.
37. How do manage costs and improve efficiency?
    - Risks
      - Risk of usage exceeding agreement thresholds, resulting in unexpected cost overages.
    - Recommendations
      - Utilize Cost Management budgeting to set up budgets and budget-based alerts to improve cloud governance and accountability.
38. How do you build custom policies to enable security and management (restrict deployment options for organization to specific datacenters or enable the creation of specific resource types only) at scale?
    - Risks
      - Risk of resources not staying compliant with corporate standards and service-level agreements (SLAs).
    - Recommendations
      - Use Custom Azure Policy to enforce different rules and effects over resources to ensure that resources stay compliant with corporate standards and SLAs.
39. How do you apply policy over resources at scale (from a single subscription to a management group with control across your entire organization)?
    - Risks
      - Inability to provide RBAC assignments over multiple subscriptions.
    - Recommendations
      - Employ Azure Policy scoping to apply governance conditions to multiple subscriptions (management groups) all at once.
40. How do audit policy compliance against best practices?
    - Risks
      - Risk of resources getting created in wrong location, enforcing common and consistent tag usage, or auditing existing resources for appropriate configurations and setting.
    - Recommendations
      - Use Azure Policy compliance monitoring to understand the compliance state of environment.

### Protection
41. Do you have pay-as-you-go backup service reducing unnecessary costs?
    - Risks
      - Inability to pick and choose the data you want to protect.
    - Recommendations
      - Use Azure Backup to pay only for the storage you consume.
42. How do you automatically detect virtual machines for backup?
    - Risks
      - Inability to detect virtual machines to back up.
    - Recommendations
      - Adopt Azure Backup VMWare integration to back up VMware server to Azure.
43. How do you access control backup operations so only authorized users can perform them?
    - Risks
      - Inability to segregate duties within your team and grant only the amount of access users need to perform backups.
    - Recommendations
      - Use RBAC to manage Azure Backup recovery points.
44. Do you get notifications if any suspicious activity in backup is detected?
    - Risks
      - Risk of insecure backups and recovery if production and backup servers are compromised.
    - Recommendations
      - Utilize Azure Backup security capabilities to prevent, alert, and recover suspicious activities.
45. How do you ensure applications are available during outages with automatic recovery?
    - Risks
      - Inability to orchestrate replication, perform disaster recovery testing, and run failovers and failback.
    - Recommendations
      - Use Azure Site Recovery to deploy application-aware replication to the cloud or to a secondary site.
46. Do you minimize recovery issues by sequencing the order of multi-tier applications running on multiple virtual machines?
    - Risks
      - Possibility of manual backup and file recovery, which is cumbersome, error-prone, and not scalable.
    - Recommendations
      - Employ Azure Site Recovery Replication of multi-tier web applications to prevent loss of productivity.
47. Do you ensure compliance by testing your disaster recovery plan without impacting production workloads or end users?
    - Risks
      - Inability to test failover without impacting ongoing replication or production environment.
    - Recommendations
      - Use Azure Site Recovery test failover to validate replication and disaster recovery strategy.
48. How do you reduce costs by conducting business during outages?
    - Risks
      - Inability to automate tasks that require manual intervention and convert from multi-step recovery to a single-click recovery action.
    - Recommendations
      - Use Azure Automation integration with Azure Site Recovery to make recovery consistently accurate, repeatable, and automated.
49. How do you minimize downtime (RPO, RTO) with dependable recovery (SLA)?
    - Risks
      - Inability to define a systematic recovery process by creating small independent units that can fail over.
    - Recommendations
      - Use Azure Site Recovery Plan to model an app around its dependencies and automate recovery tasks to reduce RTO.
