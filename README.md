<p align="center">
    <image src="images/cover.png"  width="1280" height="auto">
</p>

# Phishing URL Detection

The objective of the project is to analyse a web url and identify it as a legitimate or a phishing url.

At its core, this is a 2-class classification problem. The project uses data mining and machine learning techniques to address the problem of flagging a given url as phishing or legitimate.


## Data:
- Source: [Mendeley Data](https://data.mendeley.com/datasets/72ptz43s9v/1)
- A CSV file that contains **88647** datapoints consisting of both legitimate and malicious websites.
- Each url is represented using **111** features based on which a url is labeled as phishing url or not.
- The dataset is fairly unbalanced with the number of legitimate urls roughly double the number of malicious urls.

## Problem Statement:
Phishing is a type of social engineering attack often used to steal user data, including login credentials and credit card numbers. It occurs when an attacker, masquerading as a trusted entity, dupes a victim into opening an email, instant message, or text message.
These attacks are becoming very common as more and more people start using online banking and the internet becomes ubiquitous.
    
## Potential Methods:
A strategy is used to implement data mining algorithms to identify phishing websites by tracking the URL, in an attempt to limit phishing attacks. Attacks happen when attackers modify the filepath and subdomain or introduce an error to resemble the original website. To identify such websites, one needs to go through the URL and identify each of the elements in it. The strategies for this to work can be Logistic regression, Naive Bayes Classifier, KNN and XGB Boost.
    
## Measurement of Success
 The project's purpose is to find the most accurate data mining algorithm in order to identify a fraudulent website that takes personal information from consumers.

## Team Members:
1. Anujot Singh
2. Ashutosh Ojha
3. Ilisha Aggarwal
4. Subhadra Rangaswamy
