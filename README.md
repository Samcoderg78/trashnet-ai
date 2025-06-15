# ♻️ AI Waste Classifier with Vertex A

A production-ready waste classification system powered by **Google Vertex AI** and **TensorFlow**, deployed on Cloud Run.

🔗 **Live App**:  https://trashnet-app-2d6z4zt5vq-uc.a.run.app/

## 🚀 Features
- **CNN Model**: 92% accurate waste classification (plastic/paper/metal/etc.)
- **Cloud Native**: Fully deployed on GCP (Vertex AI + Cloud Run)
- **Interactive UI**: Streamlit interface with real-time predictions
- **Scalable**: Handles 100+ RPM with auto-scaling

## 🛠️ Tech Stack
| Component               | Technology Used |
|-------------------------|-----------------|
| **Machine Learning**    | TensorFlow, Keras |
| **Cloud Deployment**    | Vertex AI, Cloud Run |
| **Web Framework**       | Streamlit |
| **CI/CD**               | Cloud Build |
| **Containerization**    | Docker |

## 📦 Installation
```bash
# Local development
git clone https://github.com/your-username/trashnet-ai.git
cd trashnet-ai
pip install -r requirements.txt
streamlit run app.py
