label start:

label start_task:
    scene bg dark_home
    "Hey again,\ let's say this is the last task you have to do so don't worry and work hard .."
    "Our victim for today is an old man who appears to be 58 years old name's mark."
    "He lives in Hooker Town, has a wife and a 17-year-old daughter. His bedroom is on the second floor, and his daughter's room is next to his."
    menu:
        "How can I find him?":
            jump choice1

label choice1:
    "When I send you the location, you start the quiet hour of 2 am, taking advantage of the cover of darkness."
    #"Allow excitement to build as you prepare for the task ahead, recognizing that his day off will be devoted to this important mission.
    #"Identify his vehicle by its white license plate with the code \"REJ-256.\"
    #"insure that all preparations are complete for the operation to start smoothly in the early hours of the morning."

    menu:
        "next day..":
            jump Next_day

label Next_day:
    scene message 1
    menu:
        "Following the location":
            jump next

label next:
    "As you stealthily followed Mark's car through the dimly lit streets, your focus remained sharp, every step calculated to avoid detection."  
    "Suddenly, a familiar figure appeared from the shadows—an old friend of Mark's named Henry."
    "Your pulse quickened when you noticed the interaction, your curiosity piqued by the urgency of the man's demeanor."
    menu:
        "Continue..":
            jump Continue

label Continue:
    "Impatiently, you strained to listen to their conversation, your senses on high alert. "
    "But for a moment, you noticed that the man was the father of the girl who had been tortured by the past victim!"
    "The man’s words hinted at something urgent, which made you feel uncomfortable. "
    "Mark's demeanor changed, his expression growing tense as he absorbed his old friend's words."
    menu:
        "Tell the hacker what happened":
            jump Tell_the_hacker
        "Wait until Mark comes home":
            jump Wait

label Tell_the_hacker:
    "What! Oh my God, there's been a change in the plan. You have to go back tomorrow."
    menu:
        "Continue1":
            jump Continue1

label Wait:
    "You wait next to his house, but unfortunately, Mark didn't return."
    "Consequently, you're forced to inform the hacker about everything that happened."
    menu:
        "You have to wait for him to send you a text message.":
            jump wait_him

label Continue1:
    scene message 2
    menu:
        "Let's start":
            jump Lets_start

label wait_him:
    "     AFTER 7 HOURS.."
    "New Message !!
The plan changed
Time : Today at 3 AM
Location : 975 Baptist Way, Homestead, FL 33033"
    menu:
        "Let's start":
            jump Lets_start

label Lets_start:
    "After following Mr. Mark, you arrived at his mansion, your anticipation palpable as you approached the imposing gates."
    "You steadied yourself and entered the grand entrance hall, nerves and determination driving you forward."
    "Every creak of the floor heightened your awareness as you made your way to Mark's study."
    "With resolve,you pushed open the door, keenly attuned to the charged atmosphere within."
    menu:
        "What happen after?":
            jump Happen
label Happen:
    "As you awaited Mark's next move, expecting him to head to his bedroom to execute our plan, he surprised you by deviating from the expected path."
    "Instead of going upstairs, Mark disappeared from sight, his movements shrouded in mystery."
    " Intrigued, you monitored his progress through security cameras installed around the mansion."
    "To your astonishment, you watched as Mark descended into the depths of the basement, his determination unwavering as he approached a nondescript door that held an air of secrecy."
    menu:
        "Go straight in behind him":
            jump Go_straight_in_behind_him
        "Wait a little bit":
            jump Wait_a_little_bit

label Go_straight_in_behind_him:
    "As you walked behind Mark, the hacker sent you a message, causing your phone to ring."
    "Unfortunately, Mark heard a sound, prompting him to quickly return upstairs."
    menu:
        "i wait him till he  return ":
            jump i_wait_him_till_he_return

label i_wait_him_till_he_return:
    "Mark returned, visibly terrified, and rushed downstairs, his face displaying worry and tension.He entered a room that appeared somewhat secret."
    menu:
        "Go check the secret room":
            jump Go_check_the_secret_room
label Wait_a_little_bit:

    "As you monitored the flickering light of the computer screen, a sudden interruption occurred when you glimpsed Mark's daughter returning home"
    "her cheerful voice echoing through the mansion's halls."
    "Reacting swiftly, Mark abandoned his exploration of the secret room to intercept his daughter, ensuring his clandestine activities remained concealed from her curious gaze with practiced stealth."

    menu:
        "1-Go check the secret room":
            jump Go_check_the_secret_room
