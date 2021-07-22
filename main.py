import streamlit as st

def main():

    st.title("ISONOMIA")
    teams = ["Team A","Team B","Team C","Team D","Team E" ,"Team F","Team G","Team H","Team I","Team J","Team K"]
    teams_choice = st.sidebar.selectbox("Teams",teams)

    if teams_choice == "Team A":

        st.header("Team A")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "23759":
            st.subheader("Your Topic")
            st.write("**TESLA**")
            st.write("Tesla, one of the fastest growing and largest Companies of the modern world is known for the volatility of its CEO, Elon Musk. News has surfaced that Elon Musk crashed a Tesla car under the influence of multiple hallucinogens. The Media has covered the story multiple times. Shareholders are outraged. Large numbers of people have chosen to boycott Tesla and Elon Musk's other enterprises. As the spokesperson of Tesla, the world now looks to you for your statement on the future of Tesla. Good Luck.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "39475":
            st.subheader("Your Topic")
            st.write("**For this round, you will be Angela Merkel applying for a position in BMW.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "34975":
            st.header("Your Question")
            st.write("**David**")
            st.write("You are a crazy scientist who has no interest in mundane matters such as murder.You are honest and direct. You want to clear yourself of suspicions you want to return to continue your research and study the results of your painstaking experiment.You met Charles who seems like a capable student and showed him the lab and what work you were doing. You heard Andrew scream but didn't go because your work is far more important than solving the crime")
            st.write("**Where were you at the time of the murder?** Lab- Working- Experiment with acids and highly lethal chemicals- Charles came to the lab to take a quick look and see what he would be working with in the future- Tissue therapy- Lab Animals- I had Scalpels, Bleach, glass- It could be me but I wouldn't waste my time with murder- Heard Andrew scream- Didn't go- Important and dangerous experiment would have to be redone.")
            st.write("**What do you know about Frank?** Hard worker but not as much as me. Smart, but again not as much as me. Didn't particularly know him. We were working together and now he was going to get promoted and didn't even bother to inform me. How discourteous? He even told Brian to schedule an interview for his replacement without consulting with me first.")
            st.write("**Who do you think the murderer is and why?** Give the answer you think is right after the Evidence and Questioning along with a short explanation and justification and also add in why it's not you.")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team B":

        st.header("Team B")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "20838":
            st.subheader("Your Topic")
            st.write("**APPLE**")
            st.write("Apple, the multi-trillion dollar company is know for its quality and integrity. Tim Cook, the CEO of apple, one of the highest paid company executives was found to have a dark side. Police reports state that the billionaire has murdered over 20 people in the past decade. Tim Cook and his attorney have made no statement yet. With company stock plummeting and apple products getting boycotted, the world looks to the Spokesperson of Apple, you. Your statement can make or break one of the greatest legacies of our time. Good Luck.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "39937":
            st.subheader("Your Topic")
            st.write("**For this round, you will be Barack Obama applying for a job in United Healthcare.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "38749":
            st.header("Your Question")
            st.write("**Eric**")
            st.write("You have a family at home waiting for you.You finished work and wanted to leave. You are polite and trusting. You hope that the murderer is found so that you can return to your family. You don't suspect anyone.")
            st.write("**Where were you at the time of the meeting?** I had just finished work in the workspace- Went to break room to smoke- Went to kitchen to make lemonade to disguise the smell of the smoke from wife- Met Andrew- He was making coffee- Went to leave and heard a scream- Saw Charles in the lobby- Went with him to see what happened- Stayed in workspace until cops arrived")
            st.write("**What do you know about him?** He was a classic good guy. Made a good impression on everyone he met. Very friendly. My children called him uncle B. He was always so good with them. He was going to come over for Dinner next week. They'll be devastated to hear about this. I would never kill him.")
            st.write("**Who do you think the murderer is and why?**Give the answer you think is right after the Evidence and Questioning along with a short explanation and justification and also add in why it's not you.")

        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team C":

        st.header("Team C")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "73737":
            st.subheader("Your Topic")
            st.write("**MICROSOFT**")
            st.write("Microsoft, one of the wealthiest corporations in the world has been known for quality and integrity for decades. However, recently, reports have started emerging of Microsoft CEO, Satya Nadella, violating the privacy of multiple microsoft users, calling into question the security and reliability of the entire company. Users are switching to other operating systems. Shareholders are outraged. Share value is plummeting. Users are switching to other brand. Multiple lawsuits have been filed. It is now your duty as the Head of PR at Microsoft to sway public opinion and save the company. Good Luck.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "95858":
            st.subheader("Your Topic")
            st.write("**Kamala Harris applying for a job at oracle**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "37737":
            st.header("Your Question")
            st.write("**Brian**")
            st.write("You are a heroic character and care about justice. You weren't very close with Frank but care about right and wrong. You will do whatever it takes to get to the bottom of this mystery. ")
            st.write("**Where were you at the time of the murder and what were you doing?** Meeting room- About to have a meeting with Charles-Job interview- Finished work in Workspace- Went to kitchen to get a snack- Went to meeting room to wait- Heard Andrew scream and came to the lobby- Saw the body of Frank in workspace- Second person to get there- Called police")
            st.write("**What do you know about Frank?** Colleague- Polite. Hard worker. Efficient. Well mannered. We met here and weren't particularly close. Everyone who met him liked him. He was going to get a promotion and there was going to be a surprise party.")
            st.write("**Who do you think the murderer is and why?** Give the answer you think is right after the Evidence and Questioning along with a short explanation and justification and also add in why it's not you.")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team D":

        st.header("Team D")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "30949":
            st.subheader("Your Topic")
            st.write("**FACEBOOK**")
            st.write("There have long been suspicions that Mark Zuckerberg, CEO of Facebook, one the largest social media networks and also the parent company to some of the other largest networks, is not human. Recently, these fabrications turned out to be true. Zuckerberg, after being in a car crash, was taken to an emergency room and rumors of his supposed alien physiology have reached an all time high. Massive, news channels and media networks have covered this story and users of Facebook, WhatsApp and Instagram are rapidly deleting accounts from fear of having their information leaked to an extraterrestrial intelligence. It is your job as the spokesperson of Facebook to pacify their concerns and save Facebook. Good Luck.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "93930":
            st.subheader("Your Topic")
            st.write("**For this round, you will be Vladimir Putin seeking a job in Google**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "76464":
            st.header("Your Question")
            st.write("**Charles**")
            st.write("You are the murderer. Try to be calm and convince them that it's not you. You were Frank's college bully and now he had a high level job in a big company. You were unable to find a job anywhere else and you had a family to feed. You were worried he was going to tank your interview so you went to the lab and stole a scalpel and some bleach when David wasn't looking. You stabbed Frank, went to the lobby and cleaned the scalpel with bleach and hid the scalpel under the sofa. You saw Eric and decided to pin the blame on him and then went to the kitchen after seeing the blood on your tie that no one noticed. You washed it off and went to the break room for it to dry")
            st.write("**Where were you at the time of the murder?** Lobby- About to have a meeting with Brian- Just entered. Went to lab- Met David- Went back to lobby- Saw Eric about to leave from the direction of the murder-Seemed to be in a suspicious hurry- Heard Andrew scream and we both came- stepped on broken mug- Shards were very sharp- Went to Lean Back room to take a breath when the police arrived")
            st.write("**What do you know about Frank?** He was my friend back in college. We hadn't met each other in a long time. When he found out that I'm going to work here he said he would put in a good word for me with Brian. He helped me move to the city and said we should have lunch and catch up sometime.")
            st.write("**Who do you think the murderer is and why?** Give the answer you think is right after the Evidence and Questioning along with a short explanation and justification and also add in why it's not you.")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team E":

        st.header("Team E")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "92929":
            st.subheader("Your Topic")
            st.write("**PFIZER**")
            st.write("In the current situation of a global pandemic, Pfizer, one of the top vaccine makers has raked in billions of dollars through sales of their serum.  However, Pfizer CEO Albert Bourla was recorded saying the vaccine will kill people faster than the disease.The authenticity of the tape is being investigated and so is the safety of the vaccine. The people are still unconvinced and the product is being boycotted globally. Hunderds of Millions worldwide are demanding refunds and compensation. As the spokesperson of Pfizer, it is your job to reassure the world of the safety of your vaccine. Good Luck.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "75799":
            st.subheader("Your Topic")
            st.write("**For this round you will be Jacinda Ardern applying for a job at Apple.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "38469":
            st.header("Your Question")
            st.write("**Andrew**")
            st.write("You just saw the dead body of your best friend Frank. You are in a state of shock and will do anything to find out who did this and get justice for Frank.")
            st.write("**Where were you at the time of the murder?** Near Kitchen- Making coffee-About to pull an all nighter- Found the body in the workspace- On the way to the break room- Dropped coffee mug from shock- Called ambulance")
            st.write("**How did you know Frank?** Best friend- We met after he started working here. He was funny, kind, polite, and smart. He helped me when we started working here. He was there for me when my parents died. We used to go to an orphanage every week to do social work. He was rich so it could have been about money. He was going to get engaged soon so it could have been done by a love rival. Or it might be because he was going to get a promotion.")
            st.write("**Who do you think the murderer is and why?** Give the answer you think is right after the Evidence and Questioning along with a short explanation and justification and also add in why it's not you.")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team F":

        st.header("Team F")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "39393":
            st.subheader("Your Topic")
            st.write("**WALMART**")
            st.write("The retail giant has come under fire recently as multiple anonymous sources that claim to be employees have released tapes of Walmart managment threatening and bribing officials to get rid of local competition. Multiple inquiries into these allegations are ongoing but consumers have started boycotts and pickets of Walmart to show solidarity for small retailers. As the PR representative of Walmart, the world looks to the for your response.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "29923":
            st.subheader("Your Topic")
            st.write("**Shinzo Abe applying for a job at Toyota.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "37773":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team G":

        st.header("Team G")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "39479":
            st.subheader("Your Topic")
            st.write("**GOOGLE**")
            st.write("Google, one of the largest tech companies of the modern world has been known for its reliability and is used as a trusted research resource by the world. Recently, stories have surfaced of Sundar Pichai, the CEO of Google being involved in multiple cases of search result manipulation. Within just days of this information being made public, daily searches have fallen by 70% and brands are withdrawing their ads from the platform.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "28123":
            st.subheader("Your Topic")
            st.write("**Xi Jinping applying for a job at Xiaomi.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "28461":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team H":

        st.header("Team H")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "40347":
            st.subheader("Your Topic")
            st.write("**MC DONALD**")
            st.write("McDonald's has come under massive strain after videos of their meat freezers were shown with rotting meat. Inspections and investigations are ongoing but the sales have fallen to an all time low. Regular customers have fled to major competitors and the world looks to you, the PR representative for your response")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "39404":
            st.subheader("Your Topic")
            st.write("**Donald Trump applying for a job at Walmart.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "37398":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team I":

        st.header("Team I")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "30497":
            st.subheader("Your Topic")
            st.write("**NETFLIX**")
            st.write("One of the largest digital media streaming platforms is under fire after a Netflix original series was released portraying Hitler as the protagonist and attempting to humanize his crimes. Consumers have started boycotting Netflix and investors are outraged. With the world's gaze upon you, the PR rep of Netflix, what do you have to say?")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "34877":
            st.subheader("Your Topic")
            st.write("**Emmanuel Macron applying for a job at Facebook.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "39462":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team J":

        st.header("Team J")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "39412":
            st.subheader("Your Topic")
            st.write("**MATTEL**")
            st.write("One of the largest toy manufacturers has become the most hated company in the world after over 30 cases were revealed of Children dying due to choking on Mattel toys. Mattel has reportedly threatened and silenced the parents to prevent this information from spreading. After its reveal, people have started raising and destroying Offices, warehouses and stores of Mattel. Mattel and its associated products are being boycotted and some are even taking legal measures. As the PR representative of Mattel, the fate of the company is on your shoulders")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "24971":
            st.subheader("Your Topic")
            st.write("**Justin trodeau applying for a job at Netflix.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "58709":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")


    elif teams_choice == "Team K":

        st.header("Team K")
        st.subheader("Round 1")
        teamp = st.text_input("Type for round 1 Password ")
        if teamp == "40548":
            st.subheader("Your Topic")
            st.write("**CHANEL**")
            st.write("Chanel, one of the largest perfume makers has been thrown into a PR disaster after cases of the products causing cancer have come to light. Many suspect that the officials of Health and Safety Boards across the planet may have been bribed to allow the products to be approved. Class Action law suits have been filed against Chanel and consumers all across the world are boycotting the company. As, the PR representative of Chanel, the world looks to you for your statement.")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 2")
        password = st.text_input("Type for round 2 Password")
        if password == "56083":
            st.subheader("Your Topic")
            st.write("**Arnold Schwarzenegger applying for a job at Nike.**")
        else:
            st.write("try again incorrect password")

        st.subheader("Round 3")
        password2 = st.text_input("Type for round 3 Password")
        if password2 == "23072":
            st.header("Your Question")
        else:
            st.write("try again incorrect password")



if __name__ == '__main__':
     main()
