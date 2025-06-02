---
date: '2025-06-02'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca0291a...MicrosoftDocs:178e7a4
summary: このコードの変更は、文書の追加や新しい画像ファイルの導入に関するもので、全体的に日付の更新や情報の詳細化、新しい項目の追加が行われました。特に評価に関するセクションには視覚的コンテンツが追加されています。評価手順をサポートするための新しい画像ファイルが追加されており、重大な破壊的変更はありません。多くのファイルで日付が更新され、文書の可読性も向上しました。これにより、ユーザーは評価プロセスや手順をより深く理解しやすくなっています。新しい画像の追加は、特に評価手順を明確にし、ユーザーの学習効果を向上させる重要な措置です。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca0291a...MicrosoftDocs:178e7a4){target="_blank"}

<format>
# Highlights
このコードの変更は、複数の文書および、新しい画像ファイルの追加に関するもので、全体的に日付の更新、情報の詳細化や新しい項目の追加を行っています。特に評価に関するセクションでは、視覚的コンテンツが新たに追加されました。

## New features
- `create-new-eval.png`や`eval-semantic-similarity-1.png`などの、新しい画像ファイルが評価手順の視覚化をサポートするために追加されました。

## Breaking changes
- 特に重大な変更や破壊的な変更はありませんでした。すべての修正はマイナーアップデートとして扱われ、既存の機能に悪影響を及ぼすことは想定されていません。

## Other updates
- 多くのファイルで日付（`ms.date`）が更新され、文書の新鮮さが維持されました。
- いくつかのドキュメントでは文の簡略化や表現の改善が行われ、可読性が向上しました。

# Insights
今回の変更は、Azure OpenAIの活用において、ユーザーが対象となる評価プロセスや手順をより深く理解しやすくする目的で行われたものです。具体的には、評価に関する文書に多数の視覚的要素が追加されており、これにより読者が評価手順を直感的に把握しやすくなっています。

日付の更新により、各ドキュメントの最新性や信頼性が強調されています。この日付の更新は、非常に重要な要素であり、公式なガイドラインや手順が常に最新の状態を保っていることを示します。

また、プロンプトエンジニアリングやリスク・安全性モニタリングに関するドキュメントの情報が最大限に活用されるよう、細かい表現の更新が行われ、これにより明瞭性が向上しています。ユーザーへの情報伝達が効率的になるように設計されており、場合によっては直接的な指示形が使われるなど、文書内のトーンも最適化されています。

