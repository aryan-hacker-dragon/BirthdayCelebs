import streamlit as st
import os
import random

def get_random_birthday_image():
    birthday_image_folder = "Friends"
    images = [img for img in os.listdir(birthday_image_folder) if img.endswith(".jpg")]
    random_image = random.choice(images)
    return os.path.join(Friends, random_image)

def birthday_wish_app():
    st.title("🎉 Birthday Wishes 🎂")

    random_image_path = get_random_birthday_image()
    st.image(random_image_path, caption="Happy Birthday!", use_column_width=True)

    st.markdown("### 🎈 Happy Birthday, Sahatraksh! 🎁")
    
    st.write("Wishing you a day filled with joy, laughter, and lots of love.")
    
    st.markdown("### 🎂 Let's Celebrate! 🥳")
    
    st.write("""On this special day, I wish you a year filled with joy, growth, and incredible moments. May every day bring new opportunities, and may you find success and satisfaction in all your endeavors.

Sahas, your presence lights up the lives of those around you. Your kindness, determination, and enthusiasm are truly inspiring. May the coming year be a chapter of endless possibilities, where your dreams unfold and your goals are realized.

As you blow out the candles, remember that you have a community of friends and loved ones cheering you on. Cherish the moments, embrace the challenges, and celebrate the victories.

Here's to another year of laughter, love, and unforgettable memories. May your birthday be as fantastic as you are! 🥳🎁

Cheers to you, Sahas! 🌟""")

    # # Text input for user's birthday message
    # birthday_message = st.text_area("Your Birthday Message:", max_chars=280)

    # if st.button("Send Birthday Wishes"):
    #     if birthday_message:
    #         st.success(f"Your birthday wishes have been sent! 🎉\n\nMessage: {birthday_message}")
    #     else:
    #         st.warning("Please enter a birthday message before sending.")

if __name__ == "__main__":
    birthday_wish_app()
