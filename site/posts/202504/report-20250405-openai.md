---
date: '2025-04-05'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a4ad9b8...MicrosoftDocs:f85abdf
summary: 今回の変更は、OpenAI に関連する複数の文書における微調整で構成されており、主にプロンプトエンジニアリング、チャットマークアップ言語、チャットGPTのPowerShellスクリプト、モデルマトリックスに関する軽微な修正が行われました。新機能や破壊的変更は特にないものの、スペルミスや表現の調整、日付や地域情報の更新が施され、一般的な可読性が向上しました。これらの改善により、ユーザーはより正確で明瞭な情報を得ることができ、AIサービスの利用が一層便利になることを目指しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:a4ad9b8...MicrosoftDocs:f85abdf){target="_blank"}

# Highlights
今回の変更は、OpenAI に関連する複数の文書の微調整を含むものであり、具体的にはプロンプトエンジニアリングからチャットマークアップ言語、チャットGPTのPowerShellスクリプトからモデルマトリックスまで、各文書に対して軽微な修正が行われました。

## 新機能
- 特に新機能の追加は行われていません。

## 破壊的変更
- 特に破壊的変更は行われていません。

## その他の更新
- 文書におけるスペルミスや表現の微調整。
- モデルマトリックスやクォータと制限における日付や地域情報の更新。
- いくつかの文書での説明文の調整や冗長な表現の修正。

# Insights
この一連の更新は、OpenAI 関連の文書をより正確で読みやすいものにすることを目的としています。特に、以下の点で改善が見られます。

まず、GPT-4 におけるプロンプトエンジニアリングに関する情報が更新され、ユーザーに対してより明瞭かつ正確なデータが提供されるようにフォーマットが調整されています。この変更は、技術的な利用者がプロンプトを設計する際に、情報の誤解や不一致を防ぎ、効率的なプロンプトエンジニアリングをサポートするためのものです。

チャットマークアップ言語やチャット完了に関する文書では、主にスペルミスの修正が行われました。これにより、ユーザーはシステムが処理する情報に対する理解をより容易にし、特にチャットボットの開発や運用段階での効率が向上することが期待されます。

また、モデルマトリックスとクォータおよび制限に関するセクションでは、日付が最新の情報に更新され、地域を超えたモデルの利用可否が明確に示されるよう修正されています。これにより、グローバルに利用する企業や個人が、最新の状況に基づいた意思決定を行うための情報をより正確に得ることができるようになっています。

最後に、データソースパラメータに関する説明の微調整では、文章内における冗長な表現が削除され、内容が整理されています。これにより、読者が情報を迅速かつ効率的に理解できるよう支援されています。

