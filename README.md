# Weather-tracking
Weather tracking application in Python using OpenWeatherMap API

Presented application was based on free API (authentication is required) - 1,000 API calls per day for free:
https://openweathermap.org/api

### Additional information
1) **TODO**: GUI will be added in two variants: desktop App (flet) and Web App (streamlit)

## Installation & preconfiguration
For authentication purpose please follow below instruction (need to be done before start follow execute section)
1) Sign up using below link: https://openweathermap.org/api
2) Confirm your email using invitation email
![img.png](images/img.png)
3) Select below version:
![img_2.png](images/img_2.png)
4) Than select below option:
![img_3.png](images/img_3.png)
5) Copy your own key (it should be provided you by new email)

## Execute instruction
1) Create **API_key.json** file in project folder (hided file in repository, need to be created on local machine) 
2) Paste below json object:
{
  "key" : "YOUR_OWN_API_KEY"
}
3) Instead of ,,**YOUR_OWN_API_KEY**" string located under **key** item paste your generated key
4) Run main.py script without any argument. As result, you receive description of current weather, temperature and humidity for London city.
5) **TODO**: CLI extended functionality will be implemented soon
