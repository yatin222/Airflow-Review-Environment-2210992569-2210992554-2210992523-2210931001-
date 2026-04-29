# Airflow Review App Project

## Project Overview

This project implements an **Apache Airflow Review Application** deployed on **AWS EKS (Elastic Kubernetes Service)** using **Helm Charts** and **GitLab CI/CD**. It provides an ephemeral, on-demand Airflow environment for reviewing and testing DAGs (Directed Acyclic Graphs) before merging changes into production.

## Key Features

- **EKS Cluster Provisioning** — Automated Kubernetes cluster setup using `eksctl` on AWS (eu-north-1 region) with managed node groups and auto-scaling.
- **Helm-based Deployment** — Custom Helm chart (`airflow-review-app-chart`) to deploy the Airflow webserver, scheduler, and an embedded PostgreSQL database.
- **KubernetesExecutor** — Uses Airflow's KubernetesExecutor for dynamic, isolated task execution.
- **Ephemeral Review Environments** — PostgreSQL runs without persistence, making each review app lightweight and disposable.
- **GitLab CI/CD Integration** — DAGs are cloned from a GitLab repository via SSH, enabling branch-based review workflows.
- **ECR Image Registry** — Custom Airflow Docker image (based on `apache/airflow:2.8.1-python3.10`) stored in AWS ECR.
- **IRSA (IAM Roles for Service Accounts)** — Secure, fine-grained AWS permissions for pulling images from ECR.

## Project Structure

```
airflow-review-project/
├── airflow-dags-repo/
│   ├── Dockerfile                  # Custom Airflow Docker image
│   └── dags/
│       └── hello_world_review_dag.py   # Sample review DAG
├── airflow-helm-chart/
│   └── airflow-review-app-chart/
│       ├── Chart.yaml              # Helm chart metadata & dependencies
│       ├── values.yaml             # Configuration values (image, DB, service account)
│       └── templates/
│           ├── scheduler-deployment.yml
│           ├── webserver-deployment.yaml
│           ├── service.yaml
│           ├── serviceaccount.yaml
│           ├── hpa.yaml
│           └── _helpers.tpl
├── cluster.yaml                    # EKS cluster configuration (eksctl)
├── gitlab-ci-review-key            # GitLab CI SSH private key
├── gitlab-ci-review-key.pub        # GitLab CI SSH public key
└── gitlab-key.pem                  # SSH key for EKS node access
```

## Tech Stack

| Technology         | Purpose                              |
|--------------------|--------------------------------------|
| Apache Airflow 2.8 | Workflow orchestration                |
| AWS EKS (K8s 1.29) | Container orchestration platform     |
| Helm               | Kubernetes package management        |
| PostgreSQL         | Airflow metadata database            |
| Docker             | Containerization                     |
| AWS ECR            | Container image registry             |
| GitLab CI/CD       | Continuous integration & deployment  |
| eksctl             | EKS cluster provisioning             |

---

## Team Members

### 1. Yatin

| Field          | Details                                                                                      |
|----------------|----------------------------------------------------------------------------------------------|
| **Emp Code / Roll No.** | 2210992569                                                                          |
| **Address**    | House No. 2737/5, New Tagore Nagar, Haibowal Kalan, Ludhiana, Punjab                        |
| **Email**      | yatin2569.be22@chitkara.edu.in                                                               |
| **Mobile No.** | 8054912860                                                                                   |

### 2. Yash Goyal

| Field          | Details                                                                                      |
|----------------|----------------------------------------------------------------------------------------------|
| **Emp Code / Roll No.** | 2210992554                                                                          |
| **Address**    | 341/7, Near Hind Cinema, Opposite Arya Samaj School, Kaithal, Haryana                        |
| **Email**      | yash2554.be22@chitkara.edu.in                                                                |
| **Mobile No.** | 7015731882                                                                                   |

### 3. Vidhan Gupta

| Field          | Details                                                                                      |
|----------------|----------------------------------------------------------------------------------------------|
| **Emp Code / Roll No.** | 2210992523                                                                          |
| **Address**    | House No. 241 GP, Block A, Sector 21, Kaithal, Haryana                                      |
| **Email**      | vidhan2523.be22@chitkara.edu.in                                                              |
| **Mobile No.** | 9996310789                                                                                   |

### 4. Anmol Singla

| Field          | Details                                                                                      |
|----------------|----------------------------------------------------------------------------------------------|
| **Emp Code / Roll No.** | 2210931001                                                                          |
| **Address**    | Singla Tutorials, Nishat Bagh Colony, Near Post Office, Bhattia Bhattian Bet, Ludhiana, Punjab |
| **Email**      | anmol1001.be22@chitkara.edu.in                                                               |
| **Mobile No.** | 9478019600                                                                                   |

---

## Getting Started

### Prerequisites

- AWS CLI configured with appropriate credentials
- `eksctl` installed for cluster provisioning
- `kubectl` configured for Kubernetes access
- `helm` (v3+) installed for chart deployment
- Docker for building the Airflow image

### Steps

1. **Provision the EKS Cluster**
   ```bash
   eksctl create cluster -f airflow-review-project/cluster.yaml
   ```

2. **Build & Push the Airflow Docker Image**
   ```bash
   docker build -t airflow-base-image airflow-review-project/airflow-dags-repo/
   docker tag airflow-base-image:latest <ECR_URI>:latest
   docker push <ECR_URI>:latest
   ```

3. **Deploy with Helm**
   ```bash
   helm install airflow-review airflow-review-project/airflow-helm-chart/airflow-review-app-chart/
   ```

4. **Access the Airflow Webserver**
   ```bash
   kubectl port-forward svc/airflow-webserver 8080:8080
   ```
   Open `http://localhost:8080` and log in with `admin / admin`.
