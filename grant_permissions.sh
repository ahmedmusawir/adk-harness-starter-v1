#!/bin/bash
set -e

# --- Configuration ---
# Your existing service account's email address
SERVICE_ACCOUNT_EMAIL="stark-vertex-ai@ninth-potion-455712-g9.iam.gserviceaccount.com"
PROJECT_ID="ninth-potion-455712-g9"

echo "🛡️ Granting permissions to service account: $SERVICE_ACCOUNT_EMAIL"
echo "--------------------------------------------------"

# Grant permission to use Vertex AI
echo "1. Granting Vertex AI User role (roles/aiplatform.user)..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
  --role="roles/aiplatform.user"

# Grant permission to read from Google Cloud Storage
echo "2. Granting Storage Object Viewer role (roles/storage.objectViewer)..."
gcloud projects add-iam-policy-binding "$PROJECT_ID" \
  --member="serviceAccount:$SERVICE_ACCOUNT_EMAIL" \
  --role="roles/storage.objectViewer"

echo "--------------------------------------------------"
echo "✅ All permissions granted successfully."