# MedicAI
Code for _**"[Improving Clinical Efficiency and Reducing Medical Errors through NLP-enabled diagnosis of Health Conditions from Transcription Reports](https://arxiv.org/abs/2206.13516)"**_ <br>

## Awards/Resources
**Top 3 @ STEMist education hacks** <br>
<!-- **Pending Publication in a 6.14 IF International Journal** -->

**More Information:** <br>
[Research paper](https://arxiv.org/pdf/2206.13516.pdf)<br>
[YouTube Demo](https://www.youtube.com/watch?v=_GsxYAZyjnU&feature=emb_title&ab_channel=KabirRamzan)

## Project Objective
In an effort to streamline the process for medical practitioners and improve clinical care for patients within the hospital, we developed various machine learning and deep learning-based architectures to classify healthcare conditions in a transcription note, ultimately reducing misdiagnosis rates and alleviating the burden for overloaded hospitals. Furthermore, to increase the accessibility for hospitals worldwide, our models are packaged into an efficient and accurate AI-enabled medical app.

## Web App Details
![dash](https://user-images.githubusercontent.com/56781484/175841396-a56fd8ae-2483-449b-9a13-bca024b61a7b.png) <br>
In terms of the web technologies we used, our front-end was built with HTML, CSS, and JavaScript, and the back-end infrastructure was developed with Flask and Firebase. We implemented authentication procedures with secure login/logout functionality using Firebase and developed the database using Firebase Cloud Firestore. We believe our application is crucial for assisting clinicians in health condition diagnoses, and it has the potential to level the playing field between hospitals in different areas.
![Screen Shot 2022-06-26 at 5 56 31 PM](https://user-images.githubusercontent.com/56781484/175841744-cc1922ea-7824-48d0-b54e-e0c34ebb64b5.png)  <br>

## Model Improvements
Through hyperparameter tuning, we have improved the performance of our models as follows:

- **Random Forest:**
  - **Old Accuracy:** 84%
  - **New Accuracy:** 86%
  - **Old Classification Report:**
    ```
                  precision    recall  f1-score   support

           Heart       0.81      0.91      0.85        64
           Brain       0.89      0.92      0.91        61
    Reproductive       0.86      0.77      0.79        74
       Digestive       0.82      0.75      0.79        62

    ```

  - **New Classification Report:**
    ```
                  precision    recall  f1-score   support

           Heart       0.92      0.88      0.90        64
           Brain       0.83      0.79      0.81        61
    Reproductive       0.83      0.93      0.88        74
       Digestive       0.86      0.82      0.84        62

       
    ```

- **Logistic Regression:**
  - **Old Accuracy:** 91.19%
  - **New Accuracy:** 93%
  - **Old Classification Report:**
    ```
                  precision    recall  f1-score   support

           Heart       0.92      0.95      0.93        64
           Brain       0.94      0.94      0.94        61
    Reproductive       0.90      0.89      0.89        74
       Digestive       0.88      0.87      0.88        62
    ```

  - **New Classification Report:**
    ```
                  precision    recall  f1-score   support

           Heart       0.94      0.94      0.94        64
           Brain       0.89      0.89      0.89        61
    Reproductive       0.94      0.97      0.95        74
       Digestive       0.95      0.90      0.93        62
    ```

These improvements enhance the reliability of our diagnostic tool and its applicability in real-world scenarios.

## Dependencies
You may need to use `pip install` to install the dependencies on each line of `requirements.txt` (for example, `pip install flask==1.1.2`). This list is not comprehensive and does not include many of the modules, which will need to be installed as errors arise with running (see below section).

You will also need to install Tesseract; more details can be found online or at the [Tesseract User Manual](https://github.com/tesseract-ocr/tessdoc).

## Running
To run the code, open a terminal and navigate to the root directory of this repository. Then, run the following commands:
```bash
export FLASK_APP=app.py
flask run -h localhost -p 5001
