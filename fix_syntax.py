import re

file_path = '/Users/pablo/Documents/GitHub/forkcast-marketing/Forkcast-Adventure1/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# SCREENS array content was corrupted with unescaped quotes.
# I will replace the entire SCREENS block with a clean, correctly-double-quoted version.

fixed_screens = """    const SCREENS = [
      { // 0 Title
        type: 'story',
        text: "<h2 style=\\"font-size: 32px; font-weight: 600; line-height: 1.2; margin: 0;\\">What Foodsona are you?</h2>",
        scene: "<div class=\\"composed-emoji\\" style=\\"font-size: 7rem;\\">🥑</div>",
        btn: "Start",
        debugBtn: true
      },
      { // SCREEN 1
        type: 'story',
        text: "<p>You wake up in ForkVille. Stubby little arms. Vaguely delicious smell. No idea what you are.</p>",
        scene: "<img src=\\"assets/story/Story_1.png\\" class=\\"scene-img\\" alt=\\"ForkVille morning\\" />",
        btns: ["🌅 Look around slowly, take it all in.", "🏃 Start running. Figure it out later."]
      },
      { // SCREEN 2
        type: 'story',
        text: "<p>A Springles rolls past at full speed. \\"Food Festival TODAY. No Foodsona, no entry. Figure it out!\\"</p>",
        scene: "<img src=\\"assets/story/Story_2.png\\" class=\\"scene-img\\" alt=\\"Springles at the gate\\" />",
        btns: ["😤 \\"How hard can getting a Foodsona be.\\"", "🤔 \\"What is a Foodsona.\\""]
      },
      { // SCREEN 3 - Q1
        type: 'choice',
        qIdx: 0,
        text: "<p><strong>A Bokchoy in a high-vis vest blocks the gate. \\"No Foodsona, no entry. First question:\\"<br/><br/>How often do you cook at home?</strong></p>",
        scene: "<img src=\\"assets/story/Story_3.png\\" class=\\"scene-img\\" alt=\\"Bokchoy guard\\" />",
        answers: [
          { text: "🍳 Every day. It's my whole thing.", val: 10 },
          { text: "🥘 Most days — 4+ times a week.", val: 7 },
          { text: "🍜 A few times a week, maybe less.", val: 4 },
          { text: "🥡 Rarely. Other people exist for a reason.", val: 1 }
        ]
      },
      { // SCREEN 4
        type: 'story',
        text: "<p>She stamps \\"MYSTERY\\" on your badge and waves you through. Inside: total chaos. An Enoki Mushroom is balanced on a stack of cookbooks.</p>",
        scene: "<img src=\\"assets/story/Story_4.png\\" class=\\"scene-img\\" alt=\\"Enoki Mushroom on books\\" />",
        btns: ["👀 Head straight to the food stalls.", "🗺️ Look for a map. There has to be a map."]
      },
      { // SCREEN 5 - Q2
        type: 'choice',
        qIdx: 1,
        text: "<p><strong>A Heirloom Tomato sprints over. \\"Mystery Ingredient! Cook-Off team needs a fourth. Quick question first:\\"<br/><br/>How do you decide what to eat?</strong></p>",
        scene: "<img src=\\"assets/story/Story_5.png\\" class=\\"scene-img\\" alt=\\"Heirloom Tomato sprinting\\" />",
        answers: [
          { text: "📋 I plan meals in advance. I have a system.", val: 10 },
          { text: "🌅 I plan a day ahead — give me some notice.", val: 7 },
          { text: "☀️ I decide same day, vibe-based.", val: 4 },
          { text: "🤷 When I'm already hungry. It's fine.", val: 1 }
        ]
      },
      { // SCREEN 6
        type: 'story',
        text: "<p>\\"Perfect. You're exactly what we need.\\" You don't know what that means. She's already pulling you toward the arena.</p>",
        scene: "<img src=\\"assets/story/Story_6.png\\" class=\\"scene-img\\" alt=\\"Arena gates\\" />",
        btns: ["🏃 Try to keep up.", "😌 Let yourself be pulled. Surrender to it."]
      },
      { // SCREEN 7 - Q3
        type: 'choice',
        qIdx: 2,
        text: "<p><strong>Cook-Off theme drops: \\"A dish you've NEVER made before.\\" Avocado crumples their prep sheet. Your honest reaction?<br/><br/>Your approach to new recipes and cuisines?</strong></p>",
        scene: "<img src=\\"assets/story/Story_7.png\\" class=\\"scene-img\\" alt=\\"Cook-off kitchen\\" />",
        answers: [
          { text: "🌍 The stranger the better. I'm fully in.", val: 10 },
          { text: "🌱 Open to it with a quick Google first.", val: 7 },
          { text: "🏠 I prefer familiar meals. This is stressful.", val: 4 },
          { text: "⭐ I have 5 dishes I rotate. This is an attack.", val: 1 }
        ]
      },
      { // SCREEN 8
        type: 'story',
        text: "<p>A Strawberry knocks over the entire spice rack. The Springles team is on fire — on purpose apparently. 3 minutes left.</p>",
        scene: "<img src=\\"assets/story/Story_8.png\\" class=\\"scene-img\\" alt=\\"Kitchen chaos\\" />",
        btns: ["🔥 Power through. Plate it now.", "🤝 Ask a teammate for help."]
      },
      { // SCREEN 9 - Q4
        type: 'choice',
        qIdx: 3,
        text: "<p><strong>2 seconds to spare. The judges file in. A Broccoli, a Century Egg, a Truffle already crying. The Broccoli looks at your dish, then at you:<br/><br/>How important is it that food tastes incredible, even if it's unhealthy?</strong></p>",
        scene: "<img src=\\"assets/story/Story_9.png\\" class=\\"scene-img\\" alt=\\"Food judges\\" />",
        answers: [
          { text: "😋 Life is too short for sad meals.", val: 10 },
          { text: "❤️ Very — food should always bring joy.", val: 7 },
          { text: "⚖️ I try to find the balance.", val: 4 },
          { text: "🥦 Food is fuel. Enjoyment is secondary.", val: 1 }
        ]
      },
      { // SCREEN 10
        type: 'story',
        text: "<p>Truffle bursts into tears. Happy ones. The Century Egg writes something very long. The Broccoli nods once. \\"Walk with me.\\"</p>",
        scene: "<img src=\\"assets/story/Story_10.png\\" class=\\"scene-img\\" alt=\\"Truffle leading the way\\" />",
        btns: ["🚶 Walk alongside. Listen.", "👀 Try to peek at your scoresheet."]
      },
      { // SCREEN 11
        type: 'story',
        text: "<p>The Broccoli leads you to the ForkVille Night Market. Dogerry is doing impressions. A Cupcake looks like it's had a rough day.</p>",
        scene: "<img src=\\"assets/story/Story_11.png\\" class=\\"scene-img\\" alt=\\"Night market\\" />",
        btns: ["🍢 Get something to eat while you wait.", "🎭 Watch Dogerry's impressions."]
      },
      { // SCREEN 12
        type: 'story',
        text: "<p>A Morsel appears from nowhere and sits next to you. \\"You're the Mystery Ingredient, aren't you. I can always tell.\\" It does not elaborate.</p>",
        scene: "<img src=\\"assets/story/Story_12.png\\" class=\\"scene-img\\" alt=\\"Morsel on a bench\\" />",
        btns: ["😐 \\"…How can you tell.\\"", "🤝 \\"Yeah. Any idea what I am?\\""]
      },
      { // SCREEN 13 - Q5
        type: 'choice',
        qIdx: 4,
        text: "<p><strong>Morsel gestures at the whole market. Groups of food characters sharing plates. One Enoki mushroom alone on a bench eating, looking completely at peace.<br/><br/>Food is best when shared — or is it?</strong></p>",
        scene: "<img src=\\"assets/story/Story_13.png\\" class=\\"scene-img\\" alt=\\"Shared meal\\" />",
        answers: [
          { text: "👯 Always. A meal alone is a meal wasted.", val: 10 },
          { text: "🥂 Usually — depends on the mood.", val: 7 },
          { text: "🎧 Sometimes. I love a quiet solo meal too.", val: 4 },
          { text: "🧘 Honestly? I prefer eating alone. Less chaos.", val: 1 }
        ]
      },
      { // SCREEN 14
        type: 'story',
        text: "<p>Morsel nods like you've confirmed everything, then leaves without explaining. A Ketchup and Mayo is aggressively debating condiment philosophy with a Puff.</p>",
        scene: "<img src=\\"assets/story/Story_14.png\\" class=\\"scene-img\\" alt=\\"Night market chaos\\" />",
        btns: ["🧃 Get a drink. This has been a lot.", "👂 Listen to the condiment debate."]
      },
      { // SCREEN 15
        type: 'story',
        text: "<p>The Broccoli reappears. \\"One last stop.\\" It leads you into the ForkVille Test Kitchen — either immaculate or completely destroyed depending on who was in last.</p>",
        scene: "<img src=\\"assets/story/Story_15.png\\" class=\\"scene-img\\" alt=\\"Test kitchen\\" />",
        btns: ["🧹 Offer to help clean up.", "🔪 Pick up a knife. You feel at home here."]
      },
      { // SCREEN 16 - Q6
        type: 'choice',
        qIdx: 5,
        text: "<p><strong>The Broccoli leans against a counter and watches you take it in. \\"When you cook — what does your kitchen actually look like?\\"<br/><br/>What does your kitchen look like mid-cook?</strong></p>",
        scene: "<img src=\\"assets/story/Story_16.png\\" class=\\"scene-img\\" alt=\\"Kitchen state\\" />",
        answers: [
          { text: "📐 Prepped and organised before I even start.", val: 10 },
          { text: "🧽 Mostly tidy — I clean as I go.", val: 7 },
          { text: "🌀 Controlled chaos. I know where everything is.", val: 4 },
          { text: "💥 Absolute disaster zone. The food still slaps.", val: 1 }
        ]
      },
      { // SCREEN 17
        type: 'story',
        text: "<p>The Broccoli smiles for the first time. Back at the arena the results board is about to light up. The whole festival has gathered. Springles is near doing some wiring.</p>",
        scene: "<img src=\\"assets/story/Story_17.png\\" class=\\"scene-img\\" alt=\\"Results board assembly\\" />",
        btns: ["😬 \\"Someone should really stop Springles.\\"", "🍿 Watch from a safe distance."]
      },
      { // SCREEN 18
        type: 'story',
        text: "<p>A Dogerry starts a drumroll on an overturned pot. The Broccoli turns to you. \\"We've always known what you are. Ready?\\"",
        scene: "<img src=\\"assets/story/Story_18.png\\" class=\\"scene-img\\" alt=\\"Drumroll\\" />",
        btns: ["🫣 \\"...Kind of.\\"", "😤 \\"Yes. Tell me.\\""]
      },
      { // SCREEN 19
        type: 'story',
        text: "<p>The envelope tears open. The crowd goes silent. Even Springles stops.</p>",
        scene: "<img src=\\"assets/story/Story_19.png\\" class=\\"scene-img\\" alt=\\"The big reveal\\" />",
        btns: ["✨ \\"Who am I?\\""]
      },
      { // 20 RESULT
        type: 'result'
      }
    ];"""

start_marker = "const SCREENS = ["
end_marker = "    ];"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx) + len(end_marker)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + fixed_screens + content[end_idx:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success: Overwrote SCREENS array with fixed syntax.")
else:
    print(f"Error: Could not find markers.")
