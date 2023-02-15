## Spark Jobs with Argo Workflows

### Infrastructure
- Install Spark Operator from [spark-on-k8s-operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator)

- Apply rbac, Spark resources as ClusterRole to argo-workflow ServiceAccount

- create and apply secrets and configmaps

### Spark Job
1. Download Data Job 
 - Build and push Dockerfile.download-job
 - Add download-job workflow to bike-workflow.yaml

2. Bike Type Job
 - Build and push Dockerfile.bikesTypeJob
 - Add bike-type workflow to bike-workflow.yaml
