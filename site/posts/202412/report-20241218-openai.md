---
date: '2024-12-18'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8144fb...MicrosoftDocs:aba0ab5
summary: 今回のコード変更では、GPT-4 Turboおよびビジョン対応モデルに関するドキュメントの大幅な更新が行われました。主な新機能として「ストレージ完了と蒸留」の詳細情報とサンプルコードが追加され、視覚的説明をサポートする画像も多数用意されています。既存文書に対する小規模な修正も行われ、情報の一貫性を保ちながらユーザーの理解を促進しています。特に新しいガイドラインや視覚資料は、ユーザーエクスペリエンスを向上させ、最新技術に直感的にアクセスできるように工夫されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8144fb...MicrosoftDocs:aba0ab5){target="_blank"}

<format>
# ハイライト

今回のコード変更で特筆すべき点は、GPT-4 Turboおよびビジョン対応モデルに関連するドキュメントの更新が幅広く行われたことです。主な新機能として、「Azure OpenAIサービスのストレージ完了と蒸留」の詳細情報を追加し、新しい機能が数多く導入されました。また、いくつかの既存文書に対して小規模な修正が行われ、情報の一貫性やユーザーの理解促進を図っています。さらに、ビジュアル要素の強化により、技術情報の伝達力を向上させています。

## 新機能
- 「ストレージ完了と蒸留」機能に関する詳細なドキュメントとサンプルコードの追加。
- ストレージ済みコンプリートの視覚的説明を助ける多数の画像ファイルの追加。

## 破壊的変更
- 特に破壊的変更はありませんが、既存の仕様や機能に関するいくつかの重要な更新が行われています。

## その他の更新
- ビジョン対応モデルに関する記述の修正とリンク表記の更新。
- モデルマトリックスに関する情報の明確化。
- 料金情報の正確性を高めるための記述の修正。

# 発見

この差分からは、Azure OpenAIサービスにおける最新の技術とドキュメントの管理に力を入れている様子が伺えます。特に、「ストレージ完了と蒸留」に関する新しいガイドラインとサンプルコードの追加は、多くの開発者に歓迎されるでしょう。これにより、チャットコンテンツを効率的に管理し、ファインチューニングに活用するための実践的な手法を提供しています。

また、新しく追加された視覚的資料は、技術ドキュメントにおける理解を促進すると共に、ユーザーがAzure OpenAIサービスの新機能を直感的に学べるように工夫されています。このようなビジュアル要素の導入は、特に複雑で抽象的な概念を持つAI技術に関して、ユーザーエクスペリエンスを向上させる上で重要です。

