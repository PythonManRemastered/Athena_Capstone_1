import streamlit as st
import time

# List of countries and species
countries = ["Zambia", "Zimbabwe", "South Africa", "Russia"]
species = ["Red Maple", "Silver Maple", "Sugar Maple", "River Birch", "White Birch", "Shagbark Hickory", "Green Ash", "Black Walnut", "Black Cherry", "White Oak", "Red Oak", "Pin Oak", "Linden or Basswood", "American Elm", "Ironwood", "Cottonwood", "Dogwood", "Redbud"]
tree_height = 1
tree_diameter = 1
tree_age = 1
cup_amount = 0 
# height and diameter is in unit measurement

# Initialize session state variables
if "begin_clicked" not in st.session_state:
    st.session_state["begin_clicked"] = False
if "confirm_clicked" not in st.session_state:
    st.session_state["confirm_clicked"] = False
if "year_pass_clicked" not in st.session_state:
    st.session_state["year_pass_clicked"] = False
if "chapter_two_advance" not in st.session_state:
    st.session_state["chapter_two_advance"] = False
if "tree_cut_confirm" not in st.session_state:
    st.session_state["tree_cut_confirm"] = False
if "money_spent" not in st.session_state:
    st.session_state["money_spent"] = 0
if "money_made" not in st.session_state:
    st.session_state["money_made"] = 0
if "tree_number" not in st.session_state:
    st.session_state["tree_number"] = 0
if "carbon_offset_cost_confirm" not in st.session_state:
    st.session_state["carbon_offset_cost_confirm"] = False 

# Functions to update state
def update_money_spent(amount):
    st.session_state.money_spent += amount

def update_tree_number(number):
    st.session_state.tree_number = number

def update_cup_number(number):
    st.session_state.cup_amount = number

# Main app UI

st.header("What are we tackling in this cool article?")
project_intro = """
- Carbon credits are an incentive to decrease carbon emissions by allowing companies to buy 'credits' that allow for a certain amount of carbon emissions.
- Instead of completely halting all carbon emissions, this allows for maximums and quotas to be set for companies and organizations.
- Carbon sequestration is how you compensate for your carbon emissions.
- You can do this in many ways, from planting trees to adopting more sustainable manufacturing practices.
- In this segment of my project, we will help you understand the problem surrounding seemingly simple concepts like this.
"""
company_intro = """
- You've been tasked with heading a medium-scale ceramic cup manufacturing facility's daily operations
- You have been under a huge increase in popularity due to modern trends, and the cups that you make sell out almost immediately after they are listed!
- You are looking through your paperwork and realise that you have exceeded the amount of carbon that you are allowed to emit
- Everyday, you can only make a set number of cups, each of which need time to be fired and transported to sales
- According to the manufacturing documents, you emitted approximately 2 kilograms of CO2 per cup, and about 8 kilograms of CO2 through the entire product development life cycle
"""
first_year_prices_constant = 365
# apple trees are placeholders
first_year_prices = """
    Cost breakdown for year 1
- Cost of each tree: $25
- Spray materials for several years: $45
- Labor for planting (one hour): $20        
- Sprayer: $25
- Labor for training in summer:$20
- Tripod ladder, 10-foot: $130
- Pruning lopper: $45
- Pruning handsaw: $30
- Pruning hand shears: $25
- Total cost for the first year: $365
"""

country_overviews_dictionary = {
    "South Africa": "The South African Provincial area is known for heavy acts of deforestation. Though this makes our job a lot harder, we can still try!",
    "Zimbabwe": "Zimbabwe is a great place to start. According to the 17th Green Tax Amendment of Harare, deforestration is illegal in nearly all cases! This makes our job a lot easier",
    "Zambia": "Zambia was one of the top regions responsible for 58% of all tree cover loss between 2001 and 2023. Though this might mean forestration policies there may be harder to implement, the country needs more tree cover. Perfect: Let's begin!",
    "Russia": "Due to the current conflict in the Russian peninsula, co-ordinating forestation politically may prove to be a problem. Doesn't matter: Let's try!"

}


# Display header with updated money spent
def display_header_spent():
    st.markdown(f"""
    <div style="position: fixed; top: 0; right: 0; background-color: #0e1117; padding: 60px;">
        <p>You've spent</p>
        <h>${st.session_state.money_spent}</h>
    </div>
    """, unsafe_allow_html=True)

display_header_spent()



