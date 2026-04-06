import streamlit as st

def main():
    st.title("Movie Ticket Booking System")

    # Input widgets
    customer_name = st.text_input("Customer Name")
    movie_title = st.selectbox("Movie Title", ["Avangers", "Kung Fu Panda", "Frozen"])
    show_time = st.selectbox("Show Time", ["10:00 AM", "2:00 PM", "8:00 PM"])
    seat_type = st.radio("Seat Type", ["Standard", "Premium"])
    book_button = st.button("Book Ticket")

    # Handle button click
    if book_button:
        try:
            # Exception handling for empty name
            if not customer_name.strip():
                st.error("❌ Error: Customer name cannot be empty!")
            else:
                # Display success message and booking info
                st.success("✅ Ticket booked successfully!")
                st.subheader("------- Booking Information -------")
                st.write(f"**Customer Name:** {customer_name}")
                st.write(f"**Movie Title:** {movie_title}")
                st.write(f"**Show Time:** {show_time}")
                st.write(f"**Seat Type:** {seat_type}")

        except Exception as e:
            st.error(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()