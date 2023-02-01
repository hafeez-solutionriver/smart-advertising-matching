# Smart-Advertising-Matching

##  Methodology
In this section we will cover the complete methodology applying agile methodology so that we can accept the changes at any phase. We use supervised learning (classification) to create a model for our dataset and finally we deploy this model on web using flask (Python framework). We use multiple classification algorithms which will perform better to get our desired outcomes.

##  Flow of the project
- We train our model for gender and age classification on UTKFace dataset of 20k images.
- We make an algorithm for generating advertisement based on gender and age groups.                                                                                                                                                            

## Flow of the system:
- We access the webcam using OpenCV (python library). 
- On the other side, we will have the screen for displaying the advertisements. 
- When webcam opens our model detect the age and gender of the person on real time.
- Our back-end algorithm decide the category of that person according to age and gender and advertisement related to that category will be played on screen. 

## Dataset discussion
As we reviewed several datasets consisting of images tagged by gender, age, and ethnicity/race, and developed the UTKFace dataset as it met the needs of the project.
The UTKFace dataset is a large face dataset with a long age range (range 0 to 116 years old). The data set consists of over 20,000 facial images annotated by age, gender, and ethnicity. Images cover a wide variety of poses, facial expressions, lighting, occlusion, resolution, and more.

Labels:
- Age: is an integer from 0 to 116, indicating the age
- Gender: is either 0 (male) or 1 (female)
- Race: is an integer from 0 to 4, denoting White, Black, Asian, Indian, and others (like Hispanic, Latino, Middle Eastern).
- Date time: is in the format of yyyymmddHHMMSSFFF, showing the date and time an image was collected to UTKFace.

Every image is labelled by age, gender and ethnicity but we are working only upon gender and age because our advertisement selection depends upon these two features.

## Major Outcomes
- Our project addresses intelligent advertising based on people's gender and age, also facilitating product sales optimization.
- Our project overcomes the problem of random advertisements on billboards and LEDs, finally providing a better advertising experience for both advertisers and viewers.
- Our project detects the age and gender and according to that in which class people belong then the advertisement belong to that class will run and show on screen.


# Step for Executing
- Execute the app.py file only.
# Screenshots
![image](https://user-images.githubusercontent.com/111304445/216068304-09e223b2-8899-4c07-8053-5b3f97b41974.png)

