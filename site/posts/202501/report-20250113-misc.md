---
date: '2025-01-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:28bc1fd...MicrosoftDocs:70337bc
summary: この更新では、主にAzure AI Document IntelligenceとAzure AI Studioのドキュメントに関連する動画リンクの更新、内容の充実化、レビュアーの変更、コードサンプルのパスの修正が行われました。最新情報へのアクセスを容易にするためにリンクが更新され、ユーザーの利便性を高めるための改善が実施されています。特に、ビデオリンクのGUID形式への更新や、Azure
  Blobストレージアカウントのアクセス制御設定方法が詳述されており、ユーザー体験の向上が期待されます。また、安全評価に関する情報が強化され、リスクに対する透明性が向上しました。全体として、Azure
  AIの利用者はより確実な情報を得られるようになり、プロジェクトの成功が支援されることが目指されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:28bc1fd...MicrosoftDocs:70337bc){target="_blank"}

# Highlights
この更新には主に、Azure AI Document IntelligenceとAzure AI Studioの各種ドキュメント内の動画リンクの更新や、内容の充実化、レビュアーの変更、コードサンプルのパスの修正が含まれています。最新の情報にアクセス可能とするためのリンクの更新と、ユーザーの利便性を高めるためのドキュメントの改善が実施されました。

## New features
- ビデオリンクを最新のGUID形式に更新し、ユーザーが最新の情報にアクセスしやすくする。
- フロー開発手順で新たにAzure Blobストレージアカウントのアクセス制御設定方法を詳述。

## Breaking changes
- 特に破壊的な変更はなし。

## Other updates
- 安全評価に関する記事のタイトルと内容が強化。
- フロー展開および開発手順のレビュアーが更新。
- チャットアプリのコードサンプルのパスが新しいリポジトリ構造に合わせて修正。
- Copilot SDKの評価チュートリアルで、パッケージのインストール手順が修正。

# Insights
この一連の更新は、主にAzure AIのドキュメントを最新の状態に保つことを目的としています。特に、利用頻度の高いビデオリンクの更新は、ユーザーがより容易に最新の情報や学習資料にアクセスできるようにするための重要な施策です。古いリンクが新しいGUID形式に更新されたことで、ユーザー体験の向上が見込めます。

さらに、Azure AI Studio関連の文書の改善も行われており、特にフロー開発に関する内容の更新は、プロジェクト内での実際の操作方法をより具体的に理解するのに役立つ情報を提供しています。これにより、利用者がAzure Blobストレージアカウントへのアクセスを適切に設定し、効率的に利用できるようになります。また、手続きの明確化は、ユーザーがプロジェクトをスムーズに進行させる助けとなるでしょう。

安全評価に関する更新では、AIシステムのリスクに関する透明性が強化され、特にさまざまな危険性を詳述することによって、ユーザーに対抗策を与える重要な情報が追加されています。レビュアーの更新も品質管理に貢献し、製品の信用性を高めるための努力が顕著です。

