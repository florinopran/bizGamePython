
# RELATIONSHIP

GIRLFRIEND_NAMES = [
    "Lila", "Ava", "Mira", "Zara", "Aria", "Nina", "Selene", "Elara", "Talia", "Cora",
    "Sophia", "Emma", "Isabella", "Olivia", "Mia", "Amelia", "Chloe", "Luna", "Eva", "Grace",
    "Aurora", "Scarlett", "Violet", "Hazel", "Elena", "Penelope", "Lucy", "Hannah", "Leah", "Stella",
    "Alice", "Ellie", "Naomi", "Ruby", "Lydia", "Emily", "Jade", "Ivy", "Rose", "Evelyn",
    "Harper", "Bella", "Victoria", "Daisy", "Claire", "Natalie", "Madeline", "Anna", "Elise", "Maya",
    "Sienna", "Audrey", "Layla", "Julia", "Sophia", "Savannah", "Adeline", "Amara", "Caroline", "Isla",
    "Faith", "Skylar", "Autumn", "Lillian", "Zoe", "June", "Eleanor", "Willow", "Phoebe", "Camila",
    "Jasmine", "Melody", "Serena", "Alina", "Fiona", "Celia", "Ariana", "Freya", "Alyssa", "Isabelle",
    "Piper", "Brooklyn", "Genevieve", "Liliana", "Adriana", "Summer", "Valeria", "Callie", "Marina", "Esme",
    "Lena", "Daphne", "Bianca", "Noelle", "Juliet", "Carmen", "Tessa", "Delilah", "Iris", "Clara"
]


RELATION_EVENTS=["Let's go out!",
                    "Let's be wild tonight!",
                    "Let's go for an adventure!",
                    "Let's dance all night in the club!",
                    "Surprise me with something nice!",
                    "Let's do nasty things in a public place!",
                    "Let's walk on the beach \nand look at the moon!",
                    "Take me far away!"                        
                    ]

# RELATION_SOFT_DILEMA          -   -   -   4
# RELATION_HEAVY_DILEMA         1   2   -   -
# RELATION_COMMITTED_DILEMA     -   2   3   -
# RELATION_SELF_DILEMA          -   2   3   -


# MARRIED COUPLES (datingStatusScore==4)
RELATION_SOFT_DILEMA=[
    "What do you value most about our\nrelationship?💑",
    "How do you see us growing together\nin the future?🌱",
    "Do you think we’re a good team?🤝",
    "What do you love most about me lately?💘",
    "Do you think I’m still beautiful?🌹",
    "How do you feel about the way I look?🧐",
    "You’re still the one for me.\nJust wanted you to know that...💖",
    "Are you okay? You’ve been a little\nstressed in the last few days...😟",
    "We should help some kids this\nChristmas! And maybe we could\nhave our own someday...👶🎄",
    "Let’s make love tonight!💋",
    "We should go out more often!💃🏽",
    "What’s something about me \nthat always makes you smile?😊",
    "How can we make each other’s lives even happier?💫",
    "What’s your favorite memory of us so far?📸",
    "Miss you, baby!💖"
                    ]

#  (datingStatusScore=2/3 = lady/engaged)
RELATION_COMMITTED_DILEMA= [
    "Do you think we’re a good team?🤝",
    "How do you feel about us in the long term?🧐",
    "How do you see us growing together...\n in the future?🔮",
    "Will you still love me in the long run?💭",
    "Do you even know I exist?😞",
    "Do you think I’m still beautiful?🌹",
    "Do you think I’ve gained weight lately?🤔",
    "Tell me that you love me. I really need to hear it.💬",
    "I missed you today. \nHold me tight and tell me that you love me.💑",
    "Let's make love tonight!💖"
                    ]

#  (datingStatusScore=1/2 = girlfriend/lady)
RELATION_HEAVY_DILEMA= [
    "What do you value most... \nabout our relationship?😢",
    "Do you see us growing together...\n in the future?😃",
    "What does being in love mean to you?❤️",
    "Do you think we’re compatible?🤔",
    "How do you feel about us in the long run?🤔",
    "Do you love me?💘",
    "Am I special to you?💖",
    "Do you even know I exist?😞",
    "Are we wasting time together?⏳",
    "Do you think I'm beautiful?😊",
    "Do you think I'm fat?😔",
    "Why are you staying with me?🙇‍♀️",
    "What am I for you?💭",
    "I'm crazy about you. Damn it!🥺💘",
    "I feel that you're using me...😢",
    "Say you love me. \n'Cause I really hate you right now!\n Soooo much...😢😠",
    "Let's make love tonight!💋"
                    ]
# mature couples (datingStatusScore=2/3 = lady/engaged) - with mirror
RELATION_SELF_DILEMA=[
    "Do you think I dress in a way\nthat suits me?😞",
    "Do you think I’m beautiful?😔",
    "Do you think I’ve gained weight lately?🤨",
    "Do I have dark circles around my eyes? \nWhat do you think?😔",
    "Why are you staying with me?😢",
    "What’s the first thing \nyou noticed about me when we met?🤔",
    "Do you prefer me with a natural look \nor when I dress up?😕",
    "Will you still love me when \nI’m old, fat, and wrinkled?🥺"
]