def reset_everything():
    restarter_text = "Restarting article..."
    my_bar = st.progress(0, text=restarter_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=restarter_text)
    time.sleep(1)
    my_bar.empty()
    st.session_state["begin_clicked"] = False
    st.session_state["confirm_clicked"] = False
    st.session_state["year_pass_clicked"] = False
    tree_height = 1
    tree_diameter = 1
    update_money_spent(0)
if st.button("Click me if you want to start over"):
    reset_everything()
    

if st.button("Spend 100 buckaroos"):
    update_money_spent(100)

st.markdown(project_intro)
st.caption("Note: Remember, you can hover over any of the terms in this article to see what they mean and where they've come from")




# THIS IS THE BEGINNING OF THE CODE LOGIC #####################################################






# Start button to begin the application
if st.button("Click me to begin"):
    st.session_state["begin_clicked"] = True


# Country selection and confirmation
if st.session_state["begin_clicked"]:
    st.title("Ceramic Cup Manufacturing Company Setup")
    st.markdown(company_intro)
    global cups_amount 
    cups_amount = st.slider("Choose how many cups you want to make each day:", 0, 5000)
    st.markdown(f"Great! We have made {cups_amount} cups")
    global cups_price 
    cups_price = st.slider("Choose what these cups are priced at to the public: ", 0, 100)
    st.markdown(f"Cool! Since our product is {cups_price} dollars per cup, we've made about {cups_price*cups_amount} dollars")
    global money_made
    money_made = cups_amount*cups_price
    global carbon_emitted 
    carbon_emitted = cups_amount*8
    st.markdown(f"Unfortunately, this also means we have emitted about {8*cups_amount}kg of carbon! So, we now have to sequester this to become a green company")
    
    selected_country = st.selectbox("Where do you want to establish the company?", countries)
    if st.button("Click me to confirm your choice!"):
        st.session_state["confirm_clicked"] = True
        st.write(f"Perfect! Under new regulations in {selected_country}, you've been given clearance to emit up to 1000 kilograms of carbon dioxide.")
        country_overviews = country_overviews_dictionary.get(selected_country, 10)
        st.write(country_overviews)



# Species selection and tree planting
if st.session_state["begin_clicked"] and st.session_state["confirm_clicked"]:
    selected_species = st.selectbox("Choose the species of tree you want to plant:", species)
    
    tree_weights = {
        "Red Maple": (tree_age * 0.75)/4.5,
        "Silver Maple": (tree_age * 0.75)/3.0,
        "Sugar Maple": (tree_age * 0.75)/5.0,
        "River Birch": (tree_age * 0.75)/3.5,
        "White Birch": (tree_age * 0.75)/5.0,
        "Shagbark Hickory": (tree_age * 0.75)/7.5,
        "Green Ash": (tree_age * 0.75)/4.0,
        "Black Walnut": (tree_age * 0.75)/4.5,
        "Black Cherry": (tree_age * 0.75)/5.0,
        "White Oak": (tree_age * 0.75)/5.0,
        "Red Oak": (tree_age * 0.75)/4.0,
        "Pin Oak": (tree_age * 0.75)/3.0,
        "Linden or Basswood": (tree_age * 0.75)/3.0,
        "American Elm": (tree_age * 0.75)/4.0,
        "Ironwood": (tree_age * 0.75)/7.0,
        "Cottonwood": (tree_age * 0.75)/2.0,
        "Dogwood": (tree_age * 0.75)/7.0,
        "Redbud": (tree_age * 0.75)/7.0           
    }
    # .get prevents key issues, 30 is the default value for non-recognizable species
    tree_diameter = tree_weights.get(selected_species, 30)
    
    tree_number = st.slider("Choose how many trees you want to plant", 0, 2000000)
    update_tree_number(tree_number)

    
    st.write(f"Since you chose {selected_species}, each tree has a diameter, at breast height, of approximately {tree_diameter}")
    st.write(f"You chose to plant {tree_number} {selected_species} trees.")
    
    carbon_sequestered_original = ((((((0.25*((tree_diameter)*(tree_diameter))*tree_height)*1.2)*0.725)*0.5)*3.67)* st.session_state.tree_number)/tree_age
    st.write(f"Carbon sequestered in the first year: {carbon_sequestered_original} kgs")
    
    if carbon_sequestered_original > carbon_emitted:
        st.subheader(f"Great! You've completely sequestered your carbon emissions with {tree_number} trees.")
    else:
        st.write(f"Not yet! We still need to sequester {carbon_emitted - int(carbon_sequestered_original)} kgs more!")

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
            tree_age += 1
            st.write(f"Now that {tree_age-1} year(s) have passed, is there any difference in the amount of carbon sequestered?")     
            st.write(f"Last year, you chose to plant {st.session_state.tree_number} {selected_species} trees.")
            tree_diameter += tree_age*(tree_diameter*(1/(tree_age*0.75)))
            tree_height += 1
            st.write("The tree diameter is ", tree_diameter)
            st.write("The tree height is ", tree_height)
            st.write("The tree age is ",tree_age)
            
            carbon_sequestered_original += (tree_age * st.session_state.tree_number * 20) / 100
            
            st.write(f"Carbon sequestered in the second year: {carbon_sequestered_original} kgs")
        
            st.write("Notice how the number didn't just double over the last year?")
            expander = st.expander("Click me to see why")
            expander.write("""
                        As a tree grows up, it grows more wood to store carbon in. Hence, the amount of carbon a tree can sequester per year increases as it grows up.\n 
                        Since the tree grows quite a bit during its first year of life, it becomes an exponentially larger carbon sink until the age of 5, after which\n
                        there is a steady increase in a tree's ability to hold carbon
            """)