全体として、これらの修正は文書の正確性と可読性を向上させることを目的としており、ユーザーがAIサービスを活用する際の利便性を高めるものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [gpt-4-v-prompt-engineering.md](#item-fd7772) | minor update | GPT-4とプロンプトエンジニアリングに関する情報の更新 | modified | 1 | 1 | 2 | 
| [chat-markup-language.md](#item-e61acf) | minor update | チャットマークアップ言語に関する説明の修正 | modified | 1 | 1 | 2 | 
| [chat-completion.md](#item-1deb8a) | minor update | チャット完了に関するシステムメッセージの修正 | modified | 1 | 1 | 2 | 
| [chatgpt-powershell.md](#item-c84505) | minor update | チャットGPTのPowerShellスクリプトにおける表現の修正 | modified | 1 | 1 | 2 | 
| [standard-global.md](#item-17a84b) | minor update | モデルマトリックスの更新日および地域データの修正 | modified | 6 | 6 | 12 | 
| [quotas-limits.md](#item-06c6f9) | minor update | クォータと制限に関する日付変更と表現の修正 | modified | 2 | 2 | 4 | 
| [on-your-data.md](#item-c35b1e) | minor update | データソースのパラメータ説明の微調整 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/gpt-4-v-prompt-engineering.md{#item-fd7772}

<details>
<summary>Diff</summary>
````diff
@@ -67,7 +67,7 @@ When you receive a refusal output from a model, there are several ways you can t
 
 |Basic prompt|Model output|
 |--------|-----------|
-| :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: What is this dog breed and what is its average weight and height? | `The dog in the image appears to be a Border Collie. Border Collies are known for their intelligence, agility, and herding abilities.The average weight for a Border Collie is typically around 30-45 pounds (14-20 kilograms). As for height, Border Collies generally stand about 18-22 inches (46-56 centimeters) tall at the shoulder. These figures can vary based on the individual dog's genetics, diet, and level of activity. Border Collies are medium-sized dogs with a well-proportioned body and a high level of energy.` |
+| :::image type="content" source="../media/concepts/gpt-v/border-collie.jpg" lightbox="../media/concepts/gpt-v/border-collie.jpg" alt-text="Photograph of a border collie dog laying in a grass field."::: What is this dog breed and what is its average weight and height? | `The dog in the image appears to be a Border Collie. Border Collies are known for their intelligence, agility, and herding abilities. The average weight for a Border Collie is typically around 30-45 pounds (14-20 kilograms). As for height, Border Collies generally stand about 18-22 inches (46-56 centimeters) tall at the shoulder. These figures can vary based on the individual dog's genetics, diet, and level of activity. Border Collies are medium-sized dogs with a well-proportioned body and a high level of energy.` |
 
 |Updated prompt|Model output|
 |--------|-----------|
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4とプロンプトエンジニアリングに関する情報の更新"
}
```

### Explanation
この変更は、文書「gpt-4-v-prompt-engineering.md」の一部が更新されたことを示しています。具体的には、ボーダーコリーの犬種に関する情報に関して、数行の修正が行われました。修正は一つの行を削除し、新たに一行を追加するもので、内容自体には大きな変更がなく、情報のフォーマットや表現が微調整された結果です。この情報は、利用者がプロンプトエンジニアリングを行う際により明確かつ正確なデータを提供することを目的としています。また、変更のURLを参照することで、具体的なコードの変化を確認することができます。

## articles/ai-services/openai/how-to/chat-markup-language.md{#item-e61acf}

<details>
<summary>Diff</summary>
````diff
@@ -140,7 +140,7 @@ You can also include relevant data or information in the system message to give
 
 ```
 <|im_start|>system
-Assistant is an intelligent chatbot designed to help users answer technical questions about Azure OpenAI Serivce. Only answer questions using the context below and if you're not sure of an answer, you can say "I don't know".
+Assistant is an intelligent chatbot designed to help users answer technical questions about Azure OpenAI Service. Only answer questions using the context below and if you're not sure of an answer, you can say "I don't know".
 
 Context:
 - Azure OpenAI Service provides REST API access to OpenAI's powerful language models including the GPT-3, Codex and Embeddings model series.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットマークアップ言語に関する説明の修正"
}
```

### Explanation
この変更は、「chat-markup-language.md」文書内のシステムメッセージに関する記述の一部修正を示しています。具体的には、「Azure OpenAI Service」というフレーズにおいて、スペルミスが修正されました。この変更によって、ユーザーがチャットボットに関して正確な情報を得られるようになり、技術的な質問に対する回答がより効果的に行えることを目指しています。修正された部分は文書内の140行目付近に位置し、変更後の内容がより正確かつ効果的になっています。詳細な変更内容は、提供されたURLから確認できます。

## articles/ai-services/openai/includes/chat-completion.md{#item-1deb8a}

<details>
<summary>Diff</summary>
````diff
@@ -187,7 +187,7 @@ Instructions:
 You can also include relevant data or information in the system message to give the model extra context for the conversation. If you need to include only a small amount of information, you can hard code it in the system message. If you have a large amount of data that the model should be aware of, you can use [embeddings](../tutorials/embeddings.md?tabs=command-line) or a product like [Azure AI Search](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087) to retrieve the most relevant information at query time.
 
 ```
-{"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer technical questions about Azure OpenAI Serivce. Only answer questions using the context below and if you're not sure of an answer, you can say 'I don't know'.
+{"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer technical questions about Azure OpenAI Service. Only answer questions using the context below and if you're not sure of an answer, you can say 'I don't know'.
 
 Context:
 - Azure OpenAI Service provides REST API access to OpenAI's powerful language models including the GPT-3, Codex and Embeddings model series.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャット完了に関するシステムメッセージの修正"
}
```

### Explanation
この変更は、「chat-completion.md」文書内にあるシステムメッセージの一部におけるスペルの修正を示しています。具体的には、「Azure OpenAI Serivce」という表現が「Azure OpenAI Service」に修正され、より正確な情報が提供されるようになりました。このマイナーな修正は、ユーザーがチャットボットを使用する際に誤解を避け、技術的な質問への応答が正確になることを目的としています。修正箇所は187行目付近にあり、詳細は提供されたURLから確認することができます。

## articles/ai-services/openai/includes/chatgpt-powershell.md{#item-c84505}

<details>
<summary>Diff</summary>
````diff
@@ -66,7 +66,7 @@ For the recommended keyless authentication with Microsoft Entra ID, you need to:
     }
     $messages += @{
       role = 'assistant'
-      content = 'Yes, you can use use honey as a substitute for sugar.'
+      content = 'Yes, you can use honey as a substitute for sugar.'
     }
     $messages += @{
       role = 'user'
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットGPTのPowerShellスクリプトにおける表現の修正"
}
```

### Explanation
この変更は、「chatgpt-powershell.md」ファイルの中で使用されている文の修正を示しています。具体的には、手順における内容の重複を解消するために、「use use」という誤った文言が「use」に修正されました。この修正により、より明確で正確な情報が提供され、ユーザーがスクリプトの内容を理解しやすくなることを目指しています。変更は66行目付近で行われており、詳細は提供されたURLを通じて確認することができます。

## articles/ai-services/openai/includes/model-matrix/standard-global.md{#item-17a84b}

<details>
<summary>Diff</summary>
````diff
@@ -6,19 +6,19 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
 ms.custom: references_regions
-ms.date: 04/02/2025
+ms.date: 04/04/2025
 ---
 
 | **Region**     | **gpt-4.5-preview**, **2025-02-27**   | **o3-mini**, **2025-01-31**   | **o1**, **2024-12-17**   | **o1-preview**, **2024-09-12**   | **o1-mini**, **2024-09-12**   | **gpt-4o**, **2024-05-13**   | **gpt-4o**, **2024-08-06**   | **gpt-4o**, **2024-11-20**   | **gpt-4o-mini**, **2024-07-18**   | **gpt-4o-realtime-preview**, **2024-12-17**   | **gpt-4o-audio-preview**, **2024-12-17**   | **gpt-4o-mini-realtime-preview**, **2024-12-17**   | **gpt-4o-mini-audio-preview**, **2024-12-17**   | **gpt-4**, **turbo-2024-04-09**   | **text-embedding-3-small**, **1**   | **text-embedding-3-large**, **1**   | **text-embedding-ada-002**, **2**   |
 |:-------------------|:-----------------------------------:|:---------------------------:|:----------------------:|:------------------------------:|:---------------------------:|:--------------------------:|:--------------------------:|:--------------------------:|:-------------------------------:|:-------------------------------------------:|:----------------------------------------:|:------------------------------------------------:|:---------------------------------------------:|:-------------------------------:|:---------------------------------:|:---------------------------------:|:---------------------------------:|
-| australiaeast      | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| australiaeast      | -                               | ✅                        | -                  | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | brazilsouth        | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | canadaeast         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | eastus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | ✅                                          | ✅                            | ✅                              | ✅                              | ✅                              |
 | eastus2            | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | ✅                                          | ✅                            | ✅                              | ✅                              | -                             |
 | francecentral      | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | germanywestcentral | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| italynorth         | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | -                             | -                             | -                             |
+| italynorth         | -                               | ✅                        | ✅                   | -                          | -                       | -                      | -                      | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | -                           | ✅                              | ✅                              | ✅                              |
 | japaneast          | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | koreacentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | northcentralus     | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
@@ -28,10 +28,10 @@ ms.date: 04/02/2025
 | southcentralus     | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | southindia         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | spaincentral       | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| swedencentral      | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| swedencentral      | ✅                                | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | ✅                                        | ✅                                     | ✅                                             | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | switzerlandnorth   | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | uaenorth           | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| uksouth            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
+| uksouth            | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | ✅                              |
 | westeurope         | -                               | ✅                        | ✅                   | -                          | -                       | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
 | westus             | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
-| westus3            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
\ No newline at end of file
+| westus3            | -                               | ✅                        | ✅                   | ✅                           | ✅                        | ✅                       | ✅                       | ✅                       | ✅                            | -                                       | -                                    | -                                            | -                                         | ✅                            | ✅                              | ✅                              | -                             |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルマトリックスの更新日および地域データの修正"
}
```

### Explanation
この変更は、「standard-global.md」ファイルにおけるモデルマトリックスの更新を含んでいます。主な修正点は、日時の更新（04/02/2025から04/04/2025への変更）といくつかの地域における情報の追加や修正です。具体的には、いくつかの地域の対応するモデルの利用可否を示すチェックマークの更新が行われました。この変更により、最新のモデル情報と利用可能な地域が反映され、ユーザーがより正確なデータを使用できるようになります。変更の詳細は指定されたURLから確認することができます。

## articles/ai-services/openai/quotas-limits.md{#item-06c6f9}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: conceptual
-ms.date: 4/02/2025
+ms.date: 4/04/2025
 ms.author: mbullwin
 ---
 
@@ -203,7 +203,7 @@ If your Azure subscription is linked to certain [offer types](https://azure.micr
 |Tier| Quota Limit in tokens per minute (TPM) |
 |---|:---|
 |Azure for Students, Free Trials | 1 K (all models) <br>Exception o-series & GPT 4.5 Preview: 0|
-| MSDN & Cloud Solution Provider (CSP) subscriptions | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
+| MSDN | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> gpt-4o-realtime-preview: 1 K <br> o-series: 0 <br> GPT 4.5 Preview: 0  |
 | Monthly credit card based subscriptions <sup>1</sup> | GPT 3.5 Turbo Series: 30 K <br> GPT-4 series: 8 K <br>computer-use-preview: 30 K <br> o-series: 0 <br> GPT 4.5 Preview: 0   |
 
 <sup>1</sup> This currently applies to [offer type 0003P](https://azure.microsoft.com/support/legal/offer-details/)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータと制限に関する日付変更と表現の修正"
}
```

### Explanation
この変更は、「quotas-limits.md」ファイルに関するもので、主に更新日と表現の修正が行われています。具体的には、更新日が「4/02/2025」から「4/04/2025」に変更されており、また「MSDN & Cloud Solution Provider (CSP) subscriptions」という表記が「MSDN」に短縮されています。クォータの内容自体は変わっていないものの、文書の整合性を向上させるために微修正が加えられました。この変更により、ユーザーは最新の情報を得ることができ、より明確な表現で内容を理解できるようになります。変更の詳細は、提供されたURLから確認することができます。

## articles/ai-services/openai/references/on-your-data.md{#item-c35b1e}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ The request body inherits the same schema of chat completions API request. This
 
 |Name | Type | Required | Description |
 |--- | --- | --- | --- |
-| `data_sources` | [DataSource](#data-source)[] | True | The configuration entries for Azure OpenAI On Your Data. There must be exactly one element in the array. If `data_sources` is not provided, the service uses chat completions model directly, and does not use Azure OpenAI On Your Data. When you specify the `data_sources` parameter, you won't be able to to use the `logprobs` or `top_logprobs` parameters. |
+| `data_sources` | [DataSource](#data-source)[] | True | The configuration entries for Azure OpenAI On Your Data. There must be exactly one element in the array. If `data_sources` is not provided, the service uses chat completions model directly, and does not use Azure OpenAI On Your Data. When you specify the `data_sources` parameter, you won't be able to use the `logprobs` or `top_logprobs` parameters. |
 
 ## Response body
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソースのパラメータ説明の微調整"
}
```

### Explanation
この変更は、「on-your-data.md」ファイルにおける「data_sources」パラメータの説明に関連しています。1行の追加および削除が行われており、説明の文言に若干の調整が加えられました。具体的には、説明文中の「to use」が削除されたことにより文が整理され、より明確な表現となっています。これにより、ユーザーが「data_sources」についての理解を深める助けになることを目的としています。変更内容の詳細は、提供されたURLから確認することができます。