新たな画像の追加は、特に評価手順の具体的な段階での視点を明確にし、システムを扱う際の学習効果をより良いものにするための重要な措置です。こうした視覚的補助は、複雑な操作を伴うプロジェクトやアプリケーションにおいて、ユーザーの理解を助け、新しいシステムの活用の一助となります。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [default-safety-policies.md](#item-39b6a0) | minor update | デフォルトの安全ポリシーの更新 | modified | 1 | 1 | 2 | 
| [gpt-4-v-prompt-engineering.md](#item-fd7772) | minor update | GPT-4およびプロンプトエンジニアリングに関する文書の更新 | modified | 2 | 2 | 4 | 
| [gpt-with-vision.md](#item-991388) | minor update | GPTモデルに関する文書の更新 | modified | 12 | 12 | 24 | 
| [prompt-transformation.md](#item-21e047) | minor update | プロンプト変換に関する文書の日付更新 | modified | 1 | 1 | 2 | 
| [dall-e-quickstart.md](#item-fcd528) | minor update | DALL·Eクイックスタートの文書の日付更新 | modified | 1 | 1 | 2 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | GPT-Vクイックスタートガイドの内容と日付更新 | modified | 3 | 7 | 10 | 
| [evaluations.md](#item-dfaa1c) | minor update | 評価ガイドの内容拡充と新機能の追加 | modified | 72 | 36 | 108 | 
| [gpt-with-vision.md](#item-4d8502) | minor update | GPTとのビジョン機能の向上 | modified | 3 | 3 | 6 | 
| [risks-safety-monitor.md](#item-b2be0b) | minor update | リスクと安全性モニタリングに関する情報の更新 | modified | 3 | 3 | 6 | 
| [use-blocklists.md](#item-e99db7) | minor update | ブロックリストの使用ガイドの情報更新 | modified | 5 | 5 | 10 | 
| [create-new-eval.png](#item-d7bc67) | new feature | 新しい評価作成の画像追加 | added | 0 | 0 | 0 | 
| [eval-generate-1.png](#item-5be1c8) | new feature | 評価生成の画像追加 | added | 0 | 0 | 0 | 
| [eval-generate-2.png](#item-efeac5) | new feature | 評価生成の画像追加 | added | 0 | 0 | 0 | 
| [eval-semantic-similarity-1.png](#item-8729c1) | new feature | 意味的類似性の評価画像追加 | added | 0 | 0 | 0 | 
| [eval-semantic-similarity-2.png](#item-a316c2) | new feature | 意味的類似性評価の画像追加 | added | 0 | 0 | 0 | 
| [eval-semantic-similarity-3.png](#item-0c0125) | new feature | 意味的類似性評価用画像の追加 | added | 0 | 0 | 0 | 
| [eval-submit-job-2.png](#item-d8110c) | new feature | ジョブ提出のための画像追加 | added | 0 | 0 | 0 | 
| [eval-submit-job.png](#item-a9a1f5) | new feature | ジョブ提出手順の画像追加 | added | 0 | 0 | 0 | 
| [eval-testing-criteria-2.png](#item-220e27) | new feature | 評価テスト基準の画像追加 | added | 0 | 0 | 0 | 
| [eval-testing-criteria.png](#item-268f4b) | new feature | 評価テスト基準の画像追加 | added | 0 | 0 | 0 | 
| [upload-data-1.png](#item-cd5af0) | new feature | データアップロードに関する画像追加 | added | 0 | 0 | 0 | 
| [upload-data-2.png](#item-de63da) | new feature | 追加のデータアップロード画像 | added | 0 | 0 | 0 | 


# Modified Contents
## articles/ai-services/openai/concepts/default-safety-policies.md{#item-39b6a0}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デフォルトの安全ポリシーの更新"
}
```

### Explanation
このコードの変更は、`default-safety-policies.md`ファイルの日付情報が更新されたことを示しています。具体的には、`ms.date`の値が「02/20/2025」から「05/31/2025」に変更されました。この更新により、文書の最新の適用日が反映され、コンテンツの正確さと関連性が向上します。変更は、1つの行が追加され、1つの行が削除され、全体で2つの変更が行われています。この修正は、文書の管理者や作成者が最新の情報を提供することを目的としています。

## articles/ai-services/openai/concepts/gpt-4-v-prompt-engineering.md{#item-fd7772}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
 # Image prompt engineering techniques
 
-To unlock the full potential of vision-enabled chat models like GPT-4 Turbo with Vision and GPT-4o, it's essential to tailor the prompts to your specific needs. Here are some guidelines to enhance the accuracy and efficiency of your prompts.
+To unlock the full potential of vision-enabled chat models, it's essential to tailor the prompts to your specific needs. Here are some guidelines to enhance the accuracy and efficiency of your prompts.
 
 ## Fundamentals of writing an image prompt
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-4およびプロンプトエンジニアリングに関する文書の更新"
}
```

### Explanation
このコードの変更は、`gpt-4-v-prompt-engineering.md`ファイルにおける小規模な更新を示しています。更新された内容には、`ms.date`の変更（「02/20/2025」から「05/31/2025」への変更）と、文書中のテキストの改訂が含まれています。具体的には、「視覚に対応したチャットモデルのフルポテンシャルを引き出すためには」という文が削除され、より一般的な表現に置き換えられました。この修正により、文書は最新の情報を提供し、明確さが向上します。また、変更は合計で4つあり、2行の追加と2行の削除が行われています。これにより、プロンプトエンジニアリングの手法に関するガイドラインがより明確になり、正確さと効率性が向上することを目的としています。

## articles/ai-services/openai/concepts/gpt-with-vision.md{#item-991388}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
 # Vision-enabled chat model concepts
 
-Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are GPT-4 Turbo with Vision, GPT-4o, and GPT-4o-mini. This guide provides details on their capabilities and limitations.
+Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. This guide provides details on their capabilities and limitations. To see which models support image input, see the [Models page](./models.md).
 
 To try out vision-enabled chat models, see the [quickstart](/azure/ai-services/openai/gpt-v-quickstart).
 
@@ -21,6 +21,16 @@ To try out vision-enabled chat models, see the [quickstart](/azure/ai-services/o
 The vision-enabled models answer general questions about what's present in the images you upload.
 
 
+## Input limitations
+
+This section describes the limitations of vision-enabled chat models.
+
+### Image support
+
+- **Maximum input image size**: The maximum size for input images is restricted to 20 MB.
+- **Low resolution accuracy**: When images are analyzed using the "low resolution" setting, it allows for faster responses and uses fewer input tokens for certain use cases. However, this could impact the accuracy of object and text recognition within the image.
+- **Image chat restriction**: When you upload images in [Azure AI Foundry portal](https://ai.azure.com/) or the API, there is a limit of 10 images per chat call.
+
 ## Special pricing information
 
 > [!IMPORTANT]
@@ -70,16 +80,6 @@ For a typical use case, take a 3-minute video with a 100-token prompt input. The
 Additionally, there's a one-time indexing cost of $0.15 to generate the Video Retrieval index for this 3-minute video. This index can be reused across any number of Video Retrieval and GPT-4 Turbo with Vision API calls.
 -->
 
-## Input limitations
-
-This section describes the limitations of vision-enabled chat models.
-
-### Image support
-
-- **Maximum input image size**: The maximum size for input images is restricted to 20 MB.
-- **Low resolution accuracy**: When images are analyzed using the "low resolution" setting, it allows for faster responses and uses fewer input tokens for certain use cases. However, this could impact the accuracy of object and text recognition within the image.
-- **Image chat restriction**: When you upload images in [Azure AI Foundry portal](https://ai.azure.com/) or the API, there is a limit of 10 images per chat call.
-
 <!--
 ### Video support
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPTモデルに関する文書の更新"
}
```

### Explanation
このコードの変更は、`gpt-with-vision.md`ファイルにおける内容の改訂を示しています。主な変更点は、文書の日付の更新（「02/20/2025」から「05/31/2025」への変更）と新たなセクションの追加です。具体的には、視覚に対応したチャットモデルに関する情報が詳細化され、モデルが画像入力をサポートしていることを示すリンクが追加されました。また、「入力制限」に関する詳細な説明が新たに追加され、最大入力画像サイズや低解像度時の精度、チャットごとの画像制限についての具体的な情報が提供されています。これにより、ユーザーはこれらのモデルの仕様と制約をよりよく理解できるようになります。一方で、以前の内容は削除され、構成が洗練されていることが特徴です。この変更により、文書はより包括的で、ユーザーにとっての有用性が向上します。

## articles/ai-services/openai/concepts/prompt-transformation.md{#item-21e047}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロンプト変換に関する文書の日付更新"
}
```

### Explanation
このコードの変更は、`prompt-transformation.md`ファイルの日付更新を示しています。具体的には、`ms.date`が「02/20/2025」から「05/31/2025」に変更されました。この更新により、文書の情報が最新であることが反映されています。全体として、変更は非常に小規模であり、主に日付の修正に集中していますが、これにより文書の信頼性が維持され、読者は常に最新の情報にアクセスできるようになります。

## articles/ai-services/openai/dall-e-quickstart.md{#item-fcd528}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.custom: devx-track-python, devx-track-dotnet, devx-track-extended-java, devx-
 ms.topic: quickstart
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 zone_pivot_groups: openai-quickstart-dall-e
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·Eクイックスタートの文書の日付更新"
}
```

### Explanation
このコードの変更は、`dall-e-quickstart.md`ファイルの日付更新を示しています。具体的には、`ms.date`が「02/20/2025」から「05/31/2025」へと変更されました。この小規模な更新は、文書が最新の情報を反映していることを確認するものであり、読者がDALL·Eに関する最新のクイックスタートガイドを参照できるようにするためのものです。全体として、変更は単純ですが、この日付の修正により、文書の信頼性と適時性が高まります。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -9,18 +9,14 @@ ms.custom: devx-track-python, devx-track-js, devx-track-ts
 ms.topic: quickstart
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 zone_pivot_groups: openai-quickstart-gpt-v
 ---
 
 # Quickstart: Use images in your AI chats
 
-Get started using GPT-4 Turbo with images with the Azure OpenAI in Azure AI Foundry Models.
+Get started using images in your chats with Azure OpenAI in Azure AI Foundry Models.
 
-> [!NOTE]
-> **Model choice**
->
-> The latest vision-capable models are `gpt-4o` and `gpt-4o mini`. These models are in public preview. The latest available GA model is `gpt-4` version `turbo-2024-04-09`.
 
 > [!IMPORTANT]
 > Extra usage fees might apply when using chat completion models with vision functionality.
@@ -62,7 +58,7 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI in Azure AI Foun
 
 ::: zone-end
 
-## Next steps
+## Related content
 
 * [Get started with multimodal vision chat apps using Azure OpenAI AI App template](/azure/developer/ai/get-started-app-chat-vision?tabs=github-codespaces)
 * Learn more about these APIs in the [Vision-enabled models how-to guide](./gpt-v-quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-Vクイックスタートガイドの内容と日付更新"
}
```

### Explanation
このコードの変更は、`gpt-v-quickstart.md`ファイルにおける内容の更新と日付の修正を示しています。具体的には、`ms.date`の更新が行われ、日付が「02/20/2025」から「05/31/2025」へと変更されました。また、ガイドのタイトルや内容も一部書き換えられています。

内容の変更点として、ユーザーがGPT-4 Turboを使用する際の説明が具体化され、「images in your chats」という表現が導入され、より正確になっています。さらに、セクションタイトルが「Next steps」から「Related content」に変更され、関連情報へのリンクが強調されています。これにより、読者が参考とすべき関連コンテンツを見つけやすくなっています。

全体として、これらの修正は文書の明確性を向上させ、読者にとっての有用性を高めることを目的としています。

## articles/ai-services/openai/how-to/evaluations.md{#item-dfaa1c}

<details>
<summary>Diff</summary>
````diff
@@ -18,14 +18,39 @@ The evaluation of large language models is a critical step in measuring their pe
 
 Azure OpenAI evaluation enables developers to create evaluation runs to test against expected input/output pairs, assessing the model’s performance across key metrics such as accuracy, reliability, and overall performance.
 
-## Evaluations support
+## Evaluation support
 
 ### Regional availability
 
-- East US2
+- Australia East
+- Brazil South
+- Canada Central
+- Central US
+- East US 2
+- France Central
+- Germany West Central
+- Italy North
+- Japan East
+- Japan West
+- Korea Central
 - North Central US
+- Norway East
+- Poland Central
+- South Africa North
+- Southeast Asia
+- Spain Central
 - Sweden Central
+- Switzerland North
 - Switzerland West
+- UAE North
+- UK South
+- UK West
+- West Europe
+- West US
+- West US 2
+- West US 3
+
+If your preferred region is missing, refer to [Azure OpenAI regions](https://learn.microsoft.com/azure/ai-services/openai/concepts/models?tabs=global-standard%2Cstandard-chat-completions#global-standard-model-availability) and check if it is one of the Azure OpenAI regional availability zones.
 
 ### Supported deployment types
 
@@ -36,6 +61,10 @@ Azure OpenAI evaluation enables developers to create evaluation runs to test aga
 - Global provisioned-managed
 - Data zone provisioned-managed
 
+## Evaluation API (preview)
+
+Evaluation API lets you test model outputs directly through API calls, and programmatically assess model quality and performance. To use Evaluation API, check out the [REST API documentation](https://learn.microsoft.com/azure/ai-services/openai/authoring-reference-preview#evaluation---get-list). 
+
 ## Evaluation pipeline
 
 ### Test data
@@ -90,30 +119,40 @@ Outputs generated during the evaluation will be referenced in subsequent steps u
 
 ### Model deployment
 
-As part of creating evaluations you'll pick which models to use when generating responses (optional) as well as which models to use when grading models with specific testing criteria.  
-
-In Azure OpenAI you'll be assigning specific model deployments to use as part of your evaluations. You can compare multiple model deployments in single evaluation run.
+In Azure OpenAI, you need to create a model deployment to use for your evaluation. You can pick and deploy a single model, or multiple models, depending on your needs. These model deployments will be used when grading your base model or your fine-tuned model with the test criteria of your choice. You can also use the deployed models to auto-generate responses for your provided prompt. 
 
-You can evaluate either base or fine-tuned model deployments. The deployments available in your list depend on those you created within your Azure OpenAI resource. If you can't find the desired deployment, you can create a new one from the Azure OpenAI Evaluation page.
+The deployments available in your list depend on those you created within your Azure OpenAI resource. If you can't find the desired deployment, you can create a new one from the Azure OpenAI Evaluation page.
 
 ### Testing criteria
 
 Testing criteria is used to assess the effectiveness of each output generated by the target model. These tests compare the input data with the output data to ensure consistency. You have the flexibility to configure different criteria to test and measure the quality and relevance of the output at different levels.
 
-:::image type="content" source="../media/how-to/evaluations/testing-criteria.png" alt-text="Screenshot that shows the evaluations testing criteria options." lightbox="../media/how-to/evaluations/testing-criteria.png":::
+:::image type="content" source="../media/how-to/evaluations/eval-testing-criteria.png" alt-text="Screenshot that shows the evaluations testing criteria options." lightbox="../media/how-to/evaluations/eval-testing-criteria.png":::
+
+When you click into each testing criteria, you will see different types of graders as well as preset schemas that you can modify per your own evaluation dataset and criteria. 
+
+:::image type="content" source="../media/how-to/evaluations/eval-testing-criteria-2.png" alt-text="Screenshot that shows the evaluations testing criteria options." lightbox="../media/how-to/evaluations/eval-testing-criteria-2.png":::
 
 ## Getting started
 
 1. Select the **Azure OpenAI Evaluation (PREVIEW)** within [Azure AI Foundry portal](https://ai.azure.com/). To see this view as an option may need to first select an existing Azure OpenAI resource in a supported region.
-2. Select **New evaluation**
+2. Select **+ New evaluation**
 
     :::image type="content" source="../media/how-to/evaluations/new-evaluation.png" alt-text="Screenshot of the Azure OpenAI evaluation UX with new evaluation selected." lightbox="../media/how-to/evaluations/new-evaluation.png":::
 
-3. Enter a name of your evaluation. By default a random name is automatically generated unless you edit and replace it. Select **Upload new dataset**.
+3. Choose how you would like to provide test data for evaluation. You can import stored Chat Completions, create data using provided default templates, or upload your own data. Let's walk through uploading your own data. 
+
+    :::image type="content" source="../media/how-to/evaluations/create-new-eval.png" alt-text="Screenshot of the Azure OpenAI create new evaluation." lightbox="../media/how-to/evaluations/create-new-eval.png":::
 
-    :::image type="content" source="../media/how-to/evaluations/upload.png" alt-text="Screenshot of the Azure OpenAI upload UX." lightbox="../media/how-to/evaluations/upload.png":::
+4. Select your evaluation data which will be in `.jsonl` format. If you already have an existing data, you can select one, or upload a new data.
 
-4. Select your evaluation which will be in `.jsonl` format. If you need a sample test file you can save these 10 lines to a file called `eval-test.jsonl`:
+    :::image type="content" source="../media/how-to/evaluations/upload-data-1.png" alt-text="Screenshot of data upload." lightbox="../media/how-to/evaluations/upload-data-1.png":::
+
+   When you upload new data, you'll see the first three lines of the file as a preview on the right side:
+
+    :::image type="content" source="../media/how-to/evaluations/upload-data-2.png" alt-text="Screenshot of data upload." lightbox="../media/how-to/evaluations/upload-data-2.png":::
+
+   If you need a sample test file, you can use this sample `.jsonl` text. This sample contains sentences of various technical content, and we are going to be assessing semantic similarity across these sentences.
 
     ```jsonl
     {"input": [{"role": "system", "content": "Provide a clear and concise summary of the technical content, highlighting key concepts and their relationships. Focus on the main ideas and practical implications."}, {"role": "user", "content": "Tokenization is a key step in preprocessing for natural language processing, involving the division of text into smaller components called tokens. These can be words, subwords, or characters, depending on the method chosen. Word tokenization divides text at word boundaries, while subword techniques like Byte Pair Encoding (BPE) or WordPiece can manage unknown words by breaking them into subunits. Character tokenization splits text into individual characters, useful for multiple languages and misspellings. The tokenization method chosen greatly affects model performance and its capacity to handle various languages and vocabularies."}], "output": "Tokenization divides text into smaller units (tokens) for NLP applications, using word, subword (e.g., BPE), or character methods. Each has unique benefits, impacting model performance and language processing capabilities."}      
@@ -127,48 +166,45 @@ Testing criteria is used to assess the effectiveness of each output generated by
     {"input": [{"role": "system", "content": "Generate a clear and focused summary that captures the essential technical details while maintaining their relationships and significance."}, {"role": "user", "content": "Transfer learning is a machine learning method where a model developed for one task is reused as the starting point for a model on a second task. This approach is powerful in deep learning, where pre-trained models on large datasets (like ImageNet for computer vision or BERT for NLP) are fine-tuned on specific downstream tasks. Transfer learning reduces the need for large amounts of task-specific training data and computational resources, as the model has already learned useful features from the source domain. Common strategies include feature extraction (freezing pre-trained layers) and fine-tuning (updating all or some pre-trained weights)."}], "output": "Transfer learning reuses models trained on one task for different tasks, particularly effective in deep learning. It leverages pre-trained models through feature extraction or fine-tuning, reducing data and computational needs for new tasks."}      
     {"input": [{"role": "system", "content": "Provide a precise and informative summary that distills the key technical concepts while maintaining their relationships and practical importance."}, {"role": "user", "content": "Ensemble methods combine multiple machine learning models to create a more robust and accurate predictor. Common techniques include bagging (training models on random data subsets), boosting (sequentially training models to correct earlier errors), and stacking (using a meta-model to combine base model predictions). Random Forests, a popular bagging method, create multiple decision trees using random feature subsets. Gradient Boosting builds trees sequentially, with each tree correcting the errors of previous ones. These methods often outperform single models by reducing overfitting and variance while capturing different data aspects."}], "output": "Ensemble methods enhance prediction accuracy by combining multiple models through techniques like bagging, boosting, and stacking. Popular implementations include Random Forests (using multiple trees with random features) and Gradient Boosting (sequential error correction), offering better performance than single models."}
     ```
+    
+5. If you would like to create new responses using inputs from your test data, you can select 'Generate new responses'. This will inject the input fields from our evaluation file into individual prompts for a model of your choice to generate output.
 
-    You'll see the first three lines of the file as a preview:
-
-    :::image type="content" source="../media/how-to/evaluations/preview.png" alt-text="Screenshot that shows a preview of an uploaded evaluation file." lightbox="../media/how-to/evaluations/preview.png":::
-
-5. Under **Responses** select the **Create** button. Select `{{item.input}}` from the **Create with a template** dropdown. This will inject the input fields from our evaluation file into individual prompts for a new model run that we want to able to compare against our evaluation dataset. The model will take that input and generate its own unique outputs which in this case will be stored in a variable called `{{sample.output_text}}`. We'll then use that sample output text later as part of our testing criteria. Alternatively you could provide your own custom system message and individual message examples manually.
-
-6. Select which model you want to generate responses based on your evaluation. If you don't have a model you can create one. For the purpose of this example we're using a standard deployment of `gpt-4o-mini`.
+:::image type="content" source="../media/how-to/evaluations/eval-generate-1.png" alt-text="Screenshot of the UX for generating model responses." lightbox="../media/how-to/evaluations/eval-generate-1.png":::
+   
+You will select the model of your choice. If you do not have a model, you can create a new model deployment. The selected model will take the input data and generate its own unique outputs, which in this case will be stored in a variable called `{{sample.output_text}}`. We'll then use that output later as part of our testing criteria. Alternatively, you could provide your own custom system message and individual message examples manually.
 
-    :::image type="content" source="../media/how-to/evaluations/item-input.png" alt-text="Screenshot of the UX for generating model responses with a model selected." lightbox="../media/how-to/evaluations/item-input.png":::
+:::image type="content" source="../media/how-to/evaluations/eval-generate-2.png" alt-text="Screenshot of the UX for generating model responses." lightbox="../media/how-to/evaluations/eval-generate-2.png":::
 
-    The settings/sprocket symbol controls the basic parameters that are passed to the model. Only the following parameters are supported at this time:
+6. For creating a test criteria, select **Add**. For the example file we provided, we are going to be assessing semantic similarity. Select **Model Scorer**, which contains test criteria presets for Semantic Similarity.
 
-- **Temperature**
-- **Maximum length**
-- **Top P**
+    :::image type="content" source="../media/how-to/evaluations/eval-semantic-similarity-1.png" alt-text="Screenshot of the semantic similarity UX config." lightbox="../media/how-to/evaluations/eval-semantic-similarity-1.png":::
 
- Maximum length is currently capped at 2048 regardless of what model you select.
+   Select **Semantic Similarity** at the top. Scroll to the bottom, and in `User` section, specify `{{item.output}}` as `Ground truth`, and specify `{{sample.output_text}}` as `Output`. This will take the original reference output from your evaluation `.jsonl` file (the sample file provided) and compare it against the output that is generated by the model you chose in the previous step.
 
-7. Select **Add testing criteria** select **Add**.
+    :::image type="content" source="../media/how-to/evaluations/eval-semantic-similarity-2.png" alt-text="Screenshot of the semantic similarity UX config." lightbox="../media/how-to/evaluations/eval-semantic-similarity-2.png":::
 
-8. Select **Semantic Similarity** >  Under **Compare** add `{{item.output}}` under **With** add ``{{sample.output_text}}``. This will take the original reference output from your evaluation `.jsonl` file and compare it against the output that will be generated by giving the model prompts based on your ``{{item.input}}``.
+:::image type="content" source="../media/how-to/evaluations/eval-semantic-similarity-3.png" alt-text="Screenshot of the semantic similarity UX config." lightbox="../media/how-to/evaluations/eval-semantic-similarity-3.png":::
 
-    :::image type="content" source="../media/how-to/evaluations/semantic-similarity-config.png" alt-text="Screenshot of the semantic similarity UX config." lightbox="../media/how-to/evaluations/semantic-similarity-config.png":::
+7. Select **Add** to add this testing criteria. If you would like to add additional testing criteria, you can add them at this step.
 
-9. Select **Add** > at this point you can either add additional testing criteria or you select Create to initiate the evaluation job run.
+8. You are ready to create your Evaluation. Provide your Evaluation name, review everything looks correct, and **Submit** to create the Evaluation job. You'll be taken to a status page for your evaluation job, which will show the status as "Waiting".
 
-10. Once you select **Create** you'll be taken to a status page for your evaluation job.
+:::image type="content" source="../media/how-to/evaluations/eval-submit-job.png" alt-text="Screenshot of the evaluation job submit UX." lightbox="../media/how-to/evaluations/eval-submit-job.png":::
+:::image type="content" source="../media/how-to/evaluations/eval-submit-job-2.png" alt-text="Screenshot of the evaluation job submit UX." lightbox="../media/how-to/evaluations/eval-submit-job-2.png":::
 
-    :::image type="content" source="../media/how-to/evaluations/status.png" alt-text="Screenshot of the evaluation status UX." lightbox="../media/how-to/evaluations/status.png":::
+9. Once your evaluation job has created, you can select the job to view the full details of the job:
 
-11. Once your evaluation job has created you can select the job to view the full details of the job:
+:::image type="content" source="../media/how-to/evaluations/test-complete.png" alt-text="Screenshot of a completed semantic similarity test with mix of pass and failures." lightbox="../media/how-to/evaluations/test-complete.png":::
 
-    :::image type="content" source="../media/how-to/evaluations/test-complete.png" alt-text="Screenshot of a completed semantic similarity test with mix of pass and failures." lightbox="../media/how-to/evaluations/test-complete.png":::
+10. For semantic similarity **View output details** contains a JSON representation that you can copy/paste of your passing tests.
 
-12. For semantic similarity **View output details** contains a JSON representation that you can copy/paste of your passing tests.
+:::image type="content" source="../media/how-to/evaluations/output-details.png" alt-text="Screenshot of the evaluation status UX with output details." lightbox="../media/how-to/evaluations/output-details.png":::
 
-    :::image type="content" source="../media/how-to/evaluations/output-details.png" alt-text="Screenshot of the evaluation status UX with output details." lightbox="../media/how-to/evaluations/output-details.png":::
+11. You can also add more Eval runs by selecting **+ Add Run** button at the top left corner of your evaluation job page.
 
-## Testing criteria details
+## Types of Testing Criteria
 
-Azure OpenAI Evaluation offers multiple testing criteria options. The section below provides additional details on each option.
+Azure OpenAI Evaluation offers various evaluation testing criteria on top of Semantic Similarity we saw in the provided example. This section provides information about each testing criteria at much more detail.
 
 ### Factuality
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価ガイドの内容拡充と新機能の追加"
}
```

### Explanation
このコードの変更は、`evaluations.md`ファイルにおける内容の大幅な改訂を示しています。この更新では、評価のサポート情報やAPI機能、モデルデプロイメントの詳細が追加され、文書全体が充実しています。

具体的には、「Evaluation support」というタイトルの下に地域の可用性リストが追加され、新たに「評価API（プレビュー）」というセクションも設けられています。この評価APIは、API呼び出しを通じてモデルの出力をテストし、品質や性能をプログラム的に評価する機能を提供します。

また、モデルデプロイメントに関する説明が広がり、評価の際に使用するモデルの選択やデプロイメントの作成についての指示が明確に記述されています。テスト基準の設定にも新しい説明が加わり、文書がより実用的で具体的な手順を提供しています。

さらに、画像のリンクや具体的な使用例が新たに挿入されており、読者が視覚的に情報を把握しやすくなっています。全体として、この変更はドキュメントの明確性と実用性を高めるために行われたもので、開発者がAzure OpenAIを利用して評価を行う際の理解を深めることに寄与しています。

## articles/ai-services/openai/how-to/gpt-with-vision.md{#item-4d8502}

<details>
<summary>Diff</summary>
````diff
@@ -7,14 +7,14 @@ ms.author: pafarley #delegenz
 #customer intent: As a developer, I want to learn how to use vision-enabled chat models so that I can integrate image processing capabilities into my applications.
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
 # Use vision-enabled chat models
 
 
-Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are [o1](./reasoning.md), GPT-4o, GPT-4o-mini, and GPT-4 Turbo with Vision.
+Vision-enabled chat models are large multimodal models (LMM) developed by OpenAI that can analyze images and provide textual responses to questions about them. They incorporate both natural language processing and visual understanding. The current vision-enabled models are the [o-series reasoning models](./reasoning.md), GPT-4.1 series models, GPT-4.5, GPT-4o series, and GPT-4 Turbo with Vision.
 
 The vision-enabled models can answer general questions about what's present in the images you upload.
 
@@ -383,7 +383,7 @@ Every response includes a `"finish_reason"` field. It has the following possible
 [!INCLUDE [GPT-4 Turbo](../includes/gpt-4-turbo.md)]
 
 
-## Next steps
+## Related content
 
 * [Learn more about Azure OpenAI](../overview.md).
 * [Vision-enabled chats quickstart](../gpt-v-quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPTとのビジョン機能の向上"
}
```

### Explanation
このコードの変更は、`gpt-with-vision.md`ファイルにおけるいくつかの内容の修正を示しています。主な変更点は、日付の更新、モデルのリストの変更、そしてセクションタイトルの修正です。

具体的には、`ms.date`のフィールドが「02/20/2025」から「05/31/2025」に更新されました。また、ビジョン対応チャットモデルの説明で、モデルの名称が詳細化され、「o1」モデルが「o-series reasoning models」と名付け直され、さらに新しいモデルシリーズとして「GPT-4.1」や「GPT-4.5」が追加されました。これによって、読者は最新のモデル情報をより正確に理解できるようになります。

加えて、セクションタイトルが「Next steps」から「Related content」に変更され、関連コンテンツへのリンクが提供されています。この変更は、ユーザーが次にどの情報を参照すべきか、より明確に示すことを目的としています。

これらの修正により、文書の内容が最新の情報を反映し、ユーザーにとっての利便性が向上しています。

## articles/ai-services/openai/how-to/risks-safety-monitor.md{#item-b2be0b}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: PatrickFarley
 ms.author: pafarley 
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 manager: nitinme
 ---
 
@@ -43,14 +43,14 @@ Adjust your content filter configuration to further align with business needs an
 
 ## Potentially abusive user detection   
 
-The **Potentially abusive user detection** pane leverages user-level abuse reporting to show information about users whose behavior has resulted in blocked content. The goal is to help you get a view of the sources of harmful content so you can take responsive actions to ensure the model is being used in a responsible way. 
+The **Potentially abusive user detection** pane shows information about users whose behavior has resulted in blocked content. The goal is to help you get a view of the sources of harmful content so you can take responsive actions to ensure the model is being used in a responsible way. 
 
 
 To use Potentially abusive user detection, you need:
 - A content filter configuration applied to your deployment.
 - You must be sending user ID information in your Chat Completion requests (see the _user_ parameter of the [Completions API](/azure/ai-services/openai/reference#completions), for example).
     > [!CAUTION]
-    > Use GUID strings to identify individual users. Do not include sensitive personal information in the _user_ field.
+    > Use GUID strings to identify individual users. Don't include sensitive personal information in the _user_ field.
 - An Azure Data Explorer database set up to store the user analysis results (instructions below).
 
 ### Set up your Azure Data Explorer database
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リスクと安全性モニタリングに関する情報の更新"
}
```

### Explanation
このコードの変更は、`risks-safety-monitor.md`ファイルに対するいくつかの修正を含んでいます。主な更新内容は、日付の変更、文の簡略化、および注意書きの表現の修正です。

具体的には、`ms.date`のフィールドが「02/20/2025」から「05/31/2025」に変更され、文書の最新性が反映されています。また、「Potentially abusive user detection」セクションにて、ユーザーの行動に基づく報告内容が簡素化されており、冗長な表現が削除されています。これにより、情報がより明確で分かりやすくなっています。

その他の変更点として、注意書きの部分で「Do not include sensitive personal information in the _user_ field」という表現が「Don't include sensitive personal information in the _user_ field」に修正されており、これにより表現がよりカジュアルで読みやすくなっています。

これらの修正により、文書の可読性が向上し、内容が最新の情報を反映する形となっており、ユーザーがリスクと安全性の監視に関する機能をより効果的に理解し利用できるようになっています。

## articles/ai-services/openai/how-to/use-blocklists.md{#item-e99db7}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use blocklists with Azure OpenAI
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 02/20/2025
+ms.date: 05/31/2025
 author: PatrickFarley
 ms.author: pafarley
 ---
@@ -17,7 +17,7 @@ The [configurable content filters](/azure/ai-services/openai/how-to/content-filt
 ## Prerequisites
 
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
-- Once you have your Azure subscription, create an Azure OpenAI resource in the Azure portal to get your token, key and endpoint. Enter a unique name for your resource, select the subscription you entered on the application form, select a resource group, supported region, and supported pricing tier. Then select **Create**.
+- Once you have your Azure subscription, create an Azure OpenAI resource in the Azure portal to get your token, key, and endpoint. Enter a unique name for your resource, select the subscription you entered on the application form, select a resource group, supported region, and supported pricing tier. Then select **Create**.
     - The resource takes a few minutes to deploy. After it finishes, select **go to resource**. In the left pane, under **Resource Management**, select **Subscription Key and Endpoint**. The endpoint and either of the keys are used to call APIs.
 - [Azure CLI](/cli/azure/install-azure-cli) installed
 - [cURL](https://curl.haxx.se/) installed
@@ -30,7 +30,7 @@ You can create blocklists with the Azure OpenAI API. The following steps help yo
 
 ### Get your token
 
-First, you need to get a token for accessing the APIs for creating, editing and deleting blocklists. You can get this token using the following Azure CLI command: 
+First, you need to get a token for accessing the APIs for creating, editing, and deleting blocklists. You can get this token using the following Azure CLI command: 
 
 ```bash
 az account get-access-token 
@@ -102,7 +102,7 @@ Copy the cURL command below to a text editor and make the following changes:
 1. Replace {raiBlocklistName} (in the URL) with a custom name for your list. Allowed characters: `0-9, A-Z, a-z, - . _ ~`. 
 1. Replace {raiBlocklistItemName} with a custom name for your list item. 
 1. Replace {token} with the token you got from the "Get your token" step above. 
-1. Replace the value of the `"blocking pattern"` field with the item you'd like to add to your blocklist. The maximum length of a blockItem is 1000 characters. Also specify whether the pattern is regex or exact match. 
+1. Replace the value of the `"blocking pattern"` field with the item you'd like to add to your blocklist. The maximum length of a blockItem is 1,000 characters. Also specify whether the pattern is regex or exact match. 
 
 ```bash
 curl --location --request PUT 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CognitiveServices/accounts/{accountName}/raiBlocklists/{raiBlocklistName}/raiBlocklistItems/{raiBlocklistItemName}?api-version=2024-04-01-preview' \ 
@@ -117,7 +117,7 @@ curl --location --request PUT 'https://management.azure.com/subscriptions/{subsc
 ```
 
 > [!NOTE]
-> It can take around 5 minutes for a new term to be added to the blocklist. Please test after 5 minutes. 
+> It can take around 5 minutes for a new term to be added to the blocklist. Test the blocklist after 5 minutes. 
 
 The response code should be `200`. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ブロックリストの使用ガイドの情報更新"
}
```

### Explanation
このコードの変更は、`use-blocklists.md`ファイルにおけるいくつかの修正を示しています。主な変更点には、日付の更新、文の構成の改善、そして数箇所の細かな表現の修正が含まれています。

具体的に、`ms.date`フィールドが「02/20/2025」から「05/31/2025」に変更され、文書が最新の情報を反映するようになっています。また、いくつかの文において、コンマや表現の統一が行われており、文の流れがスムーズになるように改善されています。例えば、"key and endpoint" が "key, and endpoint" という具合に修正され、リスト要素が明確になります。

文中の注意書きもアクティブな表現に変更されており、「Please test after 5 minutes」という部分が「Test the blocklist after 5 minutes」となっています。これにより、ユーザーへの指示がより明確で実行しやすくなります。

これらの変更は、文書がより読みやすく、正確に利用者に情報を伝えることを目的としており、ブロックリストの使用方法に関する理解を深める手助けになります。

## articles/ai-services/openai/media/how-to/evaluations/create-new-eval.png{#item-d7bc67}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "新しい評価作成の画像追加"
}
```

### Explanation
このコードの変更には、`create-new-eval.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、新しい評価の作成に関するビジュアルガイドとして使用されることを意図しています。

新しい画像の追加は、文書の説明を強化し、ユーザーが評価を作成するプロセスを視覚的に理解しやすくするためのものであり、特に手順が複雑な場合に役立ちます。このようなビジュアルコンテンツの追加は、読者にとっての使い勝手を向上させ、情報の吸収を助ける重要な要素となります。 

画像はGitHubのリポジトリ内で確認することができ、必要に応じてダウンロードや表示が可能です。この新しいビジュアルリソースは、評価作成の具体的な手順や要素を示すことで、文書全体の価値を高めることに寄与しています。

## articles/ai-services/openai/media/how-to/evaluations/eval-generate-1.png{#item-5be1c8}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価生成の画像追加"
}
```

### Explanation
このコードの変更では、`eval-generate-1.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、評価生成に関する手順を視覚的に示すことを目的としています。

新しいビジュアルコンテンツの追加により、ユーザーが評価を生成するプロセスをより理解しやすくなります。特に、手順やコンセプトが視覚的に示されることで、ユーザーは情報をより効果的に吸収できるようになります。

この画像はGitHubのリポジトリ内でアクセス可能で、読者が必要に応じて表示・ダウンロードすることができます。評価生成における重要なステップや要素を強調することによって、関連するドキュメント全体の価値を向上させることが期待されます。

## articles/ai-services/openai/media/how-to/evaluations/eval-generate-2.png{#item-efeac5}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価生成の画像追加"
}
```

### Explanation
このコードの変更では、`eval-generate-2.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、評価生成の過程を視覚的に支援することを目的としています。

画像の追加により、ユーザーは評価を生成する際の具体的な手順やポイントをより理解しやすくなります。特に手順が複雑である場合、ビジュアルの存在は操作を明確にする助けとなります。

この画像はGitHubのリポジトリにてアクセスでき、ユーザーが必要に応じて表示やダウンロードを行うことができます。評価生成の手順をより効果的に伝えるために、このような視覚的な資料の追加は文書全体の理解を深めるために非常に重要です。

## articles/ai-services/openai/media/how-to/evaluations/eval-semantic-similarity-1.png{#item-8729c1}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "意味的類似性の評価画像追加"
}
```

### Explanation
このコードの変更では、`eval-semantic-similarity-1.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、意味的類似性に関する評価のプロセスを視覚的に示すことを目的としています。

新たに追加された画像は、ユーザーが意味的類似性を評価する際の手順や考慮すべき要点を理解するのに役立つでしょう。視覚的な資料は、コンセプトや方法論をより明確に伝えるのに非常に効果的です。

この画像はGitHubのリポジトリにてアクセス可能であり、ユーザーは必要に応じて表示またはダウンロードすることができます。このように、内容に関連するビジュアルを追加することで、関連するドキュメントの効果を高め、より良い学習体験を提供することが期待されます。

## articles/ai-services/openai/media/how-to/evaluations/eval-semantic-similarity-2.png{#item-a316c2}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "意味的類似性評価の画像追加"
}
```

### Explanation
このコードの変更では、`eval-semantic-similarity-2.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、意味的類似性の評価を補助するための視覚資料としての役割を果たします。

新たに追加されたこの画像は、評価過程の具体的な例示を提供し、ユーザーが意味的類似性を効果的に理解するための手助けをします。視覚情報は、特に複雑なプロセスを理解する上で重要な役割を果たすため、ユーザーの学習体験を向上させることが期待されます。

画像はGitHubのリポジトリからアクセス可能で、ユーザーは必要に応じてその内容を確認したりダウンロードしたりすることができます。このようなビジュアルコンテンツの追加により、関連するトピックの理解が一層深まります。

## articles/ai-services/openai/media/how-to/evaluations/eval-semantic-similarity-3.png{#item-0c0125}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "意味的類似性評価用画像の追加"
}
```

### Explanation
このコードの変更では、`eval-semantic-similarity-3.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、意味的類似性を評価する際の追加のビジュアルリソースとして機能します。

この新たに追加された画像は、評価手法や結果の解釈をより分かりやすく視覚化することを目的としており、ユーザーが情報を容易に理解できるようにサポートします。複雑な概念を視覚的に表現することによって、学習を補助し、関連するプロセスを明確にする役割を果たします。

また、GitHubのリポジトリにてこの画像はアクセス可能であり、利用者は直接リンクを用いて画像を表示したりダウンロードしたりすることができるため、学習の資源として活用できます。このように、追加のビジュアルコンテンツを提供することで、学習体験がさらに充実することが期待されます。

## articles/ai-services/openai/media/how-to/evaluations/eval-submit-job-2.png{#item-d8110c}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ジョブ提出のための画像追加"
}
```

### Explanation
このコードの変更では、`eval-submit-job-2.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、ジョブ提出のプロセスを視覚的に示すためのもので、ユーザーが手順を理解しやすくすることを目的としています。

新たに追加されたこの画像は、特に評価のためのジョブを提出する際の操作方法や流れを明確に示す情報を提供します。視覚的なコンテンツは、テキストだけでは伝わりにくい手順の理解を助けるため、ユーザーがより効果的にプロセスを実行できるように設計されています。

また、この画像はGitHubのリポジトリでアクセス可能であり、ユーザーは直接リンクを使用してその内容を確認したり、必要に応じてダウンロードしたりすることができます。このように、ビジュアルリソースを追加することで、ユーザーの理解を深め、学習体験を向上させることが期待されています。

## articles/ai-services/openai/media/how-to/evaluations/eval-submit-job.png{#item-a9a1f5}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ジョブ提出手順の画像追加"
}
```

### Explanation
このコードの変更では、`eval-submit-job.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、評価のためにジョブを提出する際の手順を視覚的に説明する貴重なリソースとなります。

新たに追加された画像は、ユーザーがジョブ提出のプロセスをスムーズに理解し、実行できるようにすることを目的として設計されています。具体的には、関連するステップや重要なポイントを視覚化することで、テキスト情報だけでは伝わりにくい手続きの内容を補完します。

ユーザーはGitHubのリポジトリにある直接リンクを利用して、この画像を確認したり、ダウンロードしたりすることができ、必要に応じて手元で比較や参照を行うことができます。このように、ビジュアル教材を提供することで、学習の効率が向上し、ユーザーの体験が豊かになることが期待されています。

## articles/ai-services/openai/media/how-to/evaluations/eval-testing-criteria-2.png{#item-220e27}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価テスト基準の画像追加"
}
```

### Explanation
このコードの変更では、`eval-testing-criteria-2.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、評価のためのテスト基準を視覚的に示すもので、ユーザーが評価プロセスをより良く理解できるようにすることを目的としています。

追加された画像は、評価テストの基準やその重要性を整理して視覚化する役割を果たします。これにより、ユーザーは複雑な情報を一目で把握しやすくなり、実際のテストにおける判断がスムーズに行えるようになります。

ユーザーは、この画像をGitHubのリポジトリから直接アクセスして確認することができ、必要に応じてダウンロードできる環境が整っています。このビジュアルコンテンツは、ユーザーの学習体験を向上させ、テスト基準の理解を深めるための重要な資源として機能します。

## articles/ai-services/openai/media/how-to/evaluations/eval-testing-criteria.png{#item-268f4b}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "評価テスト基準の画像追加"
}
```

### Explanation
このコードの変更では、`eval-testing-criteria.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、評価に関連するテスト基準を視覚的に解説するために設計されており、ユーザーが評価プロセスを理解する手助けをします。

この新しい画像により、ユーザーは評価テストの基準やそれに関連する重要な要素を直感的に把握することが可能になります。視覚的な情報提供は、特に複雑な概念や手続きを理解する際に有効であり、従来のテキストのみの説明に比べて学習効果を高めることが期待されます。

ユーザーは、この画像をGitHubリポジトリのリンクから直接確認したり、ダウンロードしたりすることができるため、より効果的に評価の準備を進めることができます。全体として、この追加はユーザーの学習体験を豊かにし、評価基準の理解を深めるための重要なステップです。

## articles/ai-services/openai/media/how-to/evaluations/upload-data-1.png{#item-cd5af0}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "データアップロードに関する画像追加"
}
```

### Explanation
今回の変更では、`upload-data-1.png`という新しい画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、データのアップロード手順を視覚的にガイドする目的で作成されており、ユーザーが正確にデータをアップロードする方法を理解するのに役立ちます。

この新しいビジュアルコンテンツは、ユーザーがデータを正しくアップロードする際の具体的なステップを示すことで、プロセスの理解を促進します。視覚的な指示は、特に手順が複雑な場合において、テキストのみの説明よりも効果的であり、ユーザーの混乱を軽減します。

ユーザーは、GitHubリポジトリのリンクを通じてこの画像にアクセスすることができ、必要に応じてダウンロードすることも可能です。この追加によって、データアップロードに関するユーザーの利便性が向上し、作業の迅速化が期待されます。全体として、この変更は、使いやすさと学習効果を高めるための重要な貢献といえます。

## articles/ai-services/openai/media/how-to/evaluations/upload-data-2.png{#item-de63da}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "追加のデータアップロード画像"
}
```

### Explanation
このコードの変更では、`upload-data-2.png`という新たな画像ファイルが`how-to/evaluations`ディレクトリに追加されました。この画像は、データアップロードの手順をより詳しく説明するために作成されており、ユーザーがプロセスを視覚的に把握できるようにサポートします。

この新しい画像は、特に複雑なデータアップロード操作を行う際に、ユーザーが具体的な手順を確認する助けとなります。追加されたビジュアル情報は、データアップロードの過程で生じる可能性のある疑問を解消し、スムーズな作業を促進します。 

ユーザーは、GitHubリポジトリのリンクから直接この画像にアクセスしたり、必要に応じてダウンロードしたりすることができます。この変更により、データアップロードに関する指示が一層明確になり、ユーザーの効率的な作業を支援することが期待されます。全体として、この画像の追加は、プロセスの可視化を通じて学習体験を向上させるための重要な改善です。


