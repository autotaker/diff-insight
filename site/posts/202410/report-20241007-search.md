---
date: '2024-10-07'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b56c27...MicrosoftDocs:43a3b87
summary: この記事の更新では、情報の伝達方法が改善され、より明確な内容が提供されています。具体的には、海や水域に特有の雲の形成やパタゴニア沿岸の海流についての詳しい記述、NASA
  Earth Bookに関する説明と例が追加されました。全体的な構成も見直され、可読性が向上しています。技術的な情報に対する探究心を刺激し、読者がデータの応用についての理解を深めることができる内容になっています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:1b56c27...MicrosoftDocs:43a3b87){target="_blank"}

<format>
# Highlights
この記事の更新では、情報がより明確に伝わるように、それぞれの内容について詳細な修正と改善が施されています。具体的には、以下のような新しい機能や変更が行われています。

## New features
- 海や水域に特有の雲の形成に関する具体例の追加。
- パタゴニア沿岸の海流に関する詳細な記述。
- NASA Earth Bookに関する説明と例の追加。

## Breaking changes
- なし

## Other updates
- 全体の記事の構成を見直し、可読性を向上させるための文章構造の調整。
- セマンティックランキングとスコアリングプロファイルの更新。

# Insights
今回の変更では、専門的な内容を扱った記事がそれぞれ改善され、情報の提供方法が洗練されました。Markdown形式の記事は、より直感的な構造と流れるような文章で読者に情報を伝えることができるようになっています。

具体的な例として、海や水域の雲形成、パタゴニア沿岸の海流やリオ・デ・ラ・プラタ川から供給される栄養素に関する記述が挙げられます。これらの情報は、自然界でのダイナミックな相互作用とその視覚的なインパクトを理解するのに役立ちます。また、NASA Earth Bookに関する更新では、地球の地理的および自然現象を紹介する際に見落としがちなポイントに焦点を当て、読者がより深く理解できるように工夫されています。