if st.session_state["begin_clicked"] and st.session_state["confirm_clicked"] and st.session_state["year_pass_clicked"] and carbon_sequestered_original > 1000:
    st.error(f"""
             Suddenly, the government of {selected_country} decides that the land you're using to plant these trees have oil under them. They send you a message to tell 
             them how many trees they will have to cut down to clear the area so that they can figure out how much labour they'd need
             """)
    tree_number_lost = st.slider("Choose how many trees the government must cut down", 0, st.session_state.tree_number)
    carbon_after_deforestation = (((((0.25*(tree_diameter*tree_diameter)*tree_height)*1.2)*0.725)*0.5)*3.67)* (st.session_state.tree_number - tree_number_lost)
    carbon_lost = carbon_sequestered_original - carbon_after_deforestation
    if st.button("Click me to confirm your choice"):
        st.session_state["tree_cut_confirm"] = True
        st.write(f"We lost {tree_number_lost} trees")
        st.write(f"Because of this, about {carbon_lost} kgs of the carbon we sequestered is now back into the atmosphere")
        
if st.button("Click me to see how much this entire process costs!"):
    st.session_state["carbon_offset_cost_confirm"] = True
    
if st.session_state["carbon_offset_cost_confirm"] and st.session_state["begin_clicked"] and st.session_state["confirm_clicked"] and st.session_state["year_pass_clicked"] and carbon_sequestered_original > 1000:
    # tree sapling (current placeholder is 'apple trees') per sapling costs about 80 rupees, and may decrease per unit cost in larger scale forestation initiatives
    st.markdown(f"Since we bought {tree_number} trees, and each sapling costs about 25 USD, we spent about {tree_number*25} USD on just buying the trees to plant them")
    st.markdown("We also spent some money caring for the trees, and following is the cost breakdown for each tree. Though some of these costs are shared amongst trees, for the sake of simplicity, lets assume each tree requires these costs individually")
    st.markdown(first_year_prices)
    st.markdown(f"But remember, we made a lot of money from our cups. To be specific, we made about {money_made} USD")
    st.markdown("Thus, our costs for this year can be calculated as the following:")
    st.latex("Cost_Per_Tree * Number_of_trees - Sales * Price_of_each_cup")
    st.markdown(f"This means that our total costs for our first year were about {(tree_number*first_year_prices_constant) - money_made} USD")

if st.button("Click me to delve deeper!") and st.session_state["tree_cut_confirm"] and st.session_state["begin_clicked"] and st.session_state["confirm_clicked"] and st.session_state["year_pass_clicked"] and carbon_sequestered_original > 1000:
        st.session_state["chapter_two_advance"] = True
        st.header("So that's it....right? Did we just solve the global carbon sequestration?")
        st.header("Like we have seen before, there are always more variables to take into consideration. So let's look further!")
    
# next chapter advancement button 

if st.session_state["begin_clicked"] and st.session_state["confirm_clicked"] and st.session_state["year_pass_clicked"] and st.session_state["chapter_two_advance"] and carbon_sequestered_original > 1000:
    st.header("Chapter 2: What's next?")
    st.subheader("insert additional c2 data)")