label Go_check_the_secret_room:
    "Your eyes adjusted to the dim light, revealing rows of gleaming stainless steel instruments and medical equipment lining the walls—a stark contrast to the opulence of the rest of the mansion.."
    " so Mr Mark is a Doctor in real life !"
    menu:
        "What!! How!! Give me more information please..":
            jump more_informations
label more_informations:
    "You cautiously accessed the laptop's 'SECRET FILES', discovering a meticulously organized collection detailing Dr. Mark's illicit activities."
    "Among them was a file labeled 'OPERATIONS', which revealed a horrifying list of victims who had been deprived of organs or had perished due to Dr. Mark's actions."
    "Shock and outrage consumed you as you grasped the extent of his depravity, realizing innocent lives had been irreversibly altered to serve his twisted ambitions"

    menu:
        "1- Make a screenshot of all the names list":
            jump made_a_screenshot
        "2- Copy all files to flash disk":
            jump Copy

label made_a_screenshot:
   "2- Copy all files to flash disk":
            jump Copy

label made_a_screenshot:
    "The doctor returns to the secret room, so you have to choose one from these two choices:"
    menu:
        "1- Quickly exit the house via the stairs":
            jump exit_the_house
        "2- Wait for the doctor to confront him with the truth":
            jump Wait

label Copy:
    "After copying all the files, you hear the doctor enter the room, so you have to choose one of these two choices:"
    menu:
        "1- Quickly exit the house via the stairs":
            jump exit_the_house
        "2- Wait for the doctor to confront him with the truth":
            jump Wait
label exit_the_house:
    "As you stand in front of the doctor's house, your heart races with anticipation and understanding. The weight of the secrets you've uncovered weighs heavily on your mind."
    "You take a deep breath, steeling yourself for the confrontation ahead."
    "The door cracks open, and Dr. Mark steps out onto the porch, his expression unreadable."
    "You try to maintain a calm facade, masking the turmoil raging inside you. With each passing second, the tension between you grows palpable, like a storm brewing on the horizon."
    "For a moment, the doctor noticed that you were waiting for him to say something.."

    menu:
        "Start talking to him":
            jump talk

label talk:
    "Good evening, Dr. Mark, I hope I'm not disturbing you.\n
    I just need to ask you something important. Have you received any threats recently? Is there anyone who might want to harm you?"
    "Dr. Mark's expression shifts from surprise to suspicion as he regards you intently. 'What? Who are you?' he demands, his tone laced with caution.And why are you asking me this question at this time... and in this manner?"
    "I apologize for the abruptness of my inquiry, you reply, choosing your words carefully.\n I want to tell you that someone sent me to kill you and I want to know who this person is. Don't worry, I'm not here to hurt you."
    "But I have reason to believe that your safety may be at risk. Please, Dr. Mark, if there's anything you know or anyone you suspect, it's imperative that you share it with me."
    "You know you must tread carefully, for the truth may be far more dangerous than you realize.\n"
    "But for a moment, the doctor remembers what the forensic doctor said to him the last day... So without thinking, he blurts out:\n"
    "'Oh, so you're talking about Mr. KEVIN_MITNICK!'\n"
    "'MR. KEVIN MITNICK?? YOU'VE NEVER HEARD A NAME LIKE THIS BEFORE!'"
    "'Maybe this man could be the hacker, you need more information about him. This criminal doctor must be punished for his crimes.'"
    "Can you tell me who KEVIN_MITNICK is?\n"
    "'Look at me, the story started in 2010 when he was 15 years old. His mom died and his father accused me of being responsible for her death, so he pursued us legally.\n"
    "What do you mean about 'us'?\n"
    "Yes, they pursued me, and the forensic doctor.'"
    "'My lawyer won the case against them, and we were declared innocent of this accusation.\n"
    "I am not and I will not be afraid of him or his family. Let him do what he wants and we will see who has the power between us.'"
    "'So you realize that this criminal doctor is the leader of a dangerous organization. You have to be more careful.'"
    menu:
        "2-Search for hacker":
            jump Search_for_hacker

label Search_for_hacker:
    "Notes:\n
    Some information the doctor said about the hacker:\n
    Name: KEVIN_MITNICK\n
    Age: 29 years old\n
    He is a hacker\n
    The doctor involved in the murder of his mother."
    menu:
        "Go search for him":
            jump Go_search_for_him