さらに、モデル応答の違いや調整可能性についても言及されており、技術的に興味を持つ読者の探究心を刺激するような内容になっています。これにより、読者は、情報技術の応用により生成されるデータがどのように異なる結果を導き出すかをより深く理解できるようになったといえます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [tutorial-rag-build-solution-maximize-relevance.md](#item-2fdb09) | minor update | 記事の更新: 海に特有の雲の形成についての詳細を追加 | modified | 17 | 5 | 22 | 
| [tutorial-rag-build-solution-pipeline.md](#item-25ce01) | minor update | 記事の更新: パタゴニア沿岸の海流についての記述を改善 | modified | 12 | 6 | 18 | 
| [tutorial-rag-build-solution-query.md](#item-93965f) | minor update | 記事の更新: NASA Earth Bookに関する説明と例を追加 | modified | 35 | 16 | 51 | 


# Modified Contents
## articles/search/tutorial-rag-build-solution-maximize-relevance.md{#item-2fdb09}

<details>
<summary>Diff</summary>
````diff
@@ -107,7 +107,12 @@ print(response.choices[0].message.content)
 Output from this request might look like the following example.
 
 ```
-Yes, there are cloud formations specific to oceans and large bodies of water. A notable example is "cloud streets," which are parallel rows of clouds that form over the Bering Strait in the Arctic Ocean. These cloud streets occur when wind blows from a cold surface like sea ice over warmer, moister air near the open ocean, leading to the formation of spinning air cylinders. Clouds form along the upward cycle of these cylinders, while skies remain clear along the downward cycle (Source: page-21.pdf).
+Yes, there are cloud formations specific to oceans and large bodies of water. 
+A notable example is "cloud streets," which are parallel rows of clouds that form over 
+the Bering Strait in the Arctic Ocean. These cloud streets occur when wind blows from 
+a cold surface like sea ice over warmer, moister air near the open ocean, leading to 
+the formation of spinning air cylinders. Clouds form along the upward cycle of these cylinders, 
+while skies remain clear along the downward cycle (Source: page-21.pdf).
 ```
 
 ## Update the index for semantic ranking and scoring profiles
@@ -264,13 +269,20 @@ Output from a semantically ranked and boosted query might look like the followin
 ```
 Yes, there are specific cloud formations influenced by oceans and large bodies of water:
 
-- **Stratus Clouds Over Icebergs**: Low stratus clouds can frame holes over icebergs, such as Iceberg A-56 in the South Atlantic Ocean, likely due to thermal instability caused by the iceberg (source: page-39.pdf).
+- **Stratus Clouds Over Icebergs**: Low stratus clouds can frame holes over icebergs, 
+such as Iceberg A-56 in the South Atlantic Ocean, likely due to thermal instability caused 
+by the iceberg (source: page-39.pdf).
 
-- **Undular Bores**: These are wave structures in the atmosphere created by the collision of cool, dry air from a continent with warm, moist air over the ocean, as seen off the coast of Mauritania (source: page-23.pdf).
+- **Undular Bores**: These are wave structures in the atmosphere created by the collision 
+of cool, dry air from a continent with warm, moist air over the ocean, as seen off the 
+coast of Mauritania (source: page-23.pdf).
 
-- **Ship Tracks**: These are narrow clouds formed by water vapor condensing around tiny particles from ship exhaust. They are observed over the oceans, such as in the Pacific Ocean off the coast of California (source: page-31.pdf).
+- **Ship Tracks**: These are narrow clouds formed by water vapor condensing around tiny 
+particles from ship exhaust. They are observed over the oceans, such as in the Pacific Ocean 
+off the coast of California (source: page-31.pdf).
 
-These specific formations are influenced by unique interactions between atmospheric conditions and the presence of large water bodies or objects within them.
+These specific formations are influenced by unique interactions between atmospheric conditions 
+and the presence of large water bodies or objects within them.
 ```
 
 Adding semantic ranking and scoring profiles positively affects the response from the LLM by promoting results that meet scoring criteria and are semantically relevant. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: 海に特有の雲の形成についての詳細を追加"
}
```

### Explanation
この変更では、Markdown形式の記事「tutorial-rag-build-solution-maximize-relevance.md」において、情報の表現が改善されました。具体的には、文章の構造が見直され、文の流れがより明確に伝わるように調整されています。追加された内容は17行であり、削除された行は5行です。この変更により、海や大きな水域に特有の雲の形成に関する具体例が、より読みやすく改善されました。

例えば、特定の雲の種類に関する説明が新しい行に分かれており、これにより各例が強調されています。また、全体の文章の可読性が向上し、情報がより効果的に伝わるようになりました。さらに、セマンティックランキングとスコアリングプロファイルの更新が行われており、Llama（LLM）からの応答の質を向上させることを目的としています。この変更は、結果がスコアリング基準を満たし、意味的に関連性のあるものになるように促進します。

## articles/search/tutorial-rag-build-solution-pipeline.md{#item-25ce01}

<details>
<summary>Diff</summary>
````diff
@@ -346,20 +346,26 @@ Chunk:
 Swirling Bloom off Patagonia
 Argentina
 
-Interesting art often springs out of the convergence of different ideas and influences. And so it is with nature. 
+Interesting art often springs out of the convergence of different ideas and influences. 
+And so it is with nature. 
 
-Off the coast of Argentina, two strong ocean currents converge and often stir up a colorful brew, as shown in this Aqua image from 
+Off the coast of Argentina, two strong ocean currents converge and often stir up a colorful 
+brew, as shown in this Aqua image from 
 
 December 2010. 
 
-This milky green and blue bloom formed on the continental shelf off of Patagonia, where warmer, saltier waters from the subtropics 
+This milky green and blue bloom formed on the continental shelf off of Patagonia, where warmer, 
+saltier waters from the subtropics 
 
-meet colder, fresher waters flowing from the south. Where these currents collide, turbulent eddies and swirls form, pulling nutrients 
+meet colder, fresher waters flowing from the south. Where these currents collide, turbulent 
+eddies and swirls form, pulling nutrients 
 
-up from the deep ocean. The nearby Rio de la Plata also deposits nitrogen- and iron-laden sediment into the sea. Add in some 
+up from the deep ocean. The nearby Rio de la Plata also deposits nitrogen- and iron-laden 
+sediment into the sea. Add in some 
 ...
 
-while others terminate in water. The San Rafael and San Quintín glaciers (shown at the right) are the icefield’s largest. Both have 
+while others terminate in water. The San Rafael and San Quintín glaciers (shown at the right) 
+are the icefield’s largest. Both have 
 
 been receding rapidly in the past 30 years.
 ```
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: パタゴニア沿岸の海流についての記述を改善"
}
```

### Explanation
この変更は、Markdown形式の記事「tutorial-rag-build-solution-pipeline.md」に対するもので、内容が修正され、読みやすさが向上しました。具体的には、文章のいくつかの行が分割され、より明確に構成されています。合計で12行が追加され、6行が削除されています。

例として、アルゼンチン沿岸での海流の交差についての説明が改善され、視覚的な流れがスムーズになっています。文章の内容は、異なる海流がどのように色鮮やかな現象を生み出すかについての観察を含んでおり、特にパタゴニアの大陸棚における温かく塩分濃度の高い水と冷たく新鮮な水の交わりを詳細に述べています。

さらに、近くのリオ・デ・ラ・プラタ川が豊富な栄養素を海に供給する様子を説明する文も追加され、自然環境の複雑な相互作用についての理解が深まる内容になっています。この改訂により、読者は関連する情報をより簡単に消化できるようになっています。

## articles/search/tutorial-rag-build-solution-query.md{#item-93965f}

<details>
<summary>Diff</summary>
````diff
@@ -130,7 +130,13 @@ In this response, the answer is based on five inputs (`top=5`) consisting of chu
 Results from the first query `"What's the NASA earth book about?"` should look similar to the following example.
 
 ```
-The NASA Earth book is about the intricate and captivating science of our planet, studied through NASA's unique perspective and tools. It presents Earth as a dynamic and complex system, observed through various cycles and processes such as the water cycle and ocean circulation. The book combines stunning satellite images with detailed scientific insights, portraying Earth’s beauty and the continuous interaction of land, wind, water, ice, and air seen from above. It aims to inspire and demonstrate that the truth of our planet is as compelling as any fiction.
+The NASA Earth book is about the intricate and captivating science of our planet, studied 
+through NASA's unique perspective and tools. It presents Earth as a dynamic and complex 
+system, observed through various cycles and processes such as the water cycle and ocean 
+circulation. The book combines stunning satellite images with detailed scientific insights, 
+portraying Earth’s beauty and the continuous interaction of land, wind, water, ice, and 
+air seen from above. It aims to inspire and demonstrate that the truth of our planet is 
+as compelling as any fiction.
 
 Source: page-8.pdf
 ```
@@ -173,13 +179,19 @@ search_results = search_client.search(
 Results from the filtered query should now look similar to the following response. Notice the emphasis on ice cover.
 
 ```
-The NASA Earth book showcases various geographic and environmental features of Earth through satellite imagery, highlighting remarkable landscapes and natural phenomena. 
-
-- It features extraordinary views like the Holuhraun Lava Field in Iceland, captured by Landsat 8 during an eruption in 2014, with false-color images illustrating different elements such as ice, steam, sulfur dioxide, and fresh lava ([source](page-43.pdf)).
-- Other examples include the North Patagonian Icefield in South America, depicted through clear satellite images showing glaciers and their changes over time ([source](page-147.pdf)).
-- It documents melt ponds in the Arctic, exploring their effects on ice melting and heat absorption ([source](page-153.pdf)).
+The NASA Earth book showcases various geographic and environmental features of Earth through 
+satellite imagery, highlighting remarkable landscapes and natural phenomena. 
+
+- It features extraordinary views like the Holuhraun Lava Field in Iceland, captured by 
+Landsat 8 during an eruption in 2014, with false-color images illustrating different elements 
+such as ice, steam, sulfur dioxide, and fresh lava ([source](page-43.pdf)).
+- Other examples include the North Patagonian Icefield in South America, depicted through 
+clear satellite images showing glaciers and their changes over time ([source](page-147.pdf)).
+- It documents melt ponds in the Arctic, exploring their effects on ice melting and 
+- heat absorption ([source](page-153.pdf)).
   
-Overall, the book uses satellite imagery to give insights into Earth's dynamic systems and natural changes.
+Overall, the book uses satellite imagery to give insights into Earth's dynamic systems 
+and natural changes.
 ```
 
 ## Change the inputs
@@ -189,14 +201,20 @@ Increasing or decreasing the number of inputs to the LLM can have a large effect
 Here's one example of what the model returns after increasing the inputs to 8.
 
 ```
-The NASA Earth book features a range of satellite images capturing various natural phenomena across the globe. These include:
-
-- The Holuhraun Lava Field in Iceland documented by Landsat 8 during a 2014 volcanic eruption (Source: page-43.pdf).
-- The North Patagonian Icefield in South America, highlighting glacial landscapes captured in a rare cloud-free view in 2017 (Source: page-147.pdf).
-- The impact of melt ponds on ice sheets and sea ice in the Arctic, with images from an airborne research campaign in Alaska during July 2014 (Source: page-153.pdf).
-- Sea ice formations at Shikotan, Japan, and other notable geographic features in various locations recorded by different Landsat missions (Source: page-168.pdf).
-
-Summary: The book showcases satellite images of diverse Earth phenomena, such as volcanic eruptions, icefields, and sea ice, to provide insights into natural processes and landscapes.
+The NASA Earth book features a range of satellite images capturing various natural phenomena 
+across the globe. These include:
+
+- The Holuhraun Lava Field in Iceland documented by Landsat 8 during a 2014 volcanic 
+eruption (Source: page-43.pdf).
+- The North Patagonian Icefield in South America, highlighting glacial landscapes 
+captured in a rare cloud-free view in 2017 (Source: page-147.pdf).
+- The impact of melt ponds on ice sheets and sea ice in the Arctic, with images from 
+an airborne research campaign in Alaska during July 2014 (Source: page-153.pdf).
+- Sea ice formations at Shikotan, Japan, and other notable geographic features in various 
+locations recorded by different Landsat missions (Source: page-168.pdf).
+
+Summary: The book showcases satellite images of diverse Earth phenomena, such as volcanic 
+eruptions, icefields, and sea ice, to provide insights into natural processes and landscapes.
 ```
 
 Because the model is bound to the grounding data, the answer becomes more expansive as you increase size of the input. You can use relevance tuning to potentially generate more focused answers.
@@ -224,7 +242,8 @@ Sources:\n{sources}
 Output from changing just the prompt, otherwise retaining all aspects of the previous query, might look like this example. 
 
 ```
-The NASA Earth book appears to showcase various locations on Earth captured through satellite imagery, highlighting natural phenomena and geographic features. For instance, the book includes:
+The NASA Earth book appears to showcase various locations on Earth captured through satellite imagery, 
+highlighting natural phenomena and geographic features. For instance, the book includes:
 
 - The Holuhraun Lava Field in Iceland, detailing volcanic activity and its observation via Landsat 8.
 - The North Patagonian Icefield in South America, covering its glaciers and changes over time as seen by Landsat 8.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "記事の更新: NASA Earth Bookに関する説明と例を追加"
}
```

### Explanation
この変更は、Markdown形式の記事「tutorial-rag-build-solution-query.md」における内容の更新を示しており、情報の明確化と詳細化が図られています。合計で35行の追加があり、16行が削除されています。これにより、記事全体の構成が改善され、読みやすさも向上しました。

具体的には、NASA Earth Bookについての記述が詳細に修正され、宇宙からの衛星画像を通じて地球のさまざまな自然現象と地理的特徴がどのように紹介されているかが説明されています。例えば、アイスランドのホルフラウウン火山の風景や、南アメリカの北パタゴニア氷原、北極での氷シートへの融水の影響、シコタン島の海氷の形成など、各例が明確に分けられて示されています。

さらに、入力データの数を変更することにより、モデルがどのように応答を変化させるかについての説明も追加されています。これにより、読者はモデルの調整によって得られるさまざまな応答の違いを理解しやすくなっています。この更新は、NASA Earth Bookの重要なポイントを強調し、より深い理解を促進する役割を果たしています。


