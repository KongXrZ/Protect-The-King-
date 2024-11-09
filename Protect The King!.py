import streamlit as st

# Title of the app
st.title("Protect The King!")

# Input names separated by spaces
names_input = st.text_input("Enter names separated by spaces:", "")

# Process the input when names are provided
if names_input:
    names = names_input.split()
    king_name = 'KingNice'

    # Check if KingNice is in the list
    if king_name in names:
        k_index = names.index(king_name)
        witchs = []

        # Check for witches on both sides of the king
        if k_index > 0:
            witchs.append(names[k_index - 1])
        if k_index < len(names) - 1:
            witchs.append(names[k_index + 1])

        # Display the witches' names
        st.write("Witches:", " ".join(witchs))
    else:
        st.write(f"'{king_name}' not found in the list of names.")