さらに、ビジョン対応モデルの表記を更新することで、より包括的なモデルの操作が可能となり、ユーザーが最新技術の恩恵を最大限に引き出せるようにするための明確な指針を示しています。標準チャット完了モデルのマトリックス情報の正確性が向上され、グローバルなユーザーに対しても透明性が高まっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [gpt-4-v-prompt-engineering.md](#item-fd7772) | minor update | 画像プロンプトエンジニアリング技術の更新 | modified | 16 | 16 | 32 | 
| [gpt-with-vision.md](#item-991388) | minor update | ビジョン対応のチャットモデルの概念に関する更新 | modified | 9 | 9 | 18 | 
| [models.md](#item-db2c37) | minor update | モデルに関する情報の更新 | modified | 5 | 3 | 8 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | ビジョン対応モデルを使用するためのクイックスタートの更新 | modified | 3 | 3 | 6 | 
| [fine-tuning.md](#item-5c0e85) | minor update | ファインチューニングに関する情報の更新 | modified | 20 | 2 | 22 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | ビジョン対応チャットモデルの使用に関するガイドの更新 | modified | 7 | 7 | 14 | 
| [prompt-caching.md](#item-1631df) | minor update | プロンプトキャッシングに関する情報の更新 | modified | 5 | 2 | 7 | 
| [stored-completions.md](#item-ccc7e6) | new feature | Azure OpenAIサービスのストレージ完了と蒸留の使用方法 | added | 188 | 0 | 188 | 
| [standard-chat-completions.md](#item-aae3f1) | minor update | 標準チャット完了モデルマトリックスの修正 | modified | 1 | 1 | 2 | 
| [standard-global.md](#item-17a84b) | minor update | 標準グローバルモデルマトリックスの更新 | modified | 25 | 25 | 50 | 
| [standard-models.md](#item-af04c4) | minor update | 標準モデルマトリックスの更新 | modified | 2 | 1 | 3 | 
| [index.yml](#item-0adb87) | minor update | ビジョン対応モデルの表記修正 | modified | 2 | 2 | 4 | 
| [global-standard.png](#item-356a25) | new feature | ファインチューニンググローバル標準画像の追加 | added | 0 | 0 | 0 | 
| [distill.png](#item-86c59e) | new feature | ストレージ済みコンプリート画像の追加 | added | 0 | 0 | 0 | 
| [evaluate.png](#item-ec8d98) | new feature | 評価画像の追加 | added | 0 | 0 | 0 | 
| [evaluation-data.png](#item-81f6bb) | new feature | 評価データ画像の追加 | added | 0 | 0 | 0 | 
| [file-name.png](#item-d013d6) | new feature | ファイル名画像の追加 | added | 0 | 0 | 0 | 
| [fine-tune.png](#item-b814bb) | new feature | ファインチューニング画像の追加 | added | 0 | 0 | 0 | 
| [permissions.png](#item-5f02c1) | new feature | パーミッション画像の追加 | added | 0 | 0 | 0 | 
| [stored-completions.png](#item-6b5634) | new feature | ストアドコンプリート画像の追加 | added | 0 | 0 | 0 | 
| [version.png](#item-1e76cf) | new feature | バージョン画像の追加 | added | 0 | 0 | 0 | 
| [overview.md](#item-97d507) | minor update | 料金情報の修正 | modified | 1 | 1 | 2 | 
| [realtime-audio-reference.md](#item-276d51) | minor update | リアルタイムオーディオリファレンスの改善 | modified | 69 | 53 | 122 | 
| [toc.yml](#item-c945af) | minor update | 目次の更新 | modified | 5 | 3 | 8 | 
| [whats-new.md](#item-53303b) | minor update | 新機能の追加と日付の更新 | modified | 13 | 1 | 14 | 


# Modified Contents
## articles/ai-services/openai/concepts/gpt-4-v-prompt-engineering.md{#item-fd7772}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
 title: Image prompt engineering techniques
 titleSuffix: Azure OpenAI
-description: Learn how to better engineer image prompts for GPT-4 Turbo with Vision.
+description: Learn how to better engineer image prompts for vision-enabled chat models.
 author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
@@ -12,7 +12,7 @@ manager: nitinme
 
 # Image prompt engineering techniques
 
-To unlock the full potential of GPT-4 Turbo with Vision, it's essential to tailor the prompts to your specific needs. Here are some guidelines to enhance the accuracy and efficiency of your prompts.
+To unlock the full potential of vision-enabled chat models like GPT-4 Turbo with Vision and GPT-4o, it's essential to tailor the prompts to your specific needs. Here are some guidelines to enhance the accuracy and efficiency of your prompts.
 
 ## Fundamentals of crafting your image prompt
 - **Contextual specificity:** Adding context to the scenario at hand gives the model a better understanding of an appropriate output. This level of specificity aids in focusing on relevant aspects and avoiding extraneous details.
@@ -28,57 +28,57 @@ To unlock the full potential of GPT-4 Turbo with Vision, it's essential to tailo
 - **Define output format:** Clearly mention the desired format for the output, such as markdown, JSON, HTML, etc. You can also suggest a specific structure, length, or specific attributes about the response.
 
 ## Example prompt inputs & outputs
-There are many ways to craft system prompts to tailor the output specifically to your needs. The following sample inputs and outputs showcase how adjusting your prompts can give you different results. Try the model out for yourself using these images and adjusting the system prompt in the [Azure AI Foundry playground](https://ai.azure.com/).
+There are many ways to craft system prompts to tailor the output specifically to your needs. The following sample inputs and outputs showcase how adjusting your prompts can give you different results. Try out the model for yourself using these images and adjusting the system prompt in the [Azure AI Foundry playground](https://ai.azure.com/).
 
 ### Contextual specificity  
-Context can help improve feedback from the model. For example, if you're working on image descriptions for a product catalog, ensure your prompt reflects this in a clear and concise way. A prompt like “Describe images for an outdoor hiking product catalog, focusing on enthusiasm and professionalism” guides the model to generate responses that are both accurate and contextually rich.
+Context can help improve feedback from the model. For example, if you're working on image descriptions for a product catalog, ensure your prompt reflects that in a clear and concise way. A prompt like “Describe images for an outdoor hiking product catalog, focusing on enthusiasm and professionalism” guides the model to generate responses that are both accurate and contextually rich.
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/tent-chairs.jpg" lightbox="../media/concepts/gpt-v/tent-chairs.jpg" alt-text="Photograph of a camping tent and chairs in a forest."::: What is in this image? | The image shows a camping setup in a forest area. There is a yellow tent, two folding camping chairs—one red and one blue—and a portable camping table. The surrounding area is densely populated with trees, indicating that the campsite is in a wooded region. |
+| :::image type="content" source="../media/concepts/gpt-v/tent-chairs.jpg" lightbox="../media/concepts/gpt-v/tent-chairs.jpg" alt-text="Photograph of a camping tent and chairs in a forest."::: What is in this image? | `The image shows a camping setup in a forest area. There is a yellow tent, two folding camping chairs—one red and one blue—and a portable camping table. The surrounding area is densely populated with trees, indicating that the campsite is in a wooded region.` |
 
 |Updated prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/tent-chairs.jpg" lightbox="../media/concepts/gpt-v/tent-chairs.jpg" alt-text="Photograph of a camping tent and chairs in a forest."::: Describe images for an outdoor hiking product catalog, focusing on enthusiasm and professionalism. | "Embark on your next outdoor adventure with our premium hiking and camping essentials! Featured here is our vibrant, spacious tent, designed to be your home away from home amidst the serenity of nature. Crafted with top-notch materials, it promises durability and comfort in any weather. Complementing the tent are our ultra-comfortable, lightweight folding chairs, available in eye-catching red and serene blue, perfect for those moments of relaxation after a day of exploration. Don't forget our sturdy, portable table, ideal for a delightful outdoor meal or a game of cards under the stars. Elevate your camping experience with our reliable products, where quality meets the great outdoors!" |
+| :::image type="content" source="../media/concepts/gpt-v/tent-chairs.jpg" lightbox="../media/concepts/gpt-v/tent-chairs.jpg" alt-text="Photograph of a camping tent and chairs in a forest."::: Describe images for an outdoor hiking product catalog, focusing on enthusiasm and professionalism. | `"Embark on your next outdoor adventure with our premium hiking and camping essentials! Featured here is our vibrant, spacious tent, designed to be your home away from home amidst the serenity of nature. Crafted with top-notch materials, it promises durability and comfort in any weather. Complementing the tent are our ultra-comfortable, lightweight folding chairs, available in eye-catching red and serene blue, perfect for those moments of relaxation after a day of exploration. Don't forget our sturdy, portable table, ideal for a delightful outdoor meal or a game of cards under the stars. Elevate your camping experience with our reliable products, where quality meets the great outdoors!"` |
 
 
 ### Task-oriented prompts
 Giving the model a specific task to follow is one way of sharpening the response. In this example, this prompt steers the model to concentrate on elements crucial for insurance assessments, thereby improving accuracy and relevancy.
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/car-crash.jpg" lightbox="../media/concepts/gpt-v/car-crash.jpg" alt-text="Photograph of a car crashed into a pole."::: What is in this image? | The image shows a silver sedan that has been in an accident. The front end of the car is damaged, with the hood crumpled, and the bumper partially detached. The car is resting against a utility pole on the sidewalk, and there is visible smoke coming from the engine area, indicating a recent crash. The setting appears to be a residential street, as indicated by the presence of houses in the background, a neatly trimmed hedge, and a sidewalk. |
+| :::image type="content" source="../media/concepts/gpt-v/car-crash.jpg" lightbox="../media/concepts/gpt-v/car-crash.jpg" alt-text="Photograph of a car crashed into a pole."::: What is in this image? | `The image shows a silver sedan that has been in an accident. The front end of the car is damaged, with the hood crumpled, and the bumper partially detached. The car is resting against a utility pole on the sidewalk, and there is visible smoke coming from the engine area, indicating a recent crash. The setting appears to be a residential street, as indicated by the presence of houses in the background, a neatly trimmed hedge, and a sidewalk.` |
 
 |Updated prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/car-crash.jpg" lightbox="../media/concepts/gpt-v/car-crash.jpg" alt-text="Photograph of a car crashed into a pole."::: Analyze this car damage video for an auto insurance report, focusing on identifying and detailing damage | In the image provided, we observe a silver sedan that has sustained significant front-end damage. The vehicle's hood is notably crumpled, and the front bumper has suffered substantial deformation, partially detaching from the chassis. The right headlamp assembly appears to be damaged or dislodged. There is also visible damage to the front grille area. The car is in contact with a utility pole, suggesting a frontal collision with the pole at a relatively low or moderate speed. Smoke is emanating from the engine compartment, suggesting potential mechanical or electrical damage that may need further inspection for a comprehensive assessment. The airbags do not appear to be deployed in this image. The vehicle will require a detailed inspection to evaluate the full extent of structural and mechanical damage for a complete insurance report. |
+| :::image type="content" source="../media/concepts/gpt-v/car-crash.jpg" lightbox="../media/concepts/gpt-v/car-crash.jpg" alt-text="Photograph of a car crashed into a pole."::: Analyze this car damage video for an auto insurance report, focusing on identifying and detailing damage | `In the image provided, we observe a silver sedan that has sustained significant front-end damage. The vehicle's hood is notably crumpled, and the front bumper has suffered substantial deformation, partially detaching from the chassis. The right headlamp assembly appears to be damaged or dislodged. There is also visible damage to the front grille area. The car is in contact with a utility pole, suggesting a frontal collision with the pole at a relatively low or moderate speed. Smoke is emanating from the engine compartment, suggesting potential mechanical or electrical damage that may need further inspection for a comprehensive assessment. The airbags do not appear to be deployed in this image. The vehicle will require a detailed inspection to evaluate the full extent of structural and mechanical damage for a complete insurance report.` |
 
 ### Handling refusals
 When you receive a refusal output from a model, there are several ways you can tweak input to generate a more appropriate response. Below is one example of how to handle a refusal and progress. 
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/dinner-spread.jpg" lightbox="../media/concepts/gpt-v/dinner-spread.jpg" alt-text="Photograph of a dinner table with several plates of food."::: Plan this meal | Sorry, I can't provide that information. |
+| :::image type="content" source="../media/concepts/gpt-v/dinner-spread.jpg" lightbox="../media/concepts/gpt-v/dinner-spread.jpg" alt-text="Photograph of a dinner table with several plates of food."::: Plan this meal | `Sorry, I can't provide that information.` |
 
 |Follow up prompt|Model output|
 |--------|-----------|
-| What information do you need? | I apologize for the confusion earlier. To plan a meal based on the image provided, I would need to know the following: <br> The number of people dining to ensure there's enough food for everyone.<br>Any dietary restrictions or preferences to accommodate (e.g., vegetarian, gluten-free, allergies).<br>The occasion or type of meal being planned (e.g., casual lunch, dinner party).<br>Desired balance of the meal in terms of food groups and nutrition. <br>With this information, I could help suggest how to portion the dishes, create a balanced meal, and ensure the meal meets the needs of all diners.|
+| What information do you need? | `I apologize for the confusion earlier. To plan a meal based on the image provided, I would need to know the following: <br> The number of people dining to ensure there's enough food for everyone.<br>Any dietary restrictions or preferences to accommodate (e.g., vegetarian, gluten-free, allergies).<br>The occasion or type of meal being planned (e.g., casual lunch, dinner party).<br>Desired balance of the meal in terms of food groups and nutrition. <br>With this information, I could help suggest how to portion the dishes, create a balanced meal, and ensure the meal meets the needs of all diners.`|
 
 ### Adding examples
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: What is this dog breed and what is its average weight and height? | The dog in the image appears to be a Border Collie. Border Collies are known for their intelligence, agility, and herding abilities.The average weight for a Border Collie is typically around 30-45 pounds (14-20 kilograms). As for height, Border Collies generally stand about 18-22 inches (46-56 centimeters) tall at the shoulder. These figures can vary based on the individual dog's genetics, diet, and level of activity. Border Collies are medium-sized dogs with a well-proportioned body and a high level of energy. |
+| :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: What is this dog breed and what is its average weight and height? | `The dog in the image appears to be a Border Collie. Border Collies are known for their intelligence, agility, and herding abilities.The average weight for a Border Collie is typically around 30-45 pounds (14-20 kilograms). As for height, Border Collies generally stand about 18-22 inches (46-56 centimeters) tall at the shoulder. These figures can vary based on the individual dog's genetics, diet, and level of activity. Border Collies are medium-sized dogs with a well-proportioned body and a high level of energy.` |
 
 |Updated prompt|Model output|
 |--------|-----------|
-| Q: What is this dog breed and what is its average weight & height? :::image type="content" source="../media/concepts/gpt-v/pomeranian.jpg" lightbox="../media/concepts/gpt-v/pomeranian.jpg" alt-text="Photograph of a pomeranian dog sitting on a pool diving board above the water."::: <br> A: Breed: pomeranian; average weight: 3-7 lbs; average height: 8-14 inches <br> :::image type="content" source="../media/concepts/gpt-v/bulldog.jpg" lightbox="../media/concepts/gpt-v/bulldog.jpg" alt-text="Photograph of a bulldog laying in a grass field."::: A: Breed: English bulldog; average weight: 50-55 lbs; average height: 14-16 inches :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: | A: Breed: Border Collie; average weight: 30-45 lbs; average height: 18-22 inches |
+| Q: What is this dog breed and what is its average weight & height? :::image type="content" source="../media/concepts/gpt-v/pomeranian.jpg" lightbox="../media/concepts/gpt-v/pomeranian.jpg" alt-text="Photograph of a pomeranian dog sitting on a pool diving board above the water."::: <br> A: Breed: pomeranian; average weight: 3-7 lbs; average height: 8-14 inches <br> :::image type="content" source="../media/concepts/gpt-v/bulldog.jpg" lightbox="../media/concepts/gpt-v/bulldog.jpg" alt-text="Photograph of a bulldog laying in a grass field."::: A: Breed: English bulldog; average weight: 50-55 lbs; average height: 14-16 inches :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: | `A: Breed: Border Collie; average weight: 30-45 lbs; average height: 18-22 inches` |
 
 ### Break down requests
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/grandmas-recipe.jpg" lightbox="../media/concepts/gpt-v/grandmas-recipe.jpg" alt-text="Photograph of a recipe card detailing a recipe for Grandma's Apple Crumb Pie."::: What's in this image? | The image contains a recipe card titled Grandma's Apple Crumb Pie. It is noted as a Thanksgiving tradition. The ingredients listed are:<br><ul><li>5-7 apples, peeled </li> <li>1 9-inch pie crust</li> <li>	3/4 cups sugar </li> <li>1/2 teaspoon cinnamon </li> <li>A dash of salt </li><li>	3 tablespoons butter</li> </ul><br>Please note that the measurements for sugar, flour, and butter are not fully visible in the image. If needed, the standard measures for a crumb topping typically involve a combination of sugar, flour, and butter mixed together until crumbly|
+| :::image type="content" source="../media/concepts/gpt-v/grandmas-recipe.jpg" lightbox="../media/concepts/gpt-v/grandmas-recipe.jpg" alt-text="Photograph of a recipe card detailing a recipe for Grandma's Apple Crumb Pie."::: What's in this image? | `The image contains a recipe card titled Grandma's Apple Crumb Pie. It is noted as a Thanksgiving tradition. The ingredients listed are:<br><ul><li>5-7 apples, peeled </li> <li>1 9-inch pie crust</li> <li>	3/4 cups sugar </li> <li>1/2 teaspoon cinnamon </li> <li>A dash of salt </li><li>	3 tablespoons butter</li> </ul><br>Please note that the measurements for sugar, flour, and butter are not fully visible in the image. If needed, the standard measures for a crumb topping typically involve a combination of sugar, flour, and butter mixed together until crumbly`|
 
 |Updated prompt|Model output|
 |----------|-----------|
@@ -88,11 +88,11 @@ When you receive a refusal output from a model, there are several ways you can t
 
 |Basic prompt|Model output|
 |----------|-----------|
-|:::image type="content" source="../media/concepts/gpt-v/rental-listing.jpg" lightbox="../media/concepts/gpt-v/rental-listing.jpg" alt-text="Photograph of a white villa in a tropical region with a pool."::: Describe this image | The image shows a luxurious white villa with a traditional thatched roof on one section and a clear blue swimming pool in the foreground. There are sun loungers lined up along the poolside, inviting relaxation. The architecture includes elegant archways, a balcony with wooden railings, and large windows and doors that suggest a bright and airy interior. The villa is surrounded by lush tropical vegetation, including tall palm trees, which adds to the serene and exotic ambiance of the setting. |
+|:::image type="content" source="../media/concepts/gpt-v/rental-listing.jpg" lightbox="../media/concepts/gpt-v/rental-listing.jpg" alt-text="Photograph of a white villa in a tropical region with a pool."::: Describe this image | `The image shows a luxurious white villa with a traditional thatched roof on one section and a clear blue swimming pool in the foreground. There are sun loungers lined up along the poolside, inviting relaxation. The architecture includes elegant archways, a balcony with wooden railings, and large windows and doors that suggest a bright and airy interior. The villa is surrounded by lush tropical vegetation, including tall palm trees, which adds to the serene and exotic ambiance of the setting.` |
 
 |Updated prompt|Model output|
 |----------|-----------|
-|:::image type="content" source="../media/concepts/gpt-v/rental-listing.jpg" lightbox="../media/concepts/gpt-v/rental-listing.jpg" alt-text="Photograph of a white villa in a tropical region with a pool."::: You are an AI assistant that writes detailed listings for vacation rental properties. Summarize in three sentences the optimal features of the listing, based on only what is visible in the image. Conclude with one sentence on why the customer should book today. | This idyllic villa showcases an inviting private pool with steps for easy access, framed by a beautifully tiled sun deck and comfortable loungers ideal for soaking up the sun or enjoying a good book under the shade of tropical palms. Architectural charm is evident in the villa's design, featuring elegant archways, a thatched-roof gazebo, and balconies that promise serene views and a perfect spot to savor your morning or evening beverages. The lush greenery surrounding the property not only provides privacy but also enhances the sense of an exclusive paradise retreat. Don't miss the opportunity to secure this perfect blend of luxury and tranquility – book today for a tropical escape like no other! |
+|:::image type="content" source="../media/concepts/gpt-v/rental-listing.jpg" lightbox="../media/concepts/gpt-v/rental-listing.jpg" alt-text="Photograph of a white villa in a tropical region with a pool."::: You are an AI assistant that writes detailed listings for vacation rental properties. Summarize in three sentences the optimal features of the listing, based on only what is visible in the image. Conclude with one sentence on why the customer should book today. | `This idyllic villa showcases an inviting private pool with steps for easy access, framed by a beautifully tiled sun deck and comfortable loungers ideal for soaking up the sun or enjoying a good book under the shade of tropical palms. Architectural charm is evident in the villa's design, featuring elegant archways, a thatched-roof gazebo, and balconies that promise serene views and a perfect spot to savor your morning or evening beverages. The lush greenery surrounding the property not only provides privacy but also enhances the sense of an exclusive paradise retreat. Don't miss the opportunity to secure this perfect blend of luxury and tranquility – book today for a tropical escape like no other!` |
 
 
-These guidelines and examples demonstrate how tailored system prompts can significantly enhance the performance of GPT-4 Turbo with Vision, ensuring that the responses are not only accurate but also perfectly suited to the specific context of the task at hand.
+These guidelines and examples demonstrate how tailored system prompts can significantly enhance the performance of vision-enabled models, ensuring that the responses are not only accurate but also perfectly suited to the specific context of the task at hand.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "画像プロンプトエンジニアリング技術の更新"
}
```

### Explanation
このコードの変更は、GPT-4 Turboおよびビジョン機能を持つチャットモデルに関連したドキュメントの内容を更新しています。主に説明文や具体的な画像プロンプトの例が変更され、より一般的なビジョン対応モデルに対応した内容になっています。特に、モデルの名称を「GPT-4 Turbo with Vision」から「ビジョン対応のチャットモデル」に変更し、いくつかのプロンプトのサンプルにおいてフォーマットや表現を改善しています。これにより、ユーザーがプロンプトエンジニアリングの際に得られる理解や精度が向上することを意図しています。全体として、ドキュメントは、ビジョン機能を持つ新しいモデルに関連する技術的な課題に対処するためのガイドラインを提供しています。

## articles/ai-services/openai/concepts/gpt-with-vision.md{#item-991388}

<details>
<summary>Diff</summary>
````diff
@@ -1,5 +1,5 @@
 ---
-title: GPT-4 Turbo with Vision concepts
+title: Vision-enabled chat model concepts
 titleSuffix: Azure OpenAI
 description: Learn concepts related to using images in your AI model chats, enabled through GPT-4 Turbo with Vision and other models.
 author: PatrickFarley
@@ -10,23 +10,23 @@ ms.date: 09/24/2024
 manager: nitinme
 ---
 
-# GPT-4 Turbo with Vision concepts
+# Vision-enabled chat model concepts
 
-GPT-4 Turbo with Vision is a large multimodal model (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. It incorporates both natural language processing and visual understanding. This guide provides details on the capabilities and limitations of GPT-4 Turbo with Vision.
+Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are GPT-4 Turbo with Vision, GPT-4o, and GPT-4o-mini. This guide provides details on their capabilities and limitations.
 
-To try out GPT-4 Turbo with Vision, see the [quickstart](/azure/ai-services/openai/gpt-v-quickstart).
+To try out vision-enabled chat models, see the [quickstart](/azure/ai-services/openai/gpt-v-quickstart).
 
-## Chats with vision
+## Vision-enabled chats
 
-The GPT-4 Turbo with Vision model answers general questions about what's present in the images or videos you upload.
+The vision-enabled models answer general questions about what's present in the images or videos you upload.
 
 
 ## Special pricing information
 
 > [!IMPORTANT]
 > Pricing details are subject to change in the future.
 
-GPT-4 Turbo with Vision accrues charges like other Azure OpenAI chat models. You pay a per-token rate for the prompts and completions, detailed on the [Pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). The base charges and additional features are outlined here:
+Vision-enabled models accrue charges like other Azure OpenAI chat models. You pay a per-token rate for the prompts and completions, detailed on the [Pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/). The base charges and additional features are outlined here:
 
 Base Pricing for GPT-4 Turbo with Vision is:
 - Input: $0.01 per 1000 tokens
@@ -71,7 +71,7 @@ Additionally, there's a one-time indexing cost of $0.15 to generate the Video Re
 
 ## Input limitations
 
-This section describes the limitations of GPT-4 Turbo with Vision.
+This section describes the limitations of vision-enabled chat models.
 
 ### Image support
 
@@ -89,6 +89,6 @@ This section describes the limitations of GPT-4 Turbo with Vision.
 
 ## Next steps
 
-- Get started using GPT-4 Turbo with Vision by following the [quickstart](/azure/ai-services/openai/gpt-v-quickstart).
+- Get started using vision-enabled models by following the [quickstart](/azure/ai-services/openai/gpt-v-quickstart).
 - For a more in-depth look at the APIs, and to use video prompts in chat, follow the [how-to guide](../how-to/gpt-with-vision.md).
 - See the [completions and embeddings API reference](../reference.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジョン対応のチャットモデルの概念に関する更新"
}
```

### Explanation
このコードの変更は、「GPT-4 Turbo with Vision」関連のドキュメントを「ビジョン対応のチャットモデル」というより広範な表現に変更することを中心に行われています。具体的には、モデル名だけでなく、文中のいくつかのフレーズが、現在のビジョン対応モデルの特性をより正確に反映するように修正されています。

変更点には、モデルの名称の更新や、複数のモデル（GPT-4o、GPT-4o-miniを含む）の言及が含まれています。また、ドキュメント全体がこれらのモデルの機能や制限についても触れており、特定の機能や料金に関する情報が明確に整理されています。これにより、ユーザーがビジョン機能を持つモデルに関する理解を深めやすくなっています。全体として、内容の一貫性と明確さが向上しています。

## articles/ai-services/openai/concepts/models.md{#item-db2c37}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the different model capabilities that are available with Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 12/05/2024
+ms.date: 12/16/2024
 ms.custom: references_regions, build-2023, build-2023-dataai, refefences_regions
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
@@ -249,8 +249,9 @@ You need to [create](../how-to/create-resource.md) or use an existing resource i
 
 When your resource is created, you can [deploy](../how-to/create-resource.md#deploy-a-model) the GPT-4o models. If you are performing a programmatic deployment, the **model** names are:
 
+- `gpt-4o` **Version** `2024-11-20`
 - `gpt-4o` **Version** `2024-08-06`
-- `gpt-4o`, **Version**  `2024-05-13`
+- `gpt-4o` **Version** `2024-05-13`
 - `gpt-4o-mini` **Version** `2024-07-18`
 
 ### GPT-4 Turbo
@@ -277,7 +278,8 @@ See [model versions](../concepts/model-versions.md) to learn about how Azure Ope
 
 |  Model ID  | Description | Max Request (tokens) | Training Data (up to)  |
 |  --- |  :--- |:--- |:---: |
-|`gpt-4o` (2024-08-06) <br> **GPT-4o (Omni)** | **Latest large GA model** <br> - Structured outputs<br> - Text, image processing <br> - JSON Mode <br> - parallel function calling <br> - Enhanced accuracy and responsiveness <br> - Parity with English text and coding tasks compared to GPT-4 Turbo with Vision <br> - Superior performance in non-English languages and in vision tasks |Input: 128,000  <br> Output: 16,384 | Oct 2023 |
+| `gpt-4o` (2024-11-20) <br> **GPT-4o (Omni)**  | **Latest large GA model** <br> - Structured outputs<br> - Text, image processing <br> - JSON Mode <br> - parallel function calling <br> - Enhanced accuracy and responsiveness <br> - Parity with English text and coding tasks compared to GPT-4 Turbo with Vision <br> - Superior performance in non-English languages and in vision tasks. <br> - **Enhanced creative writing ability** | Input: 128,000  <br> Output: 16,384 | Oct 2023 |
+|`gpt-4o` (2024-08-06) <br> **GPT-4o (Omni)** | - Structured outputs<br> - Text, image processing <br> - JSON Mode <br> - parallel function calling <br> - Enhanced accuracy and responsiveness <br> - Parity with English text and coding tasks compared to GPT-4 Turbo with Vision <br> - Superior performance in non-English languages and in vision tasks |Input: 128,000  <br> Output: 16,384 | Oct 2023 |
 |`gpt-4o-mini` (2024-07-18) <br> **GPT-4o mini** | **Latest small GA model** <br> - Fast, inexpensive, capable model ideal for replacing GPT-3.5 Turbo series models. <br> - Text, image processing <br>- JSON Mode <br> - parallel function calling | Input: 128,000 <br> Output: 16,384  | Oct 2023 |
 |`gpt-4o` (2024-05-13) <br> **GPT-4o (Omni)** | Text, image processing <br> - JSON Mode <br> - parallel function calling <br> - Enhanced accuracy and responsiveness <br> - Parity with English text and coding tasks compared to GPT-4 Turbo with Vision <br> - Superior performance in non-English languages and in vision tasks |Input: 128,000  <br> Output: 4,096| Oct 2023 |
 | `gpt-4` (turbo-2024-04-09) <br>**GPT-4 Turbo with Vision** | **New GA model** <br> - Replacement for all previous GPT-4 preview models (`vision-preview`, `1106-Preview`, `0125-Preview`). <br> - [**Feature availability**](#gpt-4o-and-gpt-4-turbo) is currently different depending on method of input, and deployment type. | Input: 128,000  <br> Output: 4,096  | Dec 2023 |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関連するモデル情報を更新する内容です。具体的には、モデルのバージョンや説明が新しい情報に合わせて修正されています。主な変更点には、GPT-4oモデルの新しいバージョン（2024-11-20）が追加され、これに「強化された創造的なライティング能力」という新たな特徴が加わりました。また、古いバージョン（2024-08-06）に関する表記が整理され、記載内容が最新のものと一致するように改訂されています。

加えて、更新日（ms.date）が12月5日から12月16日に変更され、情報が正確であることが強調されています。全体として、これらの変更は、ユーザーに提供される情報をより明確にし、最新のモデルの機能を際立たせることを目的としています。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the Azure OpenAI Service'
+title: 'Quickstart: Use vision-enabled models with the Azure OpenAI Service'
 titleSuffix: Azure OpenAI
-description: Use this article to get started using Azure OpenAI to deploy and use the GPT-4 Turbo with Vision model. 
+description: Use this article to get started using Azure OpenAI to deploy and use the GPT-4 Turbo with Vision model or other vision-enabled models. 
 services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
@@ -60,6 +60,6 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
 ## Next steps
 
-* Learn more about these APIs in the [GPT-4 Turbo with Vision how-to guide](./gpt-v-quickstart.md)
+* Learn more about these APIs in the [Vision-enabled models how-to guide](./gpt-v-quickstart.md)
 * [GPT-4 Turbo with Vision frequently asked questions](./faq.yml#gpt-4-turbo-with-vision)
 * [GPT-4 Turbo with Vision API reference](https://aka.ms/gpt-v-api-ref)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジョン対応モデルを使用するためのクイックスタートの更新"
}
```

### Explanation
このコード変更は、Azure OpenAIサービスを利用したビジョン対応モデルの使用に関するクイックスタートガイドを更新する内容です。主な変更点として、タイトルが「GPT-4 Turbo with Vision」から「ビジョン対応モデル」に変更され、より広範な内容をカバーすることを示しています。また、説明文の一部も修正され、ユーザーはGPT-4 Turbo with Visionモデルやその他のビジョン対応モデルをデプロイおよび使用する方法を学ぶことができるようになっています。

さらに、次のステップのセクションでは、関連するガイドへのリンクも更新され、「GPT-4 Turbo with Vision」から「ビジョン対応モデル」に表現が変更されています。これにより、ユーザーは異なるビジョンモデルに関する情報をよりスムーズに得ることができるよう改善されています。全体として、今回の変更はユーザーに対する明確さと情報の網羅性を向上させることを目的としています。

## articles/ai-services/openai/how-to/fine-tuning.md{#item-5c0e85}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,9 @@ description: Learn how to create your own customized model with Azure OpenAI Ser
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: build-2023, build-2023-dataai, devx-track-python
+ms.custom: build-2023, build-2023-dataai, devx-track-python, references_regions
 ms.topic: how-to
-ms.date: 11/11/2024
+ms.date: 12/13/2024
 author: mrbullwinkle
 ms.author: mbullwin
 zone_pivot_groups: openai-fine-tuning
@@ -44,6 +44,20 @@ We use LoRA, or low rank approximation, to fine-tune models in a way that reduce
 
 ::: zone-end
 
+## Global Standard
+
+Azure OpenAI fine-tuning supports [global standard deployments](./deployment-types.md#global-standard) in East US2, North Central US, and Sweden Central for:
+
+- `gpt-4o-2024-08-06`
+- `gpt-4o-mini-2024-07-18`
+
+Global standard fine-tuned deployments offer [cost savings](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/), but custom model weights may temporarily be stored outside the geography of your Azure OpenAI resource.
+
+:::image type="content" source="../media/fine-tuning/global-standard.png" alt-text="Screenshot of the global standard deployment user experience with a fine-tuned model." lightbox="../media/fine-tuning/global-standard.png":::
+
+Global Standard fine-tuning deployments currently do not support vision and structured outputs.
+
+
 ## Vision fine-tuning
 
 Fine-tuning is also possible with images in your JSONL files. Just as you can send one or many image inputs to chat completions, you can include those same message types within your training data. Images can be provided either as publicly accessible URLs or data URIs containing [base64 encoded images](/azure/ai-services/openai/how-to/gpt-with-vision?tabs=rest#call-the-chat-completion-apis). 
@@ -79,6 +93,10 @@ Images containing the following will be excluded from your dataset and not used
 > [!IMPORTANT]
 >For  vision fine tuning face screening process: We screen for faces/people to skip those images from training the model. The screening capability leverages face detection **WITHOUT** Face identification which means we don't create facial templates or measure specific facial geometry, and the technology used to screen for faces is incapable of uniquely identifying the individuals. To know more about data and Privacy for face refer to - [Data and privacy for Face - Azure AI services | Microsoft Learn](/legal/cognitive-services/computer-vision/imageanalysis-data-privacy-security?context=%2Fazure%2Fai-services%2Fcomputer-vision%2Fcontext%2Fcontext).
 
+## Prompt caching
+
+Azure OpenAI fine-tuning supports prompt caching with select models. Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. To learn more about prompt caching, see [getting started with prompt caching](./prompt-caching.md).
+
 ## Troubleshooting
 
 ### How do I enable fine-tuning?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるファインチューニングの方法に関するドキュメントを更新するものです。主要な変更点には、新たに「グローバルスタンダード」セクションが追加され、特定の地域（East US2、North Central US、Sweden Central）でのファインチューニングのサポートが明記されています。このセクションでは、対応するモデルやコスト削減の可能性についても言及されています。

加えて、ファインチューニングにおけるプロンプトキャッシングに関する情報も新たに加わり、特定のモデルでのプロンプトキャッシングがリクエストのレイテンシおよびコストを低減できることが説明されています。さらに、日付情報（ms.date）が11月11日から12月13日に更新され、最新の情報が反映されています。

全体的に見て、これらの変更はファインチューニングのプロセスをより明確にし、ユーザーにとっての利便性や理解を深めることを目的としています。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -1,7 +1,7 @@
 ---
-title: How to use the GPT-4 Turbo with Vision model
+title: How to use vision-enabled chat models
 titleSuffix: Azure OpenAI Service
-description: Learn about the options for using GPT-4 Turbo with Vision
+description: Learn about the options for using vision-enabled chat models
 author: PatrickFarley #dereklegenzoff
 ms.author: pafarley #delegenz
 ms.service: azure-ai-openai
@@ -10,15 +10,15 @@ ms.date: 08/21/2024
 manager: nitinme
 ---
 
-# Use GPT-4 Turbo with Vision
+# Use vision-enabled chat models
 
 
-GPT-4 Turbo with Vision is a large multimodal model (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. It incorporates both natural language processing and visual understanding.
+Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are GPT-4 Turbo with Vision, GPT-4o, and GPT-4o-mini.
 
-The GPT-4 Turbo with Vision model answers general questions about what's present in images.
+The vision-enabled models answer general questions about what's present in the images or videos you upload.
 
 > [!TIP]
-> To use GPT-4 Turbo with Vision, you call the Chat Completion API on a GPT-4 Turbo with Vision model that you have deployed. If you're not familiar with the Chat Completion API, see the [GPT-4 Turbo & GPT-4 how-to guide](/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions).
+> To use vision-enabled models, you call the Chat Completion API on a supported model that you have deployed. If you're not familiar with the Chat Completion API, see the [Vision-enabled chat how-to guide](/azure/ai-services/openai/how-to/chatgpt?tabs=python&pivots=programming-language-chat-completions).
 
 ## GPT-4 Turbo model upgrade
 
@@ -371,6 +371,6 @@ Every response includes a `"finish_reason"` field. It has the following possible
 ## Next steps
 
 * [Learn more about Azure OpenAI](../overview.md).
-* [GPT-4 Turbo with Vision quickstart](../gpt-v-quickstart.md)
+* [Vision-enabled chats quickstart](../gpt-v-quickstart.md)
 * [GPT-4 Turbo with Vision frequently asked questions](../faq.yml#gpt-4-turbo-with-vision)
 * [GPT-4 Turbo with Vision API reference](https://aka.ms/gpt-v-api-ref)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジョン対応チャットモデルの使用に関するガイドの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるビジョン対応チャットモデルの使用方法に関するドキュメントを更新するものです。主な変更点として、ドキュメントのタイトルと説明文が変更され、特定のモデル（GPT-4 Turbo with Vision）から「ビジョン対応チャットモデル」というより広範な表現に改められています。これにより、ユーザーは複数のビジョン対応モデル（GPT-4 Turbo with Vision、GPT-4o、およびGPT-4o-mini）に触れることができ、情報がより包括的になります。

また、使用方法についての説明も改善され、具体的には、ユーザーが「ビジョン対応モデル」を利用する際のAPI呼び出しに関する記述が明確化されています。最後に、次のステップのリンクも更新され、ユーザーが最新の情報にアクセスできるよう配慮されています。

全体として、これらの変更は、ドキュメントの内容を分かりやすくし、最新の情報を提供することを目的としています。

## articles/ai-services/openai/how-to/prompt-caching.md{#item-1631df}

<details>
<summary>Diff</summary>
````diff
@@ -6,15 +6,15 @@ services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 10/18/2024
+ms.date: 12/15/2024
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
 ---
 
 # Prompt caching
 
-Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. *"Prompt"* in this context is referring to the input you send to the model as part of your chat completions request. Rather than reprocess the same input tokens over and over again, the service is able to retain a temporary cache of processed input token computations to improve overall performance. Prompt caching has no impact on the output content returned in the model response beyond a reduction in latency and cost. For supported models, cached tokens are billed at a [50% discount on input token pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for Standard deployment types and up to [100% discount on input tokens](/azure/ai-services/openai/concepts/provisioned-throughput) for Provisioned deployment types. 
+Prompt caching allows you to reduce overall request latency and cost for longer prompts that have identical content at the beginning of the prompt. *"Prompt"* in this context is referring to the input you send to the model as part of your chat completions request. Rather than reprocess the same input tokens over and over again, the service is able to retain a temporary cache of processed input token computations to improve overall performance. Prompt caching has no impact on the output content returned in the model response beyond a reduction in latency and cost. For supported models, cached tokens are billed at a [discount on input token pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for Standard deployment types and up to [100% discount on input tokens](/azure/ai-services/openai/concepts/provisioned-throughput) for Provisioned deployment types.
 
 Caches are typically cleared within 5-10 minutes of inactivity and are always removed within one hour of the cache's last use. Prompt caches are not shared between Azure subscriptions. 
 
@@ -28,6 +28,9 @@ Currently only the following models support prompt caching with Azure OpenAI:
 - `gpt-4o-2024-08-06`
 - `gpt-4o-mini-2024-07-18`
 
+> [!NOTE]
+> Prompt caching is now also available as part of model fine-tuning for `gpt-4o` and `gpt-4o-mini`. Refer to the fine-tuning section of the [pricing page](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) for details.
+
 ## API support
 
 Official support for prompt caching was first added in API version `2024-10-01-preview`. At this time, only the o1 model family supports the `cached_tokens` API response parameter.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプトキャッシングに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるプロンプトキャッシングの使用方法に関するドキュメントを更新するものです。主な変更点として、文書の日付が2024年10月18日から2024年12月15日に更新されています。この変更は、情報の最新性を保つためのものです。

また、プロンプトキャッシングのメリットや運用についての説明は保持されたままですが、キャッシュされたトークンの料金が「50%割引」ではなく「割引」の形で表現され、より一般的な表記に変更されました。これにより、利用者にとっての理解が促進されています。

さらに、プロンプトキャッシングは「`gpt-4o`および`gpt-4o-mini`のモデルファインチューニングの一部としても利用可能」との注意書きが追加され、ユーザーが新たな情報を得られるようになっています。

全体的に、これらの変更は、プロンプトキャッシングに関する最新情報および重要な利点をユーザーに提供することを目的としています。

## articles/ai-services/openai/how-to/stored-completions.md{#item-ccc7e6}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,188 @@
+---
+title: 'How to use Azure OpenAI Service stored completions & distillation'
+titleSuffix: Azure OpenAI
+description: Learn how to use stored completions & distillation with Azure OpenAI
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: how-to
+ms.custom: references_regions
+ms.date: 12/12/2024
+author: mrbullwinkle
+ms.author: mbullwin
+recommendations: false
+---
+
+# Azure OpenAI stored completions & distillation (preview)
+
+Stored completions allow you to capture the conversation history from chat completions sessions to use as datasets for [evaluations](./evaluations.md) and [fine-tuning](./fine-tuning.md).
+
+## Stored completions support
+
+### API support
+
+- `2024-10-01-preview`
+
+### Model support
+
+- `gpt-4o-2024-08-06`
+
+### Regional availability
+
+- Sweden Central
+
+## Configure stored completions
+
+To enable stored completions for your Azure OpenAI deployment set the `store` parameter to `True`. Use the `metadata` parameter to enrich your stored completion dataset with additional information.
+
+
+# [Python (Microsoft Entra ID)](#tab/python-secure)
+
+```python
+import os
+from openai import AzureOpenAI
+from azure.identity import DefaultAzureCredential, get_bearer_token_provider
+
+token_provider = get_bearer_token_provider(
+    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
+)
+
+client = AzureOpenAI(
+  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
+  azure_ad_token_provider=token_provider,
+  api_version="2024-10-01-preview"
+)
+
+completion = client.chat.completions.create(
+    
+    model="gpt-4o", # replace with model deployment name
+    store= True,
+    metadata =  {
+    "user": "admin",
+    "category": "docs-test",
+  },
+    messages=[
+    {"role": "system", "content": "Provide a clear and concise summary of the technical content, highlighting key concepts and their relationships. Focus on the main ideas and practical implications."},
+    {"role": "user", "content": "Ensemble methods combine multiple machine learning models to create a more robust and accurate predictor. Common techniques include bagging (training models on random subsets of data), boosting (sequentially training models to correct previous errors), and stacking (using a meta-model to combine base model predictions). Random Forests, a popular bagging method, create multiple decision trees using random feature subsets. Gradient Boosting builds trees sequentially, with each tree focusing on correcting the errors of previous trees. These methods often achieve better performance than single models by reducing overfitting and variance while capturing different aspects of the data."}
+    ]   
+)
+
+print(completion.choices[0].message)
+
+
+```
+
+# [Python (API Key)](#tab/python-key)
+
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/azure-key-vault.md)]
+
+```python
+import os
+from openai import AzureOpenAI
+    
+client = AzureOpenAI(
+    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
+    api_version="2024-10-01-preview",
+    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
+    )
+
+ompletion = client.chat.completions.create(
+    
+    model="gpt-4o", # replace with model deployment name
+    store= True,
+    metadata =  {
+    "user": "admin",
+    "category": "docs-test",
+  },
+    messages=[
+    {"role": "system", "content": "Provide a clear and concise summary of the technical content, highlighting key concepts and their relationships. Focus on the main ideas and practical implications."},
+    {"role": "user", "content": "Ensemble methods combine multiple machine learning models to create a more robust and accurate predictor. Common techniques include bagging (training models on random subsets of data), boosting (sequentially training models to correct previous errors), and stacking (using a meta-model to combine base model predictions). Random Forests, a popular bagging method, create multiple decision trees using random feature subsets. Gradient Boosting builds trees sequentially, with each tree focusing on correcting the errors of previous trees. These methods often achieve better performance than single models by reducing overfitting and variance while capturing different aspects of the data."}
+    ]   
+)
+
+print(completion.choices[0].message)
+```
+---
+
+Once stored completions are enabled for an Azure OpenAI deployment, they'll begin to show up in the [Azure AI Foundry portal](https://oai.azure.com) in the **Stored Completions** pane.
+
+:::image type="content" source="../media/stored-completions/stored-completions.png" alt-text="Screenshot of the stored completions User Experience." lightbox="../media/stored-completions/stored-completions.png":::
+
+## Distillation
+
+Distillation allows you to turn your stored completions into a fine-tuning dataset. A common use case is to use stored completions with a larger more powerful model for a particular task and then use the stored completions to train a smaller model on high quality examples of model interactions.
+
+Distillation requires a minimum of 10 stored completions, though it's recommended to provide hundreds to thousands of stored completions for the best results.
+
+1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://oai.azure.com) use the **Filter** options to select the completions you want to train your model with.
+
+2. To begin distillation, select **Distill**
+
+    :::image type="content" source="../media/stored-completions/distill.png" alt-text="Screenshot of the stored completions User Experience with distill highlighted." lightbox="../media/stored-completions/distill.png":::
+
+3. Pick which model you would like to fine-tune with your stored completion dataset.
+
+    :::image type="content" source="../media/stored-completions/fine-tune.png" alt-text="Screenshot of the stored completion distillation model selection." lightbox="../media/stored-completions/fine-tune.png":::
+
+4. Confirm which version of the model you want to fine-tune:
+
+    :::image type="content" source="../media/stored-completions/version.png" alt-text="Screenshot of the stored completion distillation version." lightbox="../media/stored-completions/version.png":::
+
+5. A `.jsonl` file with a randomly generated name will be created as a training dataset from your stored completions. Select the file > **Next**.
+
+    > [!Note]
+    > Stored completion distillation training files cannot be accessed directly and cannot be exported externally/downloaded.
+
+    :::image type="content" source="../media/stored-completions/file-name.png" alt-text="Screenshot of the stored completion training dataset jsonl file." lightbox="../media/stored-completions/file-name.png":::
+
+The rest of the steps correspond to the typical Azure OpenAI fine-tuning steps. To learn more, see our [fine-tuning getting started guide](./fine-tuning.md).
+
+## Evaluation
+
+The [evaluation](./evaluations.md) of large language models is a critical step in measuring their performance across various tasks and dimensions. This is especially important for fine-tuned models, where assessing the performance gains (or losses) from training is crucial. Thorough evaluations can help your understanding of how different versions of the model may impact your application or scenario.
+
+Stored completions can be used as a dataset for running evaluations.
+
+1. From the **Stored Completions** pane in the [Azure AI Foundry portal](https://oai.azure.com) use the **Filter** options to select the completions you want to be part of your evaluation dataset.
+
+2. To configure the evaluation, select **Evaluate**
+
+    :::image type="content" source="../media/stored-completions/evaluate.png" alt-text="Screenshot of the stored completion pane with evaluate selected." lightbox="../media/stored-completions/evaluate.png":::
+
+3. This launches the **Evaluations** pane with a prepopulated `.jsonl` file with a randomly generated name that is created as an evaluation dataset from your stored completions.
+
+    > [!Note]
+    > Stored completion evaluation data files cannot be accessed directly and cannot be exported externally/downloaded.
+
+    :::image type="content" source="../media/stored-completions/evaluation-data.png" alt-text="Screenshot of the evaluations pane." lightbox="../media/stored-completions/evaluation-data.png":::
+
+To learn more about evaluation see, [getting started with evaluations](./evaluations.md)
+
+## Troubleshooting
+
+### Do I need special permissions to use stored completions?
+
+Stored completions access is controlled via two DataActions:
+
+- `Microsoft.CognitiveServices/accounts/OpenAI/stored-completions/read`
+- `Microsoft.CognitiveServices/accounts/OpenAI/stored-completions/action`
+
+By default `Cognitive Services OpenAI Contributor` has access to both these permissions:
+
+:::image type="content" source="../media/stored-completions/permissions.png" alt-text="Screenshot of stored completions permissions." lightbox="../media/stored-completions/permissions.png":::
+
+### How do I delete stored data?
+
+Data can be deleted by deleting the associated Azure OpenAI resource. If you wish to only delete stored completion data you must open a case with customer support.
+
+### How much stored completion data can I store?
+
+You can store a maximum 10 GB of data.
+
+### Can I prevent stored completions from ever being enabled on a subscription?
+
+You'll need to open a case with customer support to disable stored completions at the subscription level.
+
+### TypeError: Completions.create() got an unexpected argument 'store'
+
+This error occurs when you're running an older version of the OpenAI client library that predates the stored completions feature being released. Run  `pip install openai --upgrade`.
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure OpenAIサービスのストレージ完了と蒸留の使用方法"
}
```

### Explanation
このコードの変更は、新たに「Azure OpenAIサービスのストレージ完了と蒸留」に関する詳細なドキュメントを追加するものです。このドキュメントでは、ストレージ完了機能を使用して、チャット完了セッションからの会話履歴をキャプチャし、評価やファインチューニング用のデータセットとして活用する方法について説明されています。

主な内容にはストレージ完了のサポート情報、APIとモデルのサポート、地域での利用可能性が含まれています。また、ストレージ完了を有効にするための必要な設定手順も詳述されています。さらに、Pythonを使用したサンプルコードが2種類（Microsoft Entra IDを使用する方法とAPIキーを使用する方法）提供されており、ユーザーが実際にどのように実装するかを理解しやすくしています。

蒸留機能では、ストレージ完了をファインチューニングのデータセットとして利用する方法が説明され、ユーザーがデータをどのように活用してモデルを小型化できるかが示されています。評価セクションでは、ストレージ完了を利用して大規模言語モデルのパフォーマンスを測定することの重要性が強調され、トラブルシューティングセクションでは利用時に考えられる問題への対処法が詳細に解説されています。

全体的に、この更新はAzure OpenAIサービスのストレージ機能を利用するための包括的なガイドラインを提供し、ユーザーに新たな機能の利点を活かせるようサポートしています。

## articles/ai-services/openai/includes/model-matrix/standard-chat-completions.md{#item-aae3f1}

<details>
<summary>Diff</summary>
````diff
@@ -26,4 +26,4 @@ ms.date: 10/25/2024
 | uksouth          | -                          | -                       | -                      | -                      | -                           | -               | ✅                        | ✅                        | -                         | -                           | -                   | ✅                       | ✅                       | ✅                       | ✅                       | ✅                           |
 | westeurope       | -                          | -                       | -                      | -                      | -                           | -               | -                       | -                       | -                         | -                           | -                   | ✅                       | -                      | -                      | -                      | -                          |
 | westus           | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | ✅                          | ✅                            | -                   | -                      | -                      | ✅                       | ✅                       | -                          |
-| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
+| westus3          | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -               | ✅                        | -                       | -                         | ✅                            | -                   | -                      | -                      | -                      | ✅                       | -                          |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準チャット完了モデルマトリックスの修正"
}
```

### Explanation
このコードの変更は、標準チャット完了モデルマトリックスに関連するドキュメントの小規模な修正を行ったものです。具体的には、表の内容がわずかに変更されており、特に「westus3」地域におけるモデルのサポート状況が更新されています。

以前は、表には「westus3」地域のいくつかの機能が「-」で表示されていましたが、修正後も同じ内容が維持されています。この変更は、情報の正確性を保つための調整であり、特にこの地域のモデル利用状況をわかりやすく示すことを目的としています。

このタイプの更新は、ユーザーがAzure OpenAIモデルの機能や利用可能性を理解するために重要であり、ドキュメントの整合性を高める役割を果たします。全体として、この修正はモデルマトリックスの正確な反映を促進しており、ユーザーが各地域でのチャット完了機能に関する情報を正確に把握できるようにしています。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -8,28 +8,28 @@ ms.topic: include
 ms.date: 10/25/2024
 ---
 
-| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4**, **turbo-2024-04-09**   |
-|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------:|
-| australiaeast      | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| brazilsouth        | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| canadaeast         | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
-| francecentral      | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| germanywestcentral | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| japaneast          | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| koreacentral       | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| norwayeast         | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| polandcentral      | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| southafricanorth   | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| southindia         | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| spaincentral       | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
-| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| uaenorth           | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| uksouth            | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| westeurope         | -                          | -                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
-| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| **Region**     | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-10-01**   | **gpt-4**, **turbo-2024-04-09**   |
+|:-------------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:-------------------------------:|
+| australiaeast      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| brazilsouth        | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| canadaeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| eastus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| eastus2            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
+| francecentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| germanywestcentral | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| japaneast          | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| koreacentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| northcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| norwayeast         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| polandcentral      | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| southafricanorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| southcentralus     | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| southindia         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| spaincentral       | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| swedencentral      | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                            |
+| switzerlandnorth   | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| uaenorth           | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| uksouth            | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| westeurope         | -                          | -                       | ✅                       | ✅                       | -                      | ✅                            | -                                       | ✅                            |
+| westus             | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
+| westus3            | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | ✅                            |
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準グローバルモデルマトリックスの更新"
}
```

### Explanation
この変更は、「標準グローバル」のモデルマトリックスドキュメントにおける情報の更新を反映しています。以前のバージョンから新しいモデルリリースやそのサポート地域に関する情報が追加または修正されています。具体的には、表のいくつかの列が更新され、特に「gpt-4o」モデルのバージョンが「2024-11-20」に変更されています。

変更点は、各地域におけるモデルの可用性（特に最新のモデルオプション）が正確に示されるように整理されています。この表は、ユーザーが特定の地域でどのモデルが利用可能かを迅速に確認するためのものであり、特に選択肢が増えたことにより、Azure OpenAIサービスの利用が拡大することが期待されます。

全体として、この更新は情報の正確性と一貫性を向上させており、ユーザーが最新の機能とオプションを把握しやすくするための重要なステップとなっています。

## articles/ai-services/openai/includes/model-matrix/standard-models.md{#item-af04c4}

<details>
<summary>Diff</summary>
````diff
@@ -5,9 +5,10 @@ description: Quota and limits for Azure OpenAI by region.
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 10/25/2024
+ms.date: 12/16/2024
 ---
 
+
 | **Region**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4**, **0613**   | **gpt-4**, **1106-Preview**   | **gpt-4**, **0125-Preview**   | **gpt-4**, **vision-preview**   | **gpt-4**, **turbo-2024-04-09**   | **gpt-4-32k**, **0613**   | **gpt-35-turbo**, **0301**   | **gpt-35-turbo**, **0613**   | **gpt-35-turbo**, **1106**   | **gpt-35-turbo**, **0125**   | **gpt-35-turbo-16k**, **0613**   | **gpt-35-turbo-instruct**, **0914**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **1**   | **text-embedding-ada-002**, **2**   | **dall-e-2**, **2.0**   | **dall-e-3**, **3.0**   | **babbage-002**, **1**   | **davinci-002**, **1**   | **tts**, **001**   | **tts-hd**, **001**   | **whisper**, **001**   |
 |:-----------------|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------:|:---------------------------:|:---------------------------:|:-----------------------------:|:-------------------------------:|:-----------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:------------------------------:|:-----------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------:|:---------------------:|:----------------------:|:----------------------:|:----------------:|:-------------------:|:--------------------:|
 | australiaeast    | -                          | -                       | -                      | -                      | -                           | ✅                | ✅                        | -                       | ✅                          | -                           | ✅                    | -                      | ✅                       | ✅                       | ✅                       | ✅                           | -                               | ✅                              | ✅                              | -                             | ✅                              | -                 | ✅                  | -                  | -                  | -            | -               | -                |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "標準モデルマトリックスの更新"
}
```

### Explanation
この変更は、「標準モデルマトリックス」ドキュメントの更新を反映しています。主な修正点は、日付の更新と表の新しいモデル情報の追加です。具体的には、ドキュメントの日付が「2024年10月25日」から「2024年12月16日」に変更され、さらに新しいモデルとそのバージョンに関する情報が追加されています。

更新された表には、さまざまなモデル（例えば「gpt-4」や「davinci」など）に関連する地域別の提供状況が示されており、新モデルのプレビューが追加されています。この情報は、特定のモデルの利用可能性をユーザーに伝えるために重要であり、Azure OpenAIサービスの使用状況を把握しやすくしています。

全体として、このマイナーな更新は、ユーザーに最新のモデル情報を提供し、サポートされる機能が明確に示されることで、ユーザーの理解を助ける役割を果たしています。これにより、Azure OpenAIサービスを利用する際の意思決定がよりスムーズになることが期待されます。

## articles/ai-services/openai/index.yml{#item-0adb87}

<details>
<summary>Diff</summary>
````diff
@@ -40,7 +40,7 @@ landingContent:
         links:
            - text: Chat completions
              url: chatgpt-quickstart.md
-           - text: GPT-4 Turbo with Vision
+           - text: Vision-enabled models
              url: gpt-v-quickstart.md  
            - text: DALL-E
              url: dall-e-quickstart.md
@@ -98,7 +98,7 @@ landingContent:
                url: ./how-to/role-based-access-control.md 
              - text: GPT-3.5 Turbo & GPT-4
                url:  ./how-to/chatgpt.md
-             - text: GPT-4 Turbo with Vision
+             - text: Vision-enabled models
                url:  ./how-to/gpt-with-vision.md
              - text: Provisioned Throughput Units (PTU) 
                url: ./how-to/provisioned-throughput-onboarding.md
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ビジョン対応モデルの表記修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連する「index.yml」ファイルの内容に対する小規模な更新を示しています。具体的には、「GPT-4 Turbo with Vision」という表記が「Vision-enabled models」に変更されており、その影響を受けるリンクが修正されています。

この修正は、ユーザーに提供する情報の明確化を目的としており、ビジョン機能を持つモデル全体を正確に示すためのものです。変更されたテキストは、ドキュメント内の複数の箇所で見受けられ、これにより、利用者が関連するリソースを容易に特定できるようになっています。

全体として、このマイナーアップデートは、ユーザーに対して正確で最新の情報を提供するための重要な手順であり、ドキュメントの一貫性と可読性を向上させる効果があります。

## articles/ai-services/openai/media/fine-tuning/global-standard.png{#item-356a25}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニンググローバル標準画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するリソースに新しい画像ファイル「global-standard.png」が追加されたことを示しています。この画像は、ファインチューニングプロセスや、その標準を視覚的に検討する際に役立つ可能性があります。

新たに追加されたこの画像は、ユーザーがファインチューニングに関する内容を理解する際のサポート資料として機能することが期待されます。また、ビジュアル要素を組み込むことで、ドキュメントの情報をより効果的に伝える助けとなります。

全体として、この新機能は、Azure OpenAIサービスのファインチューニングに関する情報提供を強化し、ユーザーがより直感的に理解できるようにするための重要な追加といえます。

## articles/ai-services/openai/media/stored-completions/distill.png{#item-86c59e}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ストレージ済みコンプリート画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するリソースに新しい画像ファイル「distill.png」が追加されたことを示しています。この画像は、ストレージ済みコンプリートに関する説明や理解を助けるために使用されることが考えられます。

新たに追加されたこの画像は、ストレージの利用やその効果について視覚的に示すことで、ユーザーが関連情報をより容易に理解できるようにサポートします。特に、技術的な内容が多くを占めるドキュメントにおいて、ビジュアル要素は重要な役割を果たします。

全体として、この新機能はAzure OpenAIサービスにおけるストレージ済みコンプリート情報を強化し、ユーザーがその効果や使用方法を直感的に把握できるようにするための補足データとしての意義を持っています。

## articles/ai-services/openai/media/stored-completions/evaluate.png{#item-ec8d98}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するリソースに新しい画像ファイル「evaluate.png」が追加されたことを示しています。この画像は、ストレージ済みコンプリートの評価に関する情報を視覚的に表現するために使用されることが予想されます。

新たに追加されたこの画像は、ユーザーがストレージ済みコンプリートの評価プロセスを理解するのに役立ち、具体的な手順や評価基準を示すための補完的な情報として機能します。ビジュアル要素の導入により、技術的なコンテンツがより直感的に学習できるようになることが期待されます。

全体的に、この新機能は、Azure OpenAIサービスにおけるストレージ済みコンプリートの評価に関連する理解を深めるための重要な追加となっており、ユーザーがその実用性を把握しやすくなることを目指しています。

## articles/ai-services/openai/media/stored-completions/evaluation-data.png{#item-81f6bb}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価データ画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関するドキュメントに新しい画像ファイル「evaluation-data.png」が追加されたことを示しています。この画像は、評価データの視覚的表現を提供することを目的としています。

新たに追加されたこの画像は、ユーザーが評価データの重要性や使用方法を理解するのに寄与し、具体的な情報を視覚的に示すことで、学習効果を高める役割を果たします。特に、技術的なコンテンツでは、図や画像が情報を効果的に伝えるための重要なツールとなります。

総じて、この新機能は、評価データに関連する情報をより明確にし、Azure OpenAIサービスが提供する機能の理解を促進するための重要な追加となっています。ユーザーは、ストレージ済みコンプリートの評価に必要なデータを直感的に把握できるようになることが期待されます。

## articles/ai-services/openai/media/stored-completions/file-name.png{#item-d013d6}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファイル名画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するドキュメントに新しい画像ファイル「file-name.png」が追加されたことを示しています。この画像はファイル名の視覚的な表現を提供し、ユーザーがその重要性や使い方を理解するための助けとなることを意図しています。

追加されたこの画像は、ストレージ済みコンプリートのファイル名に関する具体的な情報を提供し、技術的な文書における理解を深めるための補助ツールとして機能します。視覚的要素が組み込まれることで、情報がより直感的に伝わるため、ユーザーは内容を把握しやすくなります。

全体として、この新機能は、Azure OpenAIサービスにおけるファイル名の認識を強化し、ドキュメントの有用性を高める重要な追加となっています。ユーザーは、ストレージ済みコンプリートの管理や利用において、より効果的に情報を操作できるようになることが期待されます。

## articles/ai-services/openai/media/stored-completions/fine-tune.png{#item-b814bb}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ファインチューニング画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するドキュメントに新しい画像ファイル「fine-tune.png」が追加されたことを示しています。この画像は、ファインチューニングのプロセスを視覚的に表現しており、ユーザーがその概念をより理解しやすくすることを目的としています。

追加された画像は、Azure OpenAIサービスにおけるモデルのファインチューニングに関する具体的な情報を提供し、テキスト生成や他のタスクにおける効果的な活用方法を示唆します。視覚的な要素が含まれることで、ユーザーはファインチューニングの重要性や適用手法を直感的に理解することが可能になります。

この新機能は、資料の視覚的な魅力を高めるだけでなく、ユーザーがAzure OpenAIサービスを利用する際の理解を深め、実践的な知識の向上に寄与する重要な追加となっています。

## articles/ai-services/openai/media/stored-completions/permissions.png{#item-5f02c1}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "パーミッション画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するドキュメントに新しい画像ファイル「permissions.png」が追加されたことを示しています。この画像は、サービスにおけるアクセス権限やパーミッションの管理に関する情報を視覚的に示すことを目的としています。

追加されたこの画像は、ユーザーがアクセス権限の設定方法やコンプリートされたデータへのアクセスに必要な要件を理解するのに役立ちます。視覚的な補助が加わることで、ユーザーは複雑な情報をより理解しやすくなり、Azure OpenAIサービスの利用における操作の確実性が向上します。

この新機能は、ドキュメントの明確さと実用性を高め、ユーザーが Azure OpenAIサービスを安心して利用できるようにするための重要なステップとなるでしょう。

## articles/ai-services/openai/media/stored-completions/stored-completions.png{#item-6b5634}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ストアドコンプリート画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するドキュメントに新しい画像ファイル「stored-completions.png」が追加されたことを示しています。この画像は、ストアドコンプリート機能について視覚的に説明することを目的としています。

追加された画像は、ユーザーがストアドコンプリートの使用方法や、その利点を理解するのに役立ちます。この機能は、事前に生成したコンテンツや回答を保存し、後から再利用することを可能にします。視覚的要素が加わることで、ストアドコンプリートの概念をより直感的に把握できるようになります。

この新機能は、資料の価値を高めるだけでなく、ユーザーがAzure OpenAIサービスを効果的に活用し、自身のニーズに合ったコンテンツを生成する手助けをする重要な追加となっています。

## articles/ai-services/openai/media/stored-completions/version.png{#item-1e76cf}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "バージョン画像の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関連するドキュメントに新しい画像ファイル「version.png」が追加されたことを示しています。この画像は、バージョン管理の概念や、ストアドコンプリート機能に関連する異なるバージョンの理解を助けるために作成されています。

追加された画像は、ユーザーがストアドコンプリートのさまざまなバージョン間の差異や、どのバージョンを使用するべきかを判断するのに役立ちます。バージョン管理の明確なビジュアルを提供することで、ユーザーは自身のニーズに最適な選択をするための情報を得られるようになります。

この新機能は、ドキュメントの全体的な理解を深め、ユーザーがAzure OpenAIサービスをより効率的に利用する手助けをするための重要な追加となっています。

## articles/ai-services/openai/overview.md{#item-97d507}

<details>
<summary>Diff</summary>
````diff
@@ -22,7 +22,7 @@ Azure OpenAI Service provides REST API access to OpenAI's powerful language mode
 | --- | --- |
 | Models available | **o1-preview** & **o1-mini** - (Limited Access - [Request Access](https://aka.ms/oai/modelaccess))<br>**GPT-4o & GPT-4o mini**<br> **GPT-4 series (including GPT-4 Turbo with Vision)** <br>**GPT-3.5-Turbo series**<br> Embeddings series <br> Learn more in our [Models](./concepts/models.md) page.|
 | Fine-tuning | `GPT-4o-mini` (preview) <br> `GPT-4` (preview) <br>`GPT-3.5-Turbo` (0613) <br> `babbage-002` <br> `davinci-002`.|
-| Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on GPT-4 Turbo with Vision, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
+| Price | [Available here](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) <br> For details on vision-enabled chat models, see the [special pricing information](../openai/concepts/gpt-with-vision.md#special-pricing-information).|
 | Virtual network support & private link support | Yes.  |
 | Managed Identity| Yes, via Microsoft Entra ID | 
 | UI experience | [Azure portal](https://portal.azure.com) for account & resource management, <br> [Azure AI Foundry](https://ai.azure.com) for model exploration and fine-tuning |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "料金情報の修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスの概要に関する文書「overview.md」において、料金情報に関する記述が修正されたことを示しています。具体的には、「GPT-4 Turbo with Vision」に関する情報が、「vision-enabled chat models」に変更されました。

この修正は、ユーザーに対してより正確で明確な情報を提供することを目的としており、料金の詳細を確認する際に、どのモデルが視覚機能をサポートしているかを理解するのに役立ちます。また、関連するリンク先も変更されておらず、引き続き詳細情報が提供されることが強調されています。

全体として、この小規模な更新は、Azure OpenAIサービスを利用するユーザーに対し、正しい情報を提供し、彼らの意思決定を効果的にサポートすることに貢献しています。

## articles/ai-services/openai/realtime-audio-reference.md{#item-276d51}

<details>
<summary>Diff</summary>
````diff
@@ -54,15 +54,15 @@ There are nine client events that can be sent from the client to the server:
 
 | Event | Description |
 |-------|-------------|
-| [RealtimeClientEventConversationItemCreate](#realtimeclienteventconversationitemcreate) | Send this client event when adding an item to the conversation. |
-| [RealtimeClientEventConversationItemDelete](#realtimeclienteventconversationitemdelete) | Send this client event when you want to remove any item from the conversation history. |
-| [RealtimeClientEventConversationItemTruncate](#realtimeclienteventconversationitemtruncate) | Send this client event when you want to truncate a previous assistant message's audio. |
-| [RealtimeClientEventInputAudioBufferAppend](#realtimeclienteventinputaudiobufferappend) | Send this client event to append audio bytes to the input audio buffer. |
-| [RealtimeClientEventInputAudioBufferClear](#realtimeclienteventinputaudiobufferclear) | Send this client event to clear the audio bytes in the buffer. |
-| [RealtimeClientEventInputAudioBufferCommit](#realtimeclienteventinputaudiobuffercommit) | Send this client event to commit audio bytes to a user message. |
-| [RealtimeClientEventResponseCancel](#realtimeclienteventresponsecancel) | Send this client event to cancel an in-progress response. |
-| [RealtimeClientEventResponseCreate](#realtimeclienteventresponsecreate) | Send this client event to trigger a response generation. |
-| [RealtimeClientEventSessionUpdate](#realtimeclienteventsessionupdate) | Send this client event to update the session's default configuration. |
+| [RealtimeClientEventConversationItemCreate](#realtimeclienteventconversationitemcreate) | The client `conversation.item.create` event is used to add a new item to the conversation's context, including messages, function calls, and function call responses. |
+| [RealtimeClientEventConversationItemDelete](#realtimeclienteventconversationitemdelete) | The client `conversation.item.delete` event is used to remove an item from the conversation history. |
+| [RealtimeClientEventConversationItemTruncate](#realtimeclienteventconversationitemtruncate) | The client `conversation.item.truncate` event is used to truncate a previous assistant message's audio. |
+| [RealtimeClientEventInputAudioBufferAppend](#realtimeclienteventinputaudiobufferappend) | The client `input_audio_buffer.append` event is used to append audio bytes to the input audio buffer. |
+| [RealtimeClientEventInputAudioBufferClear](#realtimeclienteventinputaudiobufferclear) | The client `input_audio_buffer.clear` event is used to clear the audio bytes in the buffer. |
+| [RealtimeClientEventInputAudioBufferCommit](#realtimeclienteventinputaudiobuffercommit) | The client `input_audio_buffer.commit` event is used to commit the user input audio buffer. |
+| [RealtimeClientEventResponseCancel](#realtimeclienteventresponsecancel) | The client `response.cancel` event is used to cancel an in-progress response. |
+| [RealtimeClientEventResponseCreate](#realtimeclienteventresponsecreate) | The client `response.create` event is used to instruct the server to create a response via model inferencing. |
+| [RealtimeClientEventSessionUpdate](#realtimeclienteventsessionupdate) | The client `session.update` event is used to update the session's default configuration. |
 
 ### RealtimeClientEventConversationItemCreate
 
@@ -143,7 +143,7 @@ The client `input_audio_buffer.append` event is used to append audio bytes to th
 
 In Server VAD (Voice Activity Detection) mode, the audio buffer is used to detect speech and the server decides when to commit. When server VAD is disabled, the client can choose how much audio to place in each event up to a maximum of 15 MiB. For example, streaming smaller chunks from the client can allow the VAD to be more responsive. 
 
-Unlike made other client events, the server doesn't send a confirmation response to client `input_audio_buffer.append` event.
+Unlike most other client events, the server doesn't send a confirmation response to client `input_audio_buffer.append` event.
 
 #### Event structure
 
@@ -281,34 +281,34 @@ There are 28 server events that can be received from the server:
 
 | Event | Description |
 |-------|-------------|
-| [RealtimeServerEventConversationCreated](#realtimeservereventconversationcreated) | Server event when a conversation is created. Emitted right after session creation. |
-| [RealtimeServerEventConversationItemCreated](#realtimeservereventconversationitemcreated) | Server event when a conversation item is created. |
-| [RealtimeServerEventConversationItemDeleted](#realtimeservereventconversationitemdeleted) | Server event when an item in the conversation is deleted. |
-| [RealtimeServerEventConversationItemInputAudioTranscriptionCompleted](#realtimeservereventconversationiteminputaudiotranscriptioncompleted) | Server event when input audio transcription is enabled and a transcription succeeds. |
-| [RealtimeServerEventConversationItemInputAudioTranscriptionFailed](#realtimeservereventconversationiteminputaudiotranscriptionfailed) | Server event when input audio transcription is configured, and a transcription request for a user message failed. |
-| [RealtimeServerEventConversationItemTruncated](#realtimeservereventconversationitemtruncated) | Server event when the client truncates an earlier assistant audio message item. |
-| [RealtimeServerEventError](#realtimeservereventerror) | Server event when an error occurs. |
-| [RealtimeServerEventInputAudioBufferCleared](#realtimeservereventinputaudiobuffercleared) | Server event when the client clears the input audio buffer. |
-| [RealtimeServerEventInputAudioBufferCommitted](#realtimeservereventinputaudiobuffercommitted) | Server event when an input audio buffer is committed, either by the client or automatically in server VAD mode. |
-| [RealtimeServerEventInputAudioBufferSpeechStarted](#realtimeservereventinputaudiobufferspeechstarted) | Server event in server turn detection mode when speech is detected. |
-| [RealtimeServerEventInputAudioBufferSpeechStopped](#realtimeservereventinputaudiobufferspeechstopped) | Server event in server turn detection mode when speech stops. |
-| [RealtimeServerEventRateLimitsUpdated](#realtimeservereventratelimitsupdated) | Emitted after every "response.done" event to indicate the updated rate limits. |
-| [RealtimeServerEventResponseAudioDelta](#realtimeservereventresponseaudiodelta) | Server event when the model-generated audio is updated. |
-| [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | Server event when the model-generated audio is done. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventResponseAudioTranscriptDelta](#realtimeservereventresponseaudiotranscriptdelta) | Server event when the model-generated transcription of audio output is updated. |
-| [RealtimeServerEventResponseAudioTranscriptDone](#realtimeservereventresponseaudiotranscriptdone) | Server event when the model-generated transcription of audio output is done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventResponseContentPartAdded](#realtimeservereventresponsecontentpartadded) | Server event when a new content part is added to an assistant message item during response generation. |
-| [RealtimeServerEventResponseContentPartDone](#realtimeservereventresponsecontentpartdone) | Server event when a content part is done streaming in an assistant message item. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventResponseCreated](#realtimeservereventresponsecreated) | Server event when a new Response is created. The first event of response creation, where the response is in an initial state of "in_progress". |
-| [RealtimeServerEventResponseDone](#realtimeservereventresponsedone) | Server event when a response is done streaming. Always emitted, no matter the final state. |
-| [RealtimeServerEventResponseFunctionCallArgumentsDelta](#realtimeservereventresponsefunctioncallargumentsdelta) | Server event when the model-generated function call arguments are updated. |
-| [RealtimeServerEventResponseFunctionCallArgumentsDone](#realtimeservereventresponsefunctioncallargumentsdone) | Server event when the model-generated function call arguments are done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventResponseOutputItemAdded](#realtimeservereventresponseoutputitemadded) | Server event when a new output item is added to a response. |
-| [RealtimeServerEventResponseOutputItemDone](#realtimeservereventresponseoutputitemdone) | Server event when an output item is done streaming. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventResponseTextDelta](#realtimeservereventresponsetextdelta) | Server event when the model-generated text is updated. |
-| [RealtimeServerEventResponseTextDone](#realtimeservereventresponsetextdone) | Server event when the model-generated text is done. Also emitted when a response is interrupted, incomplete, or canceled. |
-| [RealtimeServerEventSessionCreated](#realtimeservereventsessioncreated) | Server event when a session is created. |
-| [RealtimeServerEventSessionUpdated](#realtimeservereventsessionupdated) | Server event when a session is updated. |
+| [RealtimeServerEventConversationCreated](#realtimeservereventconversationcreated) | The server `conversation.created` event is returned right after session creation. One conversation is created per session. |
+| [RealtimeServerEventConversationItemCreated](#realtimeservereventconversationitemcreated) | The server `conversation.item.created` event is returned when a conversation item is created. |
+| [RealtimeServerEventConversationItemDeleted](#realtimeservereventconversationitemdeleted) | The server `conversation.item.deleted` event is returned when the client deleted an item in the conversation with a `conversation.item.delete` event. |
+| [RealtimeServerEventConversationItemInputAudioTranscriptionCompleted](#realtimeservereventconversationiteminputaudiotranscriptioncompleted) | The server `conversation.item.input_audio_transcription.completed` event is the result of audio transcription for speech written to the audio buffer. |
+| [RealtimeServerEventConversationItemInputAudioTranscriptionFailed](#realtimeservereventconversationiteminputaudiotranscriptionfailed) | The server `conversation.item.input_audio_transcription.failed` event is returned when input audio transcription is configured, and a transcription request for a user message failed. |
+| [RealtimeServerEventConversationItemTruncated](#realtimeservereventconversationitemtruncated) | The server `conversation.item.truncated` event is returned when the client truncates an earlier assistant audio message item with a `conversation.item.truncate` event. |
+| [RealtimeServerEventError](#realtimeservereventerror) | The server `error` event is returned when an error occurs, which could be a client problem or a server problem. |
+| [RealtimeServerEventInputAudioBufferCleared](#realtimeservereventinputaudiobuffercleared) | The server `input_audio_buffer.cleared` event is returned when the client clears the input audio buffer with a `input_audio_buffer.clear` event. |
+| [RealtimeServerEventInputAudioBufferCommitted](#realtimeservereventinputaudiobuffercommitted) | The server `input_audio_buffer.committed` event is returned when an input audio buffer is committed, either by the client or automatically in server VAD mode. |
+| [RealtimeServerEventInputAudioBufferSpeechStarted](#realtimeservereventinputaudiobufferspeechstarted) | The server `input_audio_buffer.speech_started` event is returned in `server_vad` mode when speech is detected in the audio buffer. |
+| [RealtimeServerEventInputAudioBufferSpeechStopped](#realtimeservereventinputaudiobufferspeechstopped) | The server `input_audio_buffer.speech_stopped` event is returned in `server_vad` mode when the server detects the end of speech in the audio buffer. |
+| [RealtimeServerEventRateLimitsUpdated](#realtimeservereventratelimitsupdated) | The server `rate_limits.updated` event is emitted at the beginning of a response to indicate the updated rate limits. |
+| [RealtimeServerEventResponseAudioDelta](#realtimeservereventresponseaudiodelta) | The server `response.audio.delta` event is returned when the model-generated audio is updated. |
+| [RealtimeServerEventResponseAudioDone](#realtimeservereventresponseaudiodone) | The server `response.audio.done` event is returned when the model-generated audio is done. |
+| [RealtimeServerEventResponseAudioTranscriptDelta](#realtimeservereventresponseaudiotranscriptdelta) | The server `response.audio_transcript.delta` event is returned when the model-generated transcription of audio output is updated. |
+| [RealtimeServerEventResponseAudioTranscriptDone](#realtimeservereventresponseaudiotranscriptdone) | The server `response.audio_transcript.done` event is returned when the model-generated transcription of audio output is done streaming. |
+| [RealtimeServerEventResponseContentPartAdded](#realtimeservereventresponsecontentpartadded) | The server `response.content_part.added` event is returned when a new content part is added to an assistant message item. |
+| [RealtimeServerEventResponseContentPartDone](#realtimeservereventresponsecontentpartdone) | The server `response.content_part.done` event is returned when a content part is done streaming. |
+| [RealtimeServerEventResponseCreated](#realtimeservereventresponsecreated) | The server `response.created` event is returned when a new response is created. This is the first event of response creation, where the response is in an initial state of `in_progress`. |
+| [RealtimeServerEventResponseDone](#realtimeservereventresponsedone) | The server `response.done` event is returned when a response is done streaming. |
+| [RealtimeServerEventResponseFunctionCallArgumentsDelta](#realtimeservereventresponsefunctioncallargumentsdelta) | The server `response.function_call_arguments.delta` event is returned when the model-generated function call arguments are updated. |
+| [RealtimeServerEventResponseFunctionCallArgumentsDone](#realtimeservereventresponsefunctioncallargumentsdone) | The server `response.function_call_arguments.done` event is returned when the model-generated function call arguments are done streaming. |
+| [RealtimeServerEventResponseOutputItemAdded](#realtimeservereventresponseoutputitemadded) | The server `response.output_item.added` event is returned when a new item is created during response generation. |
+| [RealtimeServerEventResponseOutputItemDone](#realtimeservereventresponseoutputitemdone) | The server `response.output_item.done` event is returned when an item is done streaming. |
+| [RealtimeServerEventResponseTextDelta](#realtimeservereventresponsetextdelta) | The server `response.text.delta` event is returned when the model-generated text is updated. |
+| [RealtimeServerEventResponseTextDone](#realtimeservereventresponsetextdone) | The server `response.text.done` event is returned when the model-generated text is done streaming. |
+| [RealtimeServerEventSessionCreated](#realtimeservereventsessioncreated) | The server `session.created` event is the first server event when you establish a new connection to the Realtime API. This event creates and returns a new session with the default session configuration. |
+| [RealtimeServerEventSessionUpdated](#realtimeservereventsessionupdated) | The server `session.updated` event is returned when a session is updated by the client. If there's an error, the server sends an `error` event instead. |
 
 ### RealtimeServerEventConversationCreated
 
@@ -1080,7 +1080,7 @@ The server `session.updated` event is returned when a session is updated by the
 | Field | Type | Description | 
 |-------|------|-------------|
 | type | [RealtimeClientEventType](#realtimeclienteventtype) | The type of the client event. |
-| event_id | string | The unique ID of the event. |
+| event_id | string | The unique ID of the event. The ID can be specified by the client to help identify the event. |
 
 ### RealtimeClientEventType
 
@@ -1117,18 +1117,28 @@ The item to add to the conversation.
 
 ### RealtimeConversationRequestItem
 
+You use the `RealtimeConversationRequestItem` object to create a new item in the conversation via the [conversation.item.create](#realtimeclienteventconversationitemcreate) event.
+
 | Field | Type | Description | 
 |-------|------|-------------|
 | type | [RealtimeItemType](#realtimeitemtype) | The type of the item. |
-| id | string | The unique ID of the item. |
+| id | string | The unique ID of the item. The ID can be specified by the client to help manage server-side context. If the client doesn't provide an ID, the server generates one. |
 
 ### RealtimeConversationResponseItem
 
+The `RealtimeConversationResponseItem` object represents an item in the conversation. It's used in some of the server events, such as:
+
+- [conversation.item.created](#realtimeservereventconversationitemcreated)
+- [response.output_item.added](#realtimeservereventresponseoutputitemadded)
+- [response.output_item.done](#realtimeservereventresponseoutputitemdone)
+- [`response.created`](#realtimeservereventresponsecreated) (via the `response` property type [`RealtimeResponse`](#realtimeresponse))
+- [`response.done`](#realtimeservereventresponsedone) (via the `response` property type [`RealtimeResponse`](#realtimeresponse))
+
 | Field | Type | Description | 
 |-------|------|-------------|
-| object | string | The conversation response item.<br><br>Allowed values: `realtime.item` |
-| type | [RealtimeItemType](#realtimeitemtype) | The type of the item. | 
-| id | string | The unique ID of the item.<br><br>This property is nullable. |
+| object | string | The identifier for the returned API object.<br><br>Allowed values: `realtime.item` |
+| type | [RealtimeItemType](#realtimeitemtype) | The type of the item.<br><br>Allowed values: `message`, `function_call`, `function_call_output` | 
+| id | string | The unique ID of the item. The ID can be specified by the client to help manage server-side context. If the client doesn't provide an ID, the server generates one.<br><br>This property is nullable. |
 
 ### RealtimeFunctionTool
 
@@ -1138,8 +1148,8 @@ The definition of a function tool as used by the realtime endpoint.
 |-------|------|-------------|
 | type | string | The type of the tool.<br><br>Allowed values: `function` |
 | name | string | The name of the function. |
-| description | string | The description of the function. |
-| parameters | object | The parameters of the function. |
+| description | string | The description of the function, including usage guidelines. For example, "Use this function to get the current time." |
+| parameters | object | The parameters of the function in the form of a JSON object. |
 
 ### RealtimeItemStatus
 
@@ -1214,6 +1224,8 @@ The definition of a function tool as used by the realtime endpoint.
 
 ### RealtimeRequestSession
 
+You use the `RealtimeRequestSession` object when you want to update the session configuration via the [session.update](#realtimeclienteventsessionupdate) event.
+
 | Field | Type | Description | 
 |-------|------|-------------|
 | modalities | array | The modalities that the session supports.<br><br>Allowed values: `text`, `audio`<br/><br/>For example, `"modalities": ["text", "audio"]` is the default setting that enables both text and audio modalities. To enable only text, set `"modalities": ["text"]`. You can't enable only audio. |
@@ -1224,7 +1236,7 @@ The definition of a function tool as used by the realtime endpoint.
 | input_audio_transcription | [RealtimeAudioInputTranscriptionSettings](#realtimeaudioinputtranscriptionsettings) | The settings for audio input transcription.<br><br>This property is nullable. |
 | turn_detection | [RealtimeTurnDetection](#realtimeturndetection) | The turn detection settings for the session.<br><br>This property is nullable. |
 | tools | array of [RealtimeTool](#realtimetool) | The tools available to the model for the session. |
-| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session. |
+| tool_choice | [RealtimeToolChoice](#realtimetoolchoice) | The tool choice for the session.<br><br>Allowed values: `auto`, `none`, and `required`. Otherwise, you can specify the name of the function to use. |
 | temperature | number | The sampling temperature for the model. The allowed temperature values are limited to [0.6, 1.2]. Defaults to 0.8. |
 | max_response_output_tokens | integer or "inf" | The maximum number of output tokens per assistant response, inclusive of tool calls.<br><br>Specify an integer between 1 and 4096 to limit the output tokens. Otherwise, set the value to "inf" to allow the maximum number of tokens.<br><br>For example, to limit the output tokens to 1000, set `"max_response_output_tokens": 1000`. To allow the maximum number of tokens, set `"max_response_output_tokens": "inf"`.<br><br>Defaults to `"inf"`. |
 
@@ -1324,6 +1336,10 @@ The response resource.
 
 ### RealtimeResponseSession
 
+The `RealtimeResponseSession` object represents a session in the Realtime API. It's used in some of the server events, such as:
+- [`session.created`](#realtimeservereventsessioncreated)
+- [`session.updated`](#realtimeservereventsessionupdated)
+
 | Field | Type | Description | 
 |-------|------|-------------|
 | object | string | The session object.<br><br>Allowed values: `realtime.session` |
@@ -1369,7 +1385,7 @@ The response resource.
 | Field | Type | Description | 
 |-------|------|-------------|
 | type | [RealtimeServerEventType](#realtimeservereventtype) | The type of the server event. |
-| event_id | string | The unique ID of the event. |
+| event_id | string | The unique ID of the server event. |
 
 ### RealtimeServerEventRateLimitsUpdatedRateLimitsItem
 
@@ -1436,21 +1452,21 @@ The base representation of a realtime tool definition.
 
 ### RealtimeToolChoice
 
-The combined set of available representations for a realtime tool_choice parameter, encompassing both string literal options like 'auto' and structured references to defined tools.
+The combined set of available representations for a realtime `tool_choice` parameter, encompassing both string literal options like 'auto' and structured references to defined tools.
 
 ### RealtimeToolChoiceFunctionObject
 
-The representation of a realtime tool_choice selecting a named function tool.
+The representation of a realtime `tool_choice` selecting a named function tool.
 
 | Field | Type | Description | 
 |-------|------|-------------|
-| type | string | The type of the tool_choice.<br><br>Allowed values: `function` |
+| type | string | The type of the `tool_choice`.<br><br>Allowed values: `function` |
 | function | object | The function tool to select.<br><br>See nested properties next.|
 | + name | string | The name of the function tool.<br><br>A property of the `function` object. | 
 
 ### RealtimeToolChoiceLiteral
 
-The available set of mode-level, string literal tool_choice options for the realtime endpoint.
+The available set of mode-level, string literal `tool_choice` options for the realtime endpoint.
 
 **Allowed Values:**
 
@@ -1460,11 +1476,11 @@ The available set of mode-level, string literal tool_choice options for the real
 
 ### RealtimeToolChoiceObject
 
-A base representation for a realtime tool_choice selecting a named tool.
+A base representation for a realtime `tool_choice` selecting a named tool.
 
 | Field | Type | Description | 
 |-------|------|-------------|
-| type | [RealtimeToolType](#realtimetooltype) | The type of the tool_choice. |
+| type | [RealtimeToolType](#realtimetooltype) | The type of the `tool_choice`. |
 
 ### RealtimeToolType
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リアルタイムオーディオリファレンスの改善"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「realtime-audio-reference.md」文書に対する修正を示しており、主にイベントの説明を改良し、情報を整理しました。具体的には、クライアントおよびサーバーの各イベントの説明がより明確になり、用語が統一されたことで理解しやすくなりました。

変更内容には、各イベントに対応するクライアントとサーバーの説明が、より直感的な表現に編集されたことが含まれています。例えば、クライアントイベントの説明文が具体的な使用例や詳細情報を含むように更新され、サーバーイベントの記述も強化されています。これにより、開発者はどのイベントがどのような用途に対応しているのかをよりよく理解できるようになります。

この更新は、リアルタイムオーディオの機能を利用する際に、開発者が迅速に正しい情報を把握できるようにするための重要なステップとなります。全体的に、文書はより一貫性があり、使いやすくなっています。

## articles/ai-services/openai/toc.yml{#item-c945af}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ items:
     - name: Chat
       href: chatgpt-quickstart.md  
       displayName: ChatGPT, chatgpt
-    - name: GPT-4 Turbo with Vision
+    - name: Vision-enabled chats
       href: gpt-v-quickstart.md
     - name: DALL-E
       href: dall-e-quickstart.md
@@ -64,7 +64,7 @@ items:
       href: ./concepts/understand-embeddings.md
     - name: Fine-tuning
       href: ./concepts/fine-tuning-considerations.md
-    - name: GPT-4 Turbo with Vision
+    - name: Vision-enabled models
       href: ./concepts/gpt-with-vision.md
     - name: Red teaming large language models (LLMs)
       href: ./concepts/red-teaming.md
@@ -122,7 +122,7 @@ items:
     - name: GPT-35-Turbo & GPT-4 
       href: ./how-to/chatgpt.md
       displayName: ChatGPT, chatgpt
-    - name: GPT-4 Turbo with Vision
+    - name: Vision-enabled chats
       href: ./how-to/gpt-with-vision.md
     - name: DALL-E
       href: ./how-to/dall-e.md
@@ -170,6 +170,8 @@ items:
         displayName: fine-tuning, finetuning
       - name: Weights & Biases integration (preview)
         href: ./how-to/weights-and-biases-integration.md
+  - name: Stored completions
+    href: ./how-to/stored-completions.md
   - name: Use your data
     items:
       - name: Text data
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する文書の目次（`toc.yml`）において、いくつかの記述が修正および追加されたことを示しています。主な変更内容は「GPT-4 Turbo with Vision」に関連する項目名が「Vision-enabled chats」や「Vision-enabled models」に変更されたことで、用語がより一般的かつ明確な表現に統一されています。

具体的には、複数のセクションで同様の変更が行われており、関連するリンク先もそのまま保持されています。また、新たに「Stored completions」という項目が追加され、これによりユーザーは保存された完了に関する情報を簡単に見つけられるようになります。

全体として、これらの更新はドキュメントの可読性およびアクセスのしやすさを向上させ、利用者が必要な情報に迅速にアクセスできるようにすることを目的としています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -11,7 +11,7 @@ ms.custom:
   - references_regions
   - ignite-2024
 ms.topic: whats-new
-ms.date: 11/12/2024
+ms.date: 11/16/2024
 recommendations: false
 ---
 
@@ -21,6 +21,18 @@ This article provides a summary of the latest releases and major documentation u
 
 ## December 2024
 
+### GPT-4o 2024-11-20
+
+`gpt-4o-2024-11-20` is now available for [global standard deployment](./how-to/deployment-types.md) in:
+
+- East US
+- East US 2
+- North Central US
+- South Central US
+- West US
+- West US 3
+- Sweden Central
+
 ### NEW data zone provisioned deployment type
 
 Data zone provisioned deployments are available in the same Azure OpenAI resource as all other Azure OpenAI deployment types but allow you to leverage Azure global infrastructure to dynamically route traffic to the data center within the Microsoft defined data zone with the best availability for each request. Data zone provisioned deployments provide reserved model processing capacity for high and predictable throughput using Azure infrastructure within Microsoft specified data zones. Data zone provisioned deployments are supported on `gpt-4o-2024-08-06`, `gpt-4o-2024-05-13`, and `gpt-4o-mini-2024-07-18` models.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能の追加と日付の更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「whats-new.md」ドキュメントに対するもので、主に新しい機能の追加と日付の更新を行っています。具体的には、文書の最終更新日が「2024年11月12日」から「2024年11月16日」に変更され、新たに「GPT-4o 2024-11-20」というモデルが追加されました。

新しいモデルは、特定の地域でのグローバルスタンダードデプロイメントに対応しており、デプロイ可能な地域には「East US」「West US」「Sweden Central」などが含まれています。また、新しいデータゾーンプロビジョニングデプロイメントタイプについて説明が追加されており、これはAzureのインフラストラクチャを利用してトラフィックを動的にルーティングし、高いスループットを提供する特性があります。

全体として、これらの変更はユーザーに対して最新の機能とリリース情報を提供し、より良い使用体験を促進することを目的としています。


