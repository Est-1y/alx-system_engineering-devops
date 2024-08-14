**Postmortem:** DB Connection Pool Exhaustion Incident.

**Issue summary**

**Duration:** August 9, 2024, 11:00 - 12:20 UTC (1 hour 20 minutes)

**Impact:** The primary service affected was the application’s API layer, resulting in 60% of users experiencing slow response times or timeouts when accessing the application. This led to degraded performance and a significant drop in user engagement during the outage.

**Root Cause:** The incident was caused by an unoptimized database connection pooling configuration, which led to the exhaustion of available connections under increased load.

**Timeline:**

**11:00 UTC:** The issue was detected by monitoring tools, which reported a sharp increase in response times and a spike in timeout errors.
**11:05 UTC:** Engineers received alerts and began investigating. The initial assumption was a network latency issue due to the increase in response times.
**11:15 UTC:** Focus shifted to the application servers, where CPU and memory usage were checked, but no significant issues were found.
**11:30 UTC:** Misleading debugging paths included investigating potential bottlenecks in the application code and load balancing, both ruled out after 20 minutes.
**11:50 UTC:** Escalation to the database team, who identified that the connection pool was exhausted, causing new connections to be blocked.
**12:00 UTC:** The root cause was traced to an overly restrictive connection pool size set in the application configuration, which was insufficient to handle the increased load.
**12:10 UTC:** The connection pool size was increased, and connections were gradually restored.
**12:20 UTC:** Normal service resumed, and the application’s performance returned to acceptable levels.
**Root Cause and Resolution:**

**Root Cause:** The connection pool configuration in the application was set to a limit that was too low to accommodate the number of concurrent requests during peak traffic. This caused the connection pool to be exhausted, leading to timeouts and failed requests as new connections could not be established.

**Resolution:** The issue was resolved by increasing the size of the database connection pool in the application configuration. This allowed more connections to be handled concurrently, reducing wait times and restoring normal operation. After the change, the system was closely monitored to ensure stability.

**Corrective and Preventative Measures:**

**Improvements and Fixes:**

  * Optimize Connection Pool Configuration: Review and optimize the connection pool settings based on expected traffic patterns to prevent future exhaustion.
  
  * Enhanced Load Testing: Implement more rigorous load testing scenarios that simulate peak traffic to identify potential bottlenecks in the connection pool before they reach production.
**Automated Alerts:** Set up automated alerts specifically for connection pool usage to catch similar issues before they escalate.
**TODO List:**

  - Increase Connection Pool Size: Permanently update the connection pool settings in the application configuration to match traffic expectations.
  - Implement Load Testing: Add load testing for connection pooling in the CI/CD pipeline to ensure configurations can handle peak loads.
  - Monitor Connection Pool Usage: Introduce real-time monitoring and alerting for connection pool metrics to detect and respond to exhaustion early.
  - Document Best Practices: Update internal documentation to include guidelines on setting and managing database connection pools based on application needs.
  - By implementing these measures, we aim to enhance the reliability and resilience of our application under heavy load, ensuring a smoother user experience.






