## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

##sample button action
* send_sample_buttons
    - action_send_buttons

##sample image action
* send_sample_image
    - action_send_image

##sample carousel action
* send_sample_carousel
    - action_send_carousel

##sample text action
* send_sample_text
    - action_send_text
