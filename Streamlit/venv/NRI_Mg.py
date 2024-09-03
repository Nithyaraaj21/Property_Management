import streamlit as st
import requests

# Flask backend URL
BASE_URL = "http://127.0.0.1:5000"

# Fetch data from Flask backend
def fetch_data(endpoint):
    response = requests.get(f"{BASE_URL}/{endpoint}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch data from {endpoint}")
        return {}

# Streamlit app
def main():
    st.title("NRI Property Management App")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Property Info", "Maintenance Requests", "Financials", "Documents", "Support"])

    if selection == "Home":
        st.header("Welcome to Your Property Management App")
        st.write("Manage your property details, track maintenance requests, and view financial information.")

    elif selection == "Property Info":
        st.header("Property Information")
        properties = fetch_data("properties")
        property_name = st.selectbox("Select Property", list(properties.keys()))
        property_details = properties.get(property_name, {})
        st.write(f"**Location:** {property_details.get('location', 'N/A')}")
        st.write(f"**Type:** {property_details.get('type', 'N/A')}")
        st.write(f"**Size:** {property_details.get('size', 'N/A')}")
        st.write(f"**Status:** {property_details.get('status', 'N/A')}")

    elif selection == "Maintenance Requests":
        st.header("Maintenance Requests")
        requests = fetch_data("maintenance")
        for request in requests:
            st.write(f"**Request ID:** {request['id']}")
            st.write(f"**Status:** {request['status']}")
            st.write(f"**Description:** {request['description']}")
            st.write("---")

    elif selection == "Financials":
        st.header("Financial Information")
        financials = fetch_data("financials")
        st.write(f"**Rent Due Date:** {financials.get('rent_due', 'N/A')}")
        st.write(f"**Amount Due:** {financials.get('amount_due', 'N/A')}")
        st.write("**Payment History:**")
        for payment in financials.get('payment_history', []):
            st.write(f"**Date:** {payment['date']} - **Amount:** {payment['amount']}")

    elif selection == "Documents":
        st.header("Documents and Agreements")
        st.write("Upload and access your property documents here.")

    elif selection == "Support":
        st.header("Support")
        st.write("For assistance, please contact support at support@nrimanagement.com")

if __name__ == "__main__":
    main()