ADVISER_PEDIA={
    "randomAdvice":[
                "\n🪙Investments generate returns between "
                "\n-13% and +20%, plus dividends.",

                "\n🪙You can make or lose money and friends "
                    "\nif you go gambling or clubbing.",

                "\n🪙If you deposit money in bank, "
                "\nyou get 3% interest.",
                
                "\n🪙Keep your eyes on your credit line."
                    "\nThe interest is burdensome."
                    "\nAlways keep some money in deposit & cash.",
                
                "\n🪙When you train, you get friends, skills, maybe a wife... "                    
                    "\n 👉 Friends/Connections help you in your business."
                    "\n 👉 skills improve your chances in everything."
                    "\n 👉 while a wife improve your connections.",
                
                "\n🪙In business you need money and connections."\
                    "\n 👉 Connections also bring you an extra profit."
                    "\n 👉 A low level businesses is rarely profitable.",
                
                "\n🪙Each business skill raise your profit with 2%",
                
                "\n🪙A job takes a lot of energy."                
                    "\nA business gives you more spare time."
        ],

    "help":     ("Main topics: 👉 business | bank | job | stock | social | skills"
                 "\n\nSecondary topics for business: 👉 upgrade | boost | scam | exit"
                 "\n\nSecondary topics for bank: 👉 credit | deposit | networth"                 
                 "\n\nSecondary topics for social: "
                 "\n                            👉 roulette | club | cocaine"
                 "\n                            👉 friends | wife | charity"
                 "\n\nSecondary topics for skills: 👉 train | masterclass | socialize"
                 "\n\nJust type your interest and i'll guide you through."
                 ),
    # SOCIAL
    "roulette": (
        "Adviser: 🎲\n"
        "You can only bet on black or red. You might earn a lot, \n"
        "if you're lucky! 🍀\n"
        "When you leave, you'll pay 10% of all the money you \n"
        "brought to the table. 💰\n"
        "So... don't come with more than you're ready to lose."
    ),

    "club": (
        "Adviser: 🎉\n"
        "The club is fun, but it can harm your financial balance. ⚠️\n"
        "You might find new connections, especially while playing \n"
        "poker with serious money. But be cautious! If you lose, \n"
        "your credit line could rise dangerously. 💳📈\n"
        "Also, you might meet a girl there. 💕\n"
        "Starting a relationship could make things more complicated."
    ),

    "cocaine": (
        "Adviser: 🚫\n"
        "You're not advised to buy cocaine! ❌ But each dose gives \n"
        "you 50% energy boost. ⚡\n"
        "However, each dose will cost more and more. 💸\n"
        "You'll also meet suspicious people—you could get robbed \n"
        "or even beaten. 🥊"
    ),

    "friends": (
        "Adviser: 🤝\n"
        "Everything is about connections! 🌐\n"
        "They are essential for your business. 📊\n"
        "You can use them to make both legit and illegit profits. 💼\n"
        "So, invest in building strong relationships!"
    ),

    "wife": (
        "Adviser: 💍\n"
        "You can be single, dating (a college girl or a lady), \n"
        "engaged, married, or divorced. 💔\n"
        "Having a partner will increase your monthly costs, 💸\n"
        "but it will also improve your connections. 🤝\n"
        "When you're prosperous, a relationship might become \n"
        "a valuable asset!"
    ),

    "charity": (
        "Adviser: 🤲\n"
        "You need money and connections to attend charity events. 🎉\n"
        "If you can't build strong connections (above 40) in clubs, \n"
        "charity is a great alternative. 🌟\n"
        "Be careful—if your donation is below your net worth, \n"
        "you might lose reputation (and connections). ⚠️\n"
        "Minimum donations should be 1–5% of your net worth."
    ),
    # SKILLS
    "train": (
        "Adviser: 🏋️\n"
        "You can improve your soft skills (social, business, and scam skills).\n"
        "Social Skills: Just socialize—it won't cost much. 👫\n"
        "Business and Scam Skills: Attend a Masterclass. 🎓\n"
        "It might be expensive, but it's worth it!"
    ),

    "masterclass": (
        "Adviser: 🎓\n"
        "Masterclasses cost a lot of money and energy! ⚡\n"
        "Each class will boost your business and/or scam skills. 📈\n"
        "It's also a great place to make valuable connections! 🤝\n"
        "The cost depends on your business skills, as you require\n"
        "more advanced knowledge (Cost = 100 + (bizSkill**2) * 100). 💰\n"
        "For example:\n"
        "👉 bizSkill 10: Cost = 100 + 10 * 10 * 100 = $10,100\n"
        "👉 bizSkill 15: Cost = 100 + 15 * 15 * 100 = $22,600"
    ),

    "socialize": (
        "Adviser: 🌟\n"
        "Costs range from $5 to $25, plus up to 0.5% of your net worth. 💸\n"
        "You can make new friends or spend time with your old ones. 👫"
    ),
    # BUSINESS
    "business": (
        "Adviser:\n"
        "You can raise your business up to level 15.\n"
        "Profits are influenced by:\n"
        " - Connections (+0.2pp max for each connection, capped at 15pp).\n"
        " - Business skill (+2pp for each business skill).\n\n"
        "If you'd like, I can explain more about:\n"
        " - How to exit the business (\"exit\").\n"
        " - How to upgrade your business (\"upgrade\").\n"
        " - How to scam your partners (\"scam\").\n"
        " - How to improve your business skills (\"skills\")."
    ),


    "exit": (
        "Adviser:\n"
        "👉 You can sell your business, but it's not always profitable.\n"
        "👉 If your business wasn't profitable last week, you'll get less\n"
        "   than $7,000. 💸 This might still help reduce your credits. \n\n"
        "👉 If your business is profitable, a secret offer will be made.\n"
        "   The offer will range between 0.33% and 1.3% of your business\n"
        "   value. You'll have limited information during negotiation. 🤝\n\n"
        "👉 Business value is determined by ROI, connections (con), and\n"
        "   total investments (TI). 💼\n"
        "   TI = Total investments you’ve made in your business."
    ),

    "upgrade": (
        "Adviser:\n"
        "You can upgrade your business up to level 12.\n"
        "Each upgrade requires an investment calculated by this formula:\n"
        "👉 (next level ** 2) * $7,000\n\n"
        "Don’t forget about connection requirements: (next level * 10 + 1).\n"
        "Example:\n"
        "Level 7 to level 8:\n"
        "   8 * 8 * $7,000 = $448,000 (+81 connections).\n"
        "Level 8 to level 9:\n"
        "   9 * 9 * $7,000 = $567,000 (+91 connections).\n\n"
        "As you can see, upgrades become more expensive,\n"
        "but they’re profitable in the long run if you have strong connections!"
    ),

    "boost": (
        "Adviser:\n"
        "If you have the resources, you can upgrade your business "
        "\nat a faster pace.\n"
        "👉 Costs will be 30% higher than step-by-step growth.\n"
        "👉 You'll also need 30% more connections."
    ),

    "scam": (
        "Adviser:\n"
        "You can scam your partners for illegitimate profits, but it’s risky:\n"
        "👉 Earn 3% of your business value for each scammed partner.\n"
        "👉 Upset partners may leave or even sue you.\n"
        "👉 Authorities might fine you or send you to jail (for 2 weeks).\n"
        "👉 All litigation costs and fines will add to your credit line,\n"
        "   potentially destabilizing your finances."
    ),

    "skills": (
        "Adviser:\n"
        "There are 3 types of skills:\n"
        " - Business skills (\"bs\").\n"
        " - Scam skills (\"ss\").\n"
        " - Personal/social skills (\"ps\").\n\n"
        "👉 Gain 'bs' and 'ss' through business training.\n"
        "👉 Gain 'ps' through personal training and club activities.\n\n"
        "Uses of each skill:\n"
        " - BS: Useful for business growth.\n"
        " - SS: Helps in scams.\n"
        " - PS: Aids in finding dates, jobs, and renegotiating salaries."
    ),

    "job": (
        "Adviser:\n"
        "Standard salary: $1,000.\n"
        "👉 Social skills greatly influence job offers.\n"
        "👉 Maximum potential raise: 11%.\n"
        "👉 Energy requirements vary between 30% and 60%."
    ),

    "stocks": (
        "Adviser:\n"
        "Investing in stocks offers potential ROI:\n"
        " - Real asset value appreciates monthly by 1-5%.\n"
        " - Market value is more volatile and unpredictable.\n\n"
        "Keep an eye on the stock market to make informed decisions!"
    ),

    "bank": (
        "Adviser:\n"
        "Banks are part of your financial ecosystem:\n"
        "👉 Deposits earn 2% monthly interest.\n"
        "👉 Keep some cash for liquidity.\n"
        "👉 Invest in assets (businesses, stocks, etc.).\n\n"
        "Maintain a balance of cash and deposits to avoid inflating "
        "\nyour credit line."
    ),

    "credit": (
        "Adviser:\n"
        "Credits can spiral out of control if not managed properly:\n"
        "👉 Losing money at clubs, paying fines, or litigations can "
        "\ninflate credits.\n"
        "👉 Running out of cash or deposits worsens the situation.\n\n"
        "Weekly repayment rate: 10% of total credits:\n"
        " - 3% reduces principal.\n"
        " - 7% covers interest.\n\n"
        "Manage your credit wisely to avoid financial troubles!"
    ),

    "deposit": (
        "Adviser:\n"
        "Deposits offer a 2% interest rate.\n"
        "Though not as profitable as stocks or businesses, "
        "\nthey are a safe investment."
    ),

    "networth": (
        "Adviser:\n"
        "Net worth is crucial for personal expenses, bank approvals, "
        "\nand more:\n"
        "Net Worth = cash + deposits + (stocks*) + (business**) - credits.\n"
        " * Stocks: Considered at investment value, not market value.\n"
        " * Business: Valued at current business worth."
    ),

    "rest": (
        "Adviser:\n"
        "Resting restores 75pp of energy but cannot exceed 100pp.\n"
        "Jobs consume between 30pp and 60pp of energy."
    )
            

}