最後に、こうした更新によって、Azure AIの利用者はより確実な情報を得て、プロジェクトの成功に向けた手続きを確実に行えるようになったと考えられます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [choose-model-feature.md](#item-6ea879) | minor update | モデル選択機能の動画リンクの更新 | modified | 1 | 1 | 2 | 
| [build-a-custom-model.md](#item-4f2040) | minor update | カスタムモデル作成ガイドの動画リンクの更新 | modified | 1 | 1 | 2 | 
| [custom-label-tips.md](#item-041f5c) | minor update | カスタムラベルティップスの記事の動画リンクの更新 | modified | 1 | 1 | 2 | 
| [safety-evaluations-transparency-note.md](#item-a4dacb) | minor update | Azure AI Foundry安全評価の記事のタイトルと内容の更新 | modified | 15 | 12 | 27 | 
| [flow-deploy.md](#item-e7fc64) | minor update | フロー展開手順の記事のレビュアー変更 | modified | 1 | 1 | 2 | 
| [flow-develop.md](#item-d1ac3e) | minor update | フロー開発手順の記事の内容更新 | modified | 14 | 3 | 17 | 
| [get-started-code.md](#item-8a5082) | minor update | チャットアプリのコードサンプルのパス修正 | modified | 3 | 3 | 6 | 
| [copilot-sdk-evaluate.md](#item-bb5754) | minor update | 評価パッケージインストールの手順修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/choose-model-feature.md{#item-6ea879}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,7 @@ ms.author: lajanuar
 
 Azure AI Document Intelligence supports a wide variety of models that enable you to add intelligent document processing to your applications and optimize your workflows. Selecting the right model is essential to ensure the success of your enterprise. In this article, we explore the available Document Intelligence models and provide guidance for how to choose the best solution for your projects.
 
-> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE5fX1b]
+> [!VIDEO 364078d4-14bc-4b16-995a-526db31ea1ee]
 
 The following decision charts highlight the features of each supported model to help you choose the model that best meets the needs and requirements of your application.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル選択機能の動画リンクの更新"
}
```

### Explanation
この修正は、Azure AI Document Intelligence のドキュメントにおけるモデル選択に関するビデオリンクの更新を含んでいます。具体的には、元のビデオリンクを新しい GUID 格式のリンクに交換しました。この変更により、読者は最新のビデオコンテンツを通じて、利用可能なドキュメントインテリジェンスモデルに関してより適切な情報を得られるようになります。ドキュメントは、アプリケーションのニーズに合わせたモデル選択をするためのガイダンスを提供しています。この更新により、情報の最新性が保たれ、ユーザーは今後のプロジェクトに最適なソリューションを選択するのに役立つでしょう。

## articles/ai-services/document-intelligence/how-to-guides/build-a-custom-model.md{#item-4f2040}

<details>
<summary>Diff</summary>
````diff
@@ -43,7 +43,7 @@ Once you gather a set of forms or documents for training, you need to upload it
 
 * Once you gather and upload your training dataset, you're ready to train your custom model. In the following video, we create a project and explore some of the fundamentals for successfully labeling and training a model.
 
-> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE5fX1c]
+> [!VIDEO b716cdc7-3c23-4c69-a2ef-e131166f792b]
 
 ## Create a project in the Document Intelligence Studio
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデル作成ガイドの動画リンクの更新"
}
```

### Explanation
この修正は、Azure AI Document Intelligence におけるカスタムモデルの作成に関するガイド内のビデオリンクが更新される内容です。具体的には、以前のビデオリンクが新しい GUID 形式のリンクに置き換えられています。この変更は、ユーザーがカスタムモデルのラベリングとトレーニングに関する基本を視覚的に学ぶために必要な情報を提供するものです。新しいビデオリンクにより、最新の内容にアクセスできるようになり、より良い学習体験が促進されます。この更新は、ユーザーがドキュメントインテリジェンススタジオで成功裏にプロジェクトを作成する手助けをすることを目的としています。

## articles/ai-services/document-intelligence/train/custom-label-tips.md{#item-041f5c}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ This article highlights the best methods for labeling custom model datasets in t
 
 * We examine best practices for labeling your selected documents. With semantically relevant and consistent labeling, you should see an improvement in model performance.
 
-> [!VIDEO https://www.microsoft.com/en-us/videoplayer/embed/RE5fZKB]
+> [!VIDEO cae72200-eeca-4897-8ca7-2e91696cac83]
 
 ### Search
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムラベルティップスの記事の動画リンクの更新"
}
```

### Explanation
この修正は、カスタムモデルのデータセットラベリングに関するベストプラクティスを強調した記事内のビデオリンクの更新を含んでいます。具体的には、既存のビデオリンクが新しい GUID 形式のリンクに置き換えられています。この変更により、ユーザーは最新の情報やトレーニング手法に基づくビデオコンテンツを通じて、より効果的にカスタムモデルのラベリング方法について学ぶことができるようになります。ビデオは、セマンティックに関連して一貫したラベリングの重要性を説明し、モデルのパフォーマンス向上に寄与する内容です。この更新は、ドキュメントインテリジェンスのトレーニングプロセスを向上させるための重要な一歩となります。

## articles/ai-studio/concepts/safety-evaluations-transparency-note.md{#item-a4dacb}

<details>
<summary>Diff</summary>
````diff
@@ -1,19 +1,19 @@
 ---
-title: Transparency Note for Azure AI Foundry safety evaluations
+title:  Azure AI Foundry risk and safety evaluations (preview) Transparency Note
 titleSuffix: Azure AI Foundry
 description: Azure AI Foundry safety evaluations intended purpose, capabilities, limitations and how to achieve the best performance.
 manager: scottpolly
 ms.service: azure-ai-studio
 ms.custom:
   - build-2024
 ms.topic: article
-ms.date: 11/21/2024
+ms.date: 01/10/2025
 ms.reviewer: mithigpe
 ms.author: lagayhar
 author: lgayhardt
 ---
 
-# Transparency Note for Azure AI Foundry safety evaluations
+# Azure AI Foundry risk and safety evaluations (preview) Transparency Note
 
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
@@ -23,27 +23,30 @@ An AI system includes not only the technology, but also the people who will use
 
 Microsoft's Transparency Notes are part of a broader effort at Microsoft to put our AI Principles into practice. To find out more, see the [Microsoft AI principles](https://www.microsoft.com/en-us/ai/responsible-ai).
 
-## The basics of Azure AI Foundry safety evaluations
+## The basics of Azure AI Foundry risk and safety evaluations (preview)
 
 ### Introduction
 
-The Azure AI Foundry portal safety evaluations let users evaluate the output of their generative AI application for textual content risks: hateful and unfair content, sexual content, violent content, self-harm-related content, jailbreak vulnerability. Safety evaluations can also help generate adversarial datasets to help you accelerate and augment the red-teaming operation. Azure AI Foundry safety evaluations reflect Microsoft's commitments to ensure AI systems are built safely and responsibly, operationalizing our Responsible AI principles.
+The Azure AI Foundry risk and safety evaluations let users evaluate the output of their generative AI application for textual content risks: hateful and unfair content, sexual content, violent content, self-harm-related content, direct and indirect jailbreak vulnerability, and protected material in content. Safety evaluations can also help generate adversarial datasets to help you accelerate and augment the red-teaming operation. Azure AI Foundry safety evaluations reflect Microsoft's commitments to ensure AI systems are built safely and responsibly, operationalizing our Responsible AI principles.
 
 ### Key terms
 
-- **Hateful and unfair content** refers to any language pertaining to hate toward or unfair representations of individuals and social groups along factors including but not limited to race, ethnicity, nationality, gender, sexual orientation, religion, immigration status, ability, personal appearance, and body size. Unfairness occurs when AI systems treat or represent social groups inequitably, creating or contributing to societal inequities.
-- **Sexual content** includes language pertaining to anatomical organs and genitals, romantic relationships, acts portrayed in erotic terms, pregnancy, physical sexual acts (including assault or sexual violence), prostitution, pornography, and sexual abuse.
-- **Violent content** includes language pertaining to physical actions intended to hurt, injure, damage, or kill someone or something. It also includes descriptions of weapons and guns (and related entities such as manufacturers and associations).
-- **Self-harm-related content** includes language pertaining to actions intended to hurt, injure, or damage one's body or kill oneself.
-- **Jailbreak**, direct prompt attacks, or user prompt injection attacks, refer to users manipulating prompts to inject harmful inputs into LLMs to distort actions and outputs. An example of a jailbreak command is a 'DAN' (Do Anything Now) attack, which can trick the LLM into inappropriate content generation or ignoring system-imposed restrictions.  
+- **Hateful and unfair content (for text and images)** refers to any language or imagery pertaining to hate toward or unfair representations of individuals and social groups along factors including but not limited to race, ethnicity, nationality, gender, sexual orientation, religion, immigration status, ability, personal appearance, and body size. Unfairness occurs when AI systems treat or represent social groups inequitably, creating or contributing to societal inequities.
+- **Sexual content (for text and images)** includes language or imagery pertaining to anatomical organs and genitals, romantic relationships, acts portrayed in erotic terms, pregnancy, physical sexual acts (including assault or sexual violence), prostitution, pornography, and sexual abuse.
+- **Violent content (for text and images)** includes language or imagery  pertaining to physical actions intended to hurt, injure, damage, or kill someone or something. It also includes descriptions of weapons and guns (and related entities such as manufacturers and associations).
+- **Self-harm-related content (for text and images)** includes language or imagery pertaining to actions intended to hurt, injure, or damage one's body or kill oneself.
+- **Protected material content (for text)** known textual content, for example, song lyrics, articles, recipes, and selected web content, that might be output by large language models. By detecting and preventing the display of protected material, organizations can maintain compliance with intellectual property rights and preserve content originality.
+- **Protected material content (for images)** refers to certain protected visual content, that is protected by copyright such as logos and brands, artworks, or fictional characters. The system uses an image-to-text foundation model to identify whether such content is present.
+- **Direct jailbreak**, direct prompt attacks, or user prompt injection attacks, refer to users manipulating prompts to inject harmful inputs into LLMs to distort actions and outputs. An example of a jailbreak command is a 'DAN' (Do Anything Now) attack, which can trick the LLM into inappropriate content generation or ignoring system-imposed restrictions.  
+- **Indirect jailbreak** indirect prompt attacks or cross-domain prompt injection attacks, refers to when malicious instructions are hidden within data that an AI system processes or generates grounded content from. This data can include emails, documents, websites, or other sources not directly authored by the developer or user and can lead to inappropriate content generation or ignoring system-imposed restrictions.
 - **Defect rate (content risk)** is defined as the percentage of instances in your test dataset that surpass a threshold on the severity scale over the whole dataset size.
 - **Red-teaming** has historically described systematic adversarial attacks for testing security vulnerabilities. With the rise of Large Language Models (LLM), the term has extended beyond traditional cybersecurity and evolved in common usage to describe many kinds of probing, testing, and attacking of AI systems. With LLMs, both benign and adversarial usage can produce potentially harmful outputs, which can take many forms, including harmful content such as hateful speech, incitement or glorification of violence, reference to self-harm-related content or sexual content.
 
 ## Capabilities
 
 ### System behavior
 
-Azure AI Foundry provisions an Azure OpenAI GPT-4 model and orchestrates adversarial attacks against your application to generate a high quality test dataset. It then provisions another GPT-4 model to annotate your test dataset for content and security. Users provide their generative AI application endpoint that they wish to test, and the safety evaluations will output a static test dataset against that endpoint along with its content risk label (Very low, Low, Medium, High) and reasoning for the AI-generated label.
+Azure AI Foundry provisions a fine-tuned Azure OpenAI GPT-4o model and orchestrates adversarial attacks against your application to generate a high quality test dataset. It then provisions another GPT-4o model to annotate your test dataset for content and security. Users provide their generative AI application endpoint that they wish to test, and the safety evaluations will output a static test dataset against that endpoint along with its content risk label (Very low, Low, Medium, High) or content risk detection label (True or False) and reasoning for the AI-generated label.
 
 ### Use cases
 
@@ -88,7 +91,7 @@ We encourage customers to leverage Azure AI Foundry safety evaluations in their
 
 ### Evaluation methods
 
-For all supported content risk types, we have internally checked the quality by comparing the rate of approximate matches between human labelers using a 0-7 severity scale and the safety evaluations' automated annotator also using a 0-7 severity scale on the same datasets. For each risk area, we had both human labelers and an automated annotator label 500 English, single-turn texts. The human labelers and the automated annotator didn't use exactly the same versions of the annotation guidelines; while the automated annotator's guidelines stemmed from the guidelines for humans, they have since diverged to varying degrees (with the hate and unfairness guidelines having diverged the most). Despite these slight to moderate differences, we believe it's still useful to share general trends and insights from our comparison of approximate matches. In our comparisons, we looked for matches with a 2-level tolerance (where human label matched automated annotator label exactly or was within 2 levels above or below in severity), matches with a 1-level tolerance, and matches with a 0-level tolerance.
+For all supported content risk types, we have internally checked the quality by comparing the rate of approximate matches between human labelers using a 0-7 severity scale and the safety evaluations' automated annotator also using a 0-7 severity scale on the same datasets. For each risk area, we had both human labelers and an automated annotator label 500 English, single-turn texts, 250 single-turn text-to-image generations,  and 250 multi-modal text with image-to-text generations. The human labelers and the automated annotator didn't use exactly the same versions of the annotation guidelines; while the automated annotator's guidelines stemmed from the guidelines for humans, they have since diverged to varying degrees (with the hate and unfairness guidelines having diverged the most). Despite these slight to moderate differences, we believe it's still useful to share general trends and insights from our comparison of approximate matches. In our comparisons, we looked for matches with a 2-level tolerance (where human label matched automated annotator label exactly or was within 2 levels above or below in severity), matches with a 1-level tolerance, and matches with a 0-level tolerance.
 
 ### Evaluation results
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry安全評価の記事のタイトルと内容の更新"
}
```

### Explanation
この修正は、Azure AI Foundryのリスクおよび安全評価に関する透明性ノートの記事のタイトルを更新し、内容を強化するものです。タイトルが「Transparency Note for Azure AI Foundry safety evaluations」から「Azure AI Foundry risk and safety evaluations (preview) Transparency Note」に変更され、ドキュメントの焦点がより明確に示されています。また、内容にはリスクおよび安全評価に関する詳細な説明が追加され、特にさまざまなテキストおよび画像に関連するリスクが強調されています。

具体的には、「Hateful and unfair content」や「Sexual content」などのリスクについての説明が、テキストと画像両方に適用されるように更新され、さらに「Protected material」に関する新しい定義も追加されています。また、AIシステムの動作や評価方法についての説明も強化されており、実際の人間のラベル付けと自動アノテーターとの比較が行われたデータについても記述が加わっています。この更新は、Azure AI Foundryの安全評価ツールを使用する際に、ユーザーがより良く理解し、評価を行う手助けをすることを目的としています。

## articles/ai-studio/how-to/flow-deploy.md{#item-e7fc64}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2024
 ms.topic: how-to
 ms.date: 5/21/2024
-ms.reviewer: likebupt
+ms.reviewer: gmuthukumar
 ms.author: lagayhar
 author: lgayhardt
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フロー展開手順の記事のレビュアー変更"
}
```

### Explanation
この変更は、Azure AI Studioのフロー展開に関する手順の記事におけるレビュアーの情報を更新するものです。以前のレビュアーである「likebupt」が「gmuthukumar」に変更されました。この修正は、文書の品質管理プロセスを確保するためのもので、更新されたレビュアーによってレビューされた内容がより良いものになることを期待しています。文書の作成者やトピック、日付などは変更されていませんが、レビュアーの更新は、コンテンツの正確性と信頼性を向上させるために重要なステップです。

## articles/ai-studio/how-to/flow-develop.md{#item-d1ac3e}

<details>
<summary>Diff</summary>
````diff
@@ -9,8 +9,8 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/08/2024
-ms.reviewer: jinzhong
+ms.date: 01/10/2025
+ms.reviewer: gmuthukumar
 ms.author: lagayhar
 author: lgayhardt
 ---
@@ -34,14 +34,25 @@ In this article, you learn how to create and develop your first prompt flow in A
 - If you don't have an Azure AI Foundry project already, first [create a project](create-projects.md).
 - Prompt flow requires a compute session. If you don't have a runtime, you can [create one in Azure AI Foundry portal](./create-manage-compute-session.md).
 - You need a deployed model.
-
+- In your project, configure access control for the blog storage account. Assign the **Storage Blob Data Contributor** role to your user account.
+    - In the bottom left of the Azure AI Foundry portal, select **Management center**.
+    - In **Connected resources** for your project, select the link that corresponds to the **Azure Blob Storage** type. 
+    - Select **View in Azure Portal**
+    - In the Azure portal, select **Access control (IAM)**.
+    - Select **Add>Add role assignment**.
+    - Search for **Storage Blob Data Contributor**, then select it.
+    - Use the **Add role assignment** page to add yourself as a member.
+    - Select **Review + assign** to review the assignment.
+    - Select **Review + assign** to assign the role.
+    
 ## Create and develop your Prompt flow
 
 You can create a flow by either cloning the samples available in the gallery or creating a flow from scratch. If you already have flow files in local or file share, you can also import the files to create a flow.
 
 To create a prompt flow from the gallery in Azure AI Foundry portal:
 
 1. Sign in to [Azure AI Foundry](https://ai.azure.com) and select your project. 
+1. If you're in the Management center, select **Go to project** to return to your project.
 1. From the collapsible left menu, select **Prompt flow**.
 1. Select **+ Create**.
 1. In the **Standard flow** tile, select **Create**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "フロー開発手順の記事の内容更新"
}
```

### Explanation
この修正は、Azure AI Studioのフロー開発に関する手順の記事を更新したもので、主に内容の充実が図られています。具体的には、前回の日付が「2024年11月8日」から「2025年1月10日」に変更され、レビュアーも「jinzhong」から「gmuthukumar」に変更されています。これにより、最新のレビューとコンテンツの更新が反映されます。

内容の追加として、プロジェクト内でのAzure Blobストレージアカウントのアクセス制御を設定する方法が具体的に詳述されており、ユーザーは役割の割り当て手順に従うことで、ストレージへの適切なアクセスを確保することができます。この情報は、Azure AI Foundryを利用する際の重要なステップであり、ユーザーにとって有益な変更となっています。全体として、この更新により、フローの作成と開発に関するプロセスがさらに明確になり、ユーザーが手続きを円滑に進める手助けとなることを目的としています。

## articles/ai-studio/quickstarts/get-started-code.md{#item-8a5082}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ pip install azure-ai-projects azure-ai-inference azure-identity
 
 Create a file named **chat.py**.  Copy and paste the following code into it.
 
-:::code language="python" source="~/azureai-samples-temp/scenarios/inference/chat-app/chat-simple.py":::
+:::code language="python" source="~/azureai-samples-main/scenarios/projects/basic/chat-simple.py":::
 
 ## Insert your connection string
 
@@ -72,7 +72,7 @@ Let's change the script to take input from a client application and generate a s
 
 1. Now define a `get_chat_response` function that takes messages and context, generates a system message using a prompt template, and calls a model.  Add this code to your  existing **chat.py** file:
 
-    :::code language="python" source="~/azureai-samples-temp/scenarios/inference/chat-app/chat-template.py" id="chat_function":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/projects/basic/chat-template.py" id="chat_function":::
 
     > [!NOTE]
     > The prompt template uses mustache format.
@@ -81,7 +81,7 @@ Let's change the script to take input from a client application and generate a s
 
 1. Now simulate passing information from a frontend application to this function.  Add the following code to the end of your **chat.py** file.  Feel free to play with the message and add your own name.
 
-    :::code language="python" source="~/azureai-samples-temp/scenarios/inference/chat-app/chat-template.py" id="create_response":::
+    :::code language="python" source="~/azureai-samples-main/scenarios/projects/basic/chat-template.py" id="create_response":::
 
 Run the revised script to see the response from the model with this new input.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットアプリのコードサンプルのパス修正"
}
```

### Explanation
この修正は、Azure AI Studioの「はじめに」セクションに関連するチャットアプリケーションのコードサンプルのパスを更新する内容です。これにより、旧いパスが新しいリポジトリの構造に合わせて変更されています。具体的には、いくつかのコードスニペットのソースが「~/azureai-samples-temp/scenarios/inference/chat-app/」から「~/azureai-samples-main/scenarios/projects/basic/」に変更されました。

この更新は、ユーザーが最新のコードを容易に取得できるようにし、正しいディレクトリ構造を反映しています。また、ユーザーがチャットアプリケーションの機能を実装する際に必要な情報をスムーズに取得できるようにするための重要な修整です。全体として、この修正により、ドキュメントの信頼性が高まり、ユーザーの学習体験が向上します。

## articles/ai-studio/tutorials/copilot-sdk-evaluate.md{#item-bb5754}

<details>
<summary>Diff</summary>
````diff
@@ -99,7 +99,7 @@ In Part 1 of this tutorial series, you created an **.env** file that specifies t
 1. Install the required package:
 
     ```bash
-    pip install azure-ai-evaluation
+    pip install azure-ai-evaluation[remote]
     ```
 
 1. Now run the evaluation script:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価パッケージインストールの手順修正"
}
```

### Explanation
この修正は、Azure AI Studioにおける「Copilot SDKの評価」チュートリアルの手順を更新したものです。特に、必要なパッケージのインストール手順が変更されました。変更前は「pip install azure-ai-evaluation」となっていましたが、変更後は「pip install azure-ai-evaluation[remote]」に修正されています。

この更新は、ユーザーがリモート機能を利用するために必要なパッケージを正しくインストールできるようにするための重要な改善です。結果として、ユーザーが正確な手順に従い、評価スクリプトを円滑に実行できるようになります。全体として、これによりチュートリアルの利便性が向上し、実行時のエラーを減少させることが期待されます。