label Go_search_for_him:

    "After 5 hours, you finally found where Kevin is living. When you were near his house, you received a phone call... It was the hacker!"
    "'Hello, what's the news? I was waiting for you to send me the pictures. Why didn't you finish the task?'\n
    Because I finally know who you are. So, open the door.\n
    Yes, as you see, I'm here, Mr. KEVIN_MITNICK, and I know what you are trying to do.\n"
    "'Oh come on, how did you find me? I tried to leave no trace.'"
    "'I admit that my choice was the most appropriate. Look, this is no time to joke around because the people you think you have the power to take down are more dangerous than you think.'"
    "'What danger are you talking about? You don't know anything about me or what I'm doing.'\n"
    "'No, I know everything. I know about your mother.'"
    "'Mom!!!\n Yes, your mom. I know that Mr. 'Mark' is a doctor, Mr. 'Henry' is a forensic doctor, and Mr. 'John' is a lawyer in your mother's murder case.'"
    "'Yes, of course, he probably lied to you. But wait, how did he let you go after he found you sneaking into his house?'"
    menu:
        "Tell him the truth of the doctor":
            jump doctor_truth

    label doctor_truth:
    "Before I tell you the truth about everything, you have to promise something first...\n
    What do you mean about the truth? If there's a truth, then it's me who should tell it to you.\n
    Okay, so tell me."
    "I don't know what exactly the doctor told you, but the real thing that you have to know is this: the doctor killed my mother because of a medical error during surgery.\n
    When he refused to confess, a case was filed against him and the forensic doctor who was with him."
    "However, the lawyer managed to secure their acquittal through bribery."
    "So, this is the reason for doing all these tasks, and in the end, you failed to have the doctor punished for his crime."
    "You open your laptop and show him all the pictures and files you found in the secret room.\n"
    "Yes, Mr. Kevin Mitnick, as you can see, this doctor is a criminal who traffics in people's organs.\nI found this secret operations room in his house.\n I have all the evidence that proves the crimes of this criminal doctor, including the file of the forensic doctor who was involved with him."
    "How?! I can't believe it! I never knew any of this about him. The only thing I know is that he killed my mother due to a medical error during surgery."
    "Look, Mr.Kevin Mitnick, we can cooperate and eliminate them because the police will definitely be able to catch them this time. However, there's a condition: you have to forget about the 200 million stolen cash in my bank accounts."
    "I'm really shocked about all of this..but as you said, this is the only way to make this criminal and everyone who was involved with him pay the price for their crimes. You and I can't hold them accountable on our own.."
    "We must cooperate with the police"
    "HELLO 911 ?"
    #===================================================================================================================================================================================================================================================================================================================
label wait:
    "As you wait for the doctor to return, your mind races with questions about the truth behind the secret room and the organ trade.\nYou know that confronting the doctor is the only way to uncover the answers you are looking for."
    "Finally, you hear the sound of footsteps approaching, and the doctor is coming. His expression is unreadable, but you sense tension in the air as you prepare to confront him.\n
    'Dr. Mark'\n'What are you doing in my house? How did you manage to enter here?!'... As tension mounts, Dr. Mark tries to inject you with a syringe, but you narrowly evade it.\n Wait, wait... look, I don't know what I'm doing here. He sent me to kill you. Do you know him?"
    "What are you talking about?"
    "I'm sure that you have an idea about him, of course you have a lawyer, someone has a daughter... yes, named Henry, and you, he knows all of you.\n
    Oh well, you are talking about Mr. Kevin Mitnick. Yes, Henry told me yesterday about him. I know that he's been following me these days... but he will never catch me."
    "Told me about him, please.\n Well, look the story started in 2010 when he was 15 years old. His mom died and his father accused me of being responsible for her death, so he pursued us legally.\n What do you mean about 'us'?"
    "Yes, they pursued me, and the forensic doctor Henry.\n My lawyer, John Joh, won the case against them, and we were declared innocent of this accusation.\n But you know, I know all the truth about you, Mr. Mark.\nYes, that's why you have to die now."
    "After 17 hours, and after your family called 911, finally the police found you dead in Dr. Mark's house.\nThe police found a murder weapon and discovered that the doctor trafficked in human organs, leading to his arrest and imprisonment."
    "After 15 days, the doctor decided to confess to all his crimes and also admitted that the forensic doctor and the lawyer were involved with him."
