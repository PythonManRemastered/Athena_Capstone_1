import streamlit as st
import time
# List of countries and species
countries = ["Zambia", "Zimbabwe", "South Africa", "Russia"]
species = ["Apple", "Oak", "Yellow Birch", "Chestnut"]
tree_weight = 0
tree_age = 0
tree_number = 0
# the following are constant variables, the data on avg diameter of each tree species not collected yet
tree_diameter = 2
tree_height = 2
basic = 0
money_spent = (tree_number * 20) + (1.05 * tree_age)
# Initialize session state variables
if "begin_clicked" not in st.session_state:
    st.session_state["begin_clicked"] = False
if "confirm_clicked" not in st.session_state:
    st.session_state["confirm_clicked"] = False
if "year_pass_clicked" not in st.session_state:
    st.session_state["year_pass_clicked"] = False
if "money_spent" not in st.session_state:
    st.session_state["money_spent"] = 0

# Functions to update state
def update_money_spent(amount):
    st.session_state.money_spent += amount

def update_tree_number(number):
    st.session_state.tree_number = number

def update_tree_age(age):
    st.session_state.tree_age = age


if st.button("Spend 100 buckaroos"):
    update_money_spent(100)

st.title("Ceramic Cup Manufacturing Company Setup")

st.subheader("What are we tackling in this cool article?")
project_intro = """
- Carbon credits are an incentive to decrease carbon emissions by allowing companies to buy 'credits' that allow for a certain amount of carbon emissions.
- Instead of completely halting all carbon emissions, this allows for maximums and quotas to be set for companies and organizations.
- Carbon sequestration is how you compensate for your carbon emissions.
- You can do this in many ways, from planting trees to adopting more sustainable manufacturing practices.
- In this segment of my project, we will help you understand the problem surrounding seemingly simple concepts like this.
"""

header = st.container()
header.write("""
<div style="position: fixed; top: 0; right: 0; background-color: #0e1117; padding: 60px;">
    <p>You've spent</p>
    <h>${}</h>
</div>
""".format(money_spent), unsafe_allow_html=True)

st.markdown(project_intro)
st.caption("Note: Remember, you can hover over any of the terms in this article to see what they mean and where they've come from")

# Start button to begin the application
if st.button("Click me to begin"):
    st.session_state["begin_clicked"] = True

# Country selection and confirmation
if st.session_state["begin_clicked"]:
    selected_country = st.selectbox("Where do you want to establish the company?", countries)
    if st.button("Click me to confirm your choice!"):
        st.session_state["confirm_clicked"] = True
        st.write(f"Perfect! Under new regulations in {selected_country}, you've been given clearance to emit up to 1000 kilograms of carbon dioxide.")
        
# Species selection and tree planting
if st.session_state["begin_clicked"] and st.session_state["confirm_clicked"]:
    selected_species = st.selectbox("Choose the species of tree you want to plant:", species)
    # real number statistics, don't change unless species change
    if selected_species == "Oak":
        tree_weight = 41
        
    elif selected_species == "Apple":
        tree_weight = 30
        
    elif selected_species == "Yellow Birch":
        tree_weight = 31
        
    else:
        tree_weight = 30
        
    
    tree_number = st.slider("Choose how many trees you want to plant", 0, 1000)

    st.write(f"You chose to plant {tree_number} {selected_species} trees. Each tree weighs approximately {tree_weight} kgs")
     
    tree_age = tree_age + 1
    carbon_sequestered_original = (((((0.25*(tree_diameter*tree_diameter)*tree_height)*1.2)*0.725)*0.5)*3.67)* tree_number
    st.write(f"Carbon sequestered in the first year: {carbon_sequestered_original} kgs")
    if carbon_sequestered_original>1000:
        st.subheader(f"Great! You've completely sequestered your carbon emissions with {tree_number} trees.")
    else:
        st.write(f"Not yet! We still need to sequester {1000 - int(carbon_sequestered_original)} kgs more!")
    
  # Simulate time passing  
    if st.button("Pass a Year"):
        st.session_state["year_pass_clicked"] = True
        progress_text = "Simulating one entire year passing..."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty() 
        if carbon_sequestered_original < 1000:
            st.warning("Hey! You still haven't planted enough trees! Go back!")
        else:
            st.balloons()
            st.write(f"Now that {tree_age} year(s) have passed, is there any difference in the amount of carbon sequestered?")     
            st.write(f"Last year, you chose to plant {tree_number} {selected_species} trees.")
            tree_age += 1
            carbon_sequestered_original += (tree_age*tree_number*20)/100
            
            st.write(f"Carbon sequestered in the second year: {carbon_sequestered_original} kgs")
        
            st.write("Notice how the number didn't just double over the last year?")
            expander = st.expander("Click me to see why")
            expander.write("""
                        As a tree grows up, it grows more wood to store carbon in. Hence, the amount of carbon a tree can sequester per year actually increases as if grows up.\n 
                        In the first year the trees sequestered 2000kgs\n
                        In the second year, as the trees increased in size, they were able to sequester 4000kgs!
            """)
if st.session_state["begin_clicked"] and st.session_state["confirm_clicked"] and st.session_state["year_pass_clicked"] and carbon_sequestered_original>1000:
    st.error(f"""
             Suddenly, the government of {selected_country} decides that the land you're using to plant these trees have oil under them. They send you a message to tell 
             them how many trees they will have to cut down to clear the area so that they can figure out how much labour they'd need
             """)
    tree_number_lost = st.slider("Choose how many trees the government must cut down", 0, tree_number)
    carbon_after_deforestration = (((((0.25*(tree_diameter*tree_diameter)*tree_height)*1.2)*0.725)*0.5)*3.67)* (tree_number-tree_number_lost)
    carbon_lost = carbon_sequestered_original-carbon_after_deforestration
    if st.button("Click me to confirm your choice"):
        st.write(f"We lost {tree_number_lost} trees")
        st.write(f"Because of this, about {carbon_lost} kgs of the carbon we sequestered is now back into the atmosphere")
