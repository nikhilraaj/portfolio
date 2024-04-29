import streamlit as st

def main():
    st.title("My Portfolio Website")
    st.write("Welcome to my portfolio! Here you can find information about me and my work.")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

    if page == "Home":
        show_home_page()
    elif page == "About":
        show_about_page()
    elif page == "Projects":
        show_projects_page()
    elif page == "Contact":
        show_contact_page()

def show_home_page():
    st.header("Home")
    st.write("This is the home page. Here you can find some general information about me.")

def show_about_page():
    st.header("About Me")
    st.write("I am a passionate software developer with experience in various technologies.")

    st.subheader("Skills")
    st.write("- Python\n- JavaScript\n- HTML/CSS\n- Streamlit\n- Flask")

def show_projects_page():
    st.header("Projects")
    st.write("Here are some of my projects:")

    project1 = {
        "title": "Project 1",
        "description": "This is a dummy project description.",
        "image": "https://via.placeholder.com/150",
        "link": "https://example.com/project1"
    }

    project2 = {
        "title": "Project 2",
        "description": "This is another dummy project description.",
        "image": "https://via.placeholder.com/150",
        "link": "https://example.com/project2"
    }

    projects = [project1, project2]

    for project in projects:
        st.subheader(project['title'])
        st.image(project['image'], use_column_width=True)
        st.write(project['description'])
        st.write(f"[Link]({project['link']})")

def show_contact_page():
    st.header("Contact Me")
    st.write("You can reach out to me via email at example@example.com")

if __name__ == "__main__":
    main()
