Create Google Service Account (GSA):
gcloud iam service-accounts create gke-cloudsql-sa \
  --project <project-id>


Grant required role:
gcloud projects add-iam-policy-binding ayush-1008 \
  --member="serviceAccount:gke-cloudsql-sa@<project-id>.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"

Create Kubernetes Service Account (KSA):
"kubectl create serviceaccount gke-cloudsql-sa"

Bind KSA → GSA (CRITICAL STEP):
gcloud iam service-accounts add-iam-policy-binding \
  gke-cloudsql-sa@<project-id>.iam.gserviceaccount.com \
  --role="roles/iam.workloadIdentityUser" \
  --member="serviceAccount:<project-id>.svc.id.goog[default/<kubernetes-sa-name>]"

Add annotatw:
kubectl annotate serviceaccount gke-cloudsql-sa \
  iam.gke.io/gcp-service-account=gke-cloudsql-sa@ayush-1008.iam.gserviceaccount.com

Update your Deployment YAML: 
spec:
  serviceAccountName: gke-cloudsql-sa #upadte the gke-sa name here
  containers:
  - name: app
    image: your-image


  

