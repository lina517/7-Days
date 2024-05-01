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
    "Good evening, Dr. Mark, I hope I'm not disturbing you."
    "I just need to ask you something important. Have you received any threats recently? Is there anyone who might want to harm you?"
    "Dr. Mark's expression shifts from surprise to suspicion as he regards you intently.'What? Who are you?' he demands,
    his tone laced with caution.'And why are you asking me this question at this time... and in this manner?'"
    "I apologize for the abruptness of my inquiry, you reply, choosing your words carefully."
    "I want to tell you that someone sent me to kill you and I want to know who this person is, don't worry I'm not here to hurt you "
    "But I have reason to believe that your safety may be at risk. Please, Dr. Mark, if there's anything you know or anyone you suspect, it's imperative that you share it with me."
    "You know you must tread carefully, for the truth may be far more dangerous than you realize."
    "But for a moment, the doctor remembers what the forensic doctor said to him the last day... So without thinking, he blurts out: 'Oh, so you're talking about Mr.KEVIN_MITNICK!"
    "MR.KEVIN MITNICK ?? YOU'VE NEVER HEARD A NAME LIKE THIS BEFORE!"
    "maybe this man could be the hacker ,you need more informations about him , this criminal doctor must be punished for his crimes"
    "Can you tell me who KEVIN_MITNICK is?"
    "Look at me, I have no problem with him, he will never be able to prove what he claims by saying that I hurt his mother"
    "so I am not and I will not be afraid of him or his family, let him do what he wants and we will see who has the power between us. I've spent years building my reputation and my empire. so after this 15 years No one can touch me."
    "So you realize that this criminal doctor is the leader of a dangerous organizationو you have to be more carful"
    menu:
        "1-Evidence gathering process":
            jump Evidence_gathering_process
        "2-Search for hacker":
            jump Search_for_hacker
label Evidence_gathering_process:
    "NoTES:\n"
        "What happen before 15 years old?\n"
        "What is the relation between doctor and hacker , what did he do to his mother\n"
        "What the relation btween the first and the second victime (1 and 2 end task)\n"
        "What the relation between the doctor and mr.Henry the old friend of mark ?"
menu:
    "Investigate the matter":
        jump Investigate_the_matter