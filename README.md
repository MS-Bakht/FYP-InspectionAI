# InspectAI

## Overview
InspectAI is a groundbreaking solution designed to transform the traditional PCB (Printed Circuit Board) inspection process through the integration of advanced artificial intelligence and augmented reality technologies. By leveraging a pair of AR-enabled glasses, such as Google Spectacles, workers can inspect PCBs with enhanced precision and efficiency. The InspectAI model processes the live video feed captured by the glasses, promptly identifying any defects and visually highlighting them on both the glasses' AR display and an external screen. Additionally, our system is capable of generating a detailed 3D model of the PCB from the video feed, offering an in-depth analysis tool for quality assurance and inspection teams.

![image](https://github.com/MS-Bakht/FYP-InspectionAI/assets/70213048/8139b2f8-4774-478d-9eff-08c3b358a005)



## Dataset
Our current dataset is a robust collection that consists of 10,668 images, each meticulously annotated to assist in training our AI model. This extensive dataset ensures high accuracy and reliability in defect detection, providing a strong foundation for the effectiveness of InspectAI.

### Dataset Details
- **Total Images**: 10,668
- **Annotations**: Each image in the dataset is paired with detailed annotations outlining the presence, type, and location of defects on the PCBs.
- **Source**: The images and annotations have been compiled from a variety of PCB inspection scenarios to ensure diversity and comprehensiveness in our model's training data.

## Key Features
- **Real-Time Defect Detection**: Immediate identification and highlighting of PCB defects during inspections.
- **Augmented Reality Support**: Defects are visually marked on the AR display of the glasses, offering a seamless inspection workflow.
- **3D Model Reconstruction**: Generates 3D representations of PCBs from the video feed, enabling a more thorough analysis.
- **Comprehensive Dataset**: Built on a foundation of over 10,000 annotated images, ensuring high model accuracy and reliability.

## Technologies Used
- Python
- Docker
- Google Spectacles
- Augmented Reality (AR) Technologies
- Advanced AI and Computer Vision Algorithms
- OpenCv
- Deep learning
- Github

## Getting Started
### Docker Image
The Docker image for InspectAI is available on Docker Hub. It can be found at:  mshayanb7/fyp_inspection_ai
