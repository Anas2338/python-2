import streamlit as st
import re

Common_Passwords = [
    "password", "123456", "12345678", "1234", "qwerty", "12345", 
    "itinitiative", "governersindh", "football", "letmein", "poiuytrewq123", "abc123", 
    "mustang", "karachi", "shadow", "master", "pakistan", "111111", 
    "2000", "jordan", "superman", "panaversity", "1234567", "admin123", 
    "trustno1", "sunshine", "123123", "welcome", "admin", "password1"
]

def password_strength (Password):

    word = 0
    feedback = []

    if len(Password) >=8:
        word += 1
    else:
        feedback.append("❌ Password is too short. Use at least 8 characters.")

    if re.search(r"[a-z]" , Password) and re.search(r"[A-Z]" , Password):
        word += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", Password):
        word += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", Password):
        word += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if word >= 4:
        strength = "strong"
    elif word >= 3:
        strength = "moderate"
    else:
        strength = "weak"

    return strength, feedback


def main():

    st.title("Password Strength Meter")
    st.write("Enter your password below to check its strength.")
    
    Password  = st.text_input("Password", type="password")

    if st.button("Proceed"):
        if not Password:
            st.error("❌ Password field cannot be empty. Please enter a password.")
        else:
            if Password in Common_Passwords:
                st.error("❌ This password is too common. Please choose a more unique password.")
            else:
                strength , feedback = password_strength(Password)
    
                if strength == "strong":
                    st.success(f"Password strength : {strength}")
                elif strength == "moderate":
                    st.warning(f"Password strength : {strength}")
                else:
                    st.error(f"Password strength : {strength}")
        
                if strength in ["weak", "moderate"]:
                    st.write("Feedback to improve your password:")
                    for suggestion in feedback:
                        st.write(f"- {suggestion}")

main()