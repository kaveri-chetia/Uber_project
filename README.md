## Problem statement
Considering the everyday increase in popularity  of uber and to enhance transparency, improves user experience, to make better decision-making for both users and the company,  it got crucial to build  app to optimize its pricing strategy.

## Project overview
The goal of this project is to develop a machine learning model that can accurately predict the fare of an Uber ride given specific input features such as the pickup and dropoff locations, time of day, and other relevant factors. 

![map](https://github.com/user-attachments/assets/0cdf8fd9-31a8-430f-aa63-70ffe8214da5)



## [Data source](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)

The details of the dataset can be found in the metadata.


## Metadata

key - A unique identifier for each trip<br>
fare_amount - The cost of each trip in usd<br>
pickup_datetime - Date and time when the meter was engaged<br>
passenger_count - The number of passengers in the vehicle (driver entered value)<br>
pickup_longitude - The longitude where the meter was engaged<br>
pickup_latitude - The latitude where the meter was engaged<br>
dropoff_longitude - The longitude where the meter was disengaged<br>
dropoff_latitude - The latitude where the meter was disengaged<br>

## Exploratory data analysis(EDA)

![output1](https://github.com/user-attachments/assets/f010412f-95ab-4e5e-821b-2ddfaaa752cc)

### Correlation

![FE2](https://github.com/user-attachments/assets/41daf76c-127c-4f15-81da-1b92c92d5423)


## Roadmap

![updated drawio](https://github.com/user-attachments/assets/6fb9cc14-89f9-4d84-8e7f-a292f7ea0dfe)


## Machine learning Models
<img width="4000" alt="Screenshot 2024-08-22 at 21 38 14" src="https://github.com/user-attachments/assets/3e4ca24e-e174-4c66-846d-922dcea9ab1f">



## Key findings and Insights

The Gradient boosting regressor model and the random forest regressor model both worked well, however, GB has better result, I selected Gradient boosting regressor model. 

<img width="4000" alt="Screenshot 2024-08-22 at 21 39 09" src="https://github.com/user-attachments/assets/80a4e224-3dcf-4003-9fbe-35f86870dc38">


## Conclusion

In conclusion, the Uber Fare Prediction project successfully demonstrates the application of machine learning to predict ride costs based on various factors such as distance, time, and location. By developing this model, we enhance transparency for users, allowing them to anticipate fare costs more accurately, which improves their overall experience. Additionally, the model provides valuable insights for Uber, enabling the company to manage demand more efficiently and optimize pricing strategies. This project lays the groundwork for future enhancements, such as integrating real-time data, expanding to other ride-sharing platforms, and developing personalized fare prediction models. Overall, the project not only benefits users by offering cost predictability but also supports Uber in maintaining a competitive edge in the dynamic ride-sharing market.

[Presentation](https://docs.google.com/presentation/d/1NBEXrlc_n9n70xWjFFB5tVtXd13ixMxz7pUKtuStOf4/edit#slide=id.g2f42c13bfb0_0_281)<br>
[stramlit](http://localhost:8501/)
