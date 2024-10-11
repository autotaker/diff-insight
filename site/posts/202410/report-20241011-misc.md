---
date: '2024-10-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f
summary: このドキュメントの変更では、Azure AIのコンテンツフィルタリング機能がプレビュー段階にあることを明示的に記載し、関連するモデルデプロイメントガイドやAPIドキュメントが更新されました。また、AIスタジオの目次整理とチャットウェブアプリチュートリアルのリンク更新も行われています。新機能の追加はありませんが、フィルタリングシステムのプレビュー状態を強調することで、ユーザーはその利用方法やリスクをより適切に評価できるようになります。全体的にこれらの変更は、ドキュメントの品質向上とユーザーエクスペリエンスを向上させるためのものです。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:7341d04...MicrosoftDocs:576156f){target="_blank"}

# ハイライト
このドキュメントの変更では、複数のモデルデプロイメントガイドや関連APIドキュメントにおいて、「コンテンツフィルタリング（プレビュー）システム」との記述が更新され、Azure AIのコンテンツフィルタリング機能がプレビュー段階にあることを明示しています。また、AIスタジオに関する目次の整理とチャットウェブアプリチュートリアルのリンク更新が行われています。

## 新機能
特に新しい機能の追加はありませんが、フィルタリングシステムがプレビューであることが強調されています。

## 破壊的変更
破壊的変更はありません。

## その他の更新
- コンテンツフィルタリングを「プレビュー」として明示。
- ドキュメントの目次整理と製品データリンクの更新。

# インサイト
この更新は、Azure AIのさまざまなモデル推論APIやデプロイガイドにおけるコンテンツフィルタリングの機能を、より一貫性のある形でユーザーに伝えることを目的としています。これにより、ユーザーはフィルタリング機能が現在プレビュー段階にあり、まだ完全な状態ではないことを意識しつつ、これを利用したコンテンツセーフティの実装方法を学ぶことができます。

コンテンツフィルタリングが「プレビュー」状態であることを明確にすることにより、ユーザーは今後の開発や更新に対して正確な期待を持つことができます。また、ユーザーはこの情報を元に、フィルタリング機能を実際のアプリケーションで使用する際のリスクとメリットをより適切に評価することが可能です。

AIスタジオの目次の整理や、チュートリアル内のリンク更新といった他の変更も、ユーザーエクスペリエンスを向上させ、必要な情報にアクセスする時間を短縮するための取り組みとして効果的です。全体として、これらの修正はドキュメントの品質向上に寄与し、Azure AIの利用を促進するための土台を提供するものとなっています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [deploy-models-cohere-command.md](#item-3e97f4) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-jais.md](#item-0bd11f) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-jamba.md](#item-eeefca) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 2 | 2 | 4 | 
| [deploy-models-llama.md](#item-6274a7) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-phi-3-5-vision.md](#item-8d6d7d) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-phi-3.md](#item-47e305) | minor update | コンテンツフィルタリングシステムのプレビュー通知の追加 | modified | 4 | 4 | 8 | 
| [deploy-models-serverless.md](#item-f8177f) | minor update | コンテンツフィルタリングのプレビュー通知の更新 | modified | 1 | 1 | 2 | 
| [fine-tune-model-llama.md](#item-2a42d8) | minor update | コンテンツフィルタリングのプレビュー通知の追加 | modified | 1 | 1 | 2 | 
| [fine-tune-phi-3.md](#item-5b722a) | minor update | コンテンツフィルタリングのプレビュー通知の追加と注意点の明確化 | modified | 5 | 5 | 10 | 
| [reference-model-inference-api.md](#item-9fe240) | minor update | コンテンツフィルタリングのプレビュー通知の追加 | modified | 1 | 1 | 2 | 
| [toc.yml](#item-2745cd) | minor update | カスタムDNSの表示名の追加と不要な項目の削除 | modified | 1 | 2 | 3 | 
| [deploy-chat-web-app.md](#item-987845) | minor update | 製品データのダウンロードリンクの更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/how-to/deploy-models-cohere-command.md{#item-3e97f4}

<details>
<summary>Diff</summary>
````diff
@@ -462,7 +462,7 @@ response = client.complete(
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -943,7 +943,7 @@ var result = await client.path("/chat/completions").post({
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1455,7 +1455,7 @@ response = client.Complete(requestOptions);
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -2084,7 +2084,7 @@ View the response from the model:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「コンテンツの安全性を適用」セクションの説明において、Azure AIモデル推論APIのコンテンツフィルタリングシステムに関する重要な用語を更新しています。具体的には、既存の「コンテンツフィルタリングシステム」という表現が「コンテンツフィルタリング（プレビュー）システム」と修正されました。これにより、システムが現在プレビュー段階であることが明確に示され、ユーザーはその整備の状況をより理解しやすくなります。

変更された箇所は複数あり、内容は全体の文脈と一致しています。これにより、デプロイメントにおけるコンテンツ安全性の重要性が強調され、モデルによる有害なコンテンツの検出とその対策の方法を示すための具体的な例も依然として提供されています。

## articles/ai-studio/how-to/deploy-models-jais.md{#item-0bd11f}

<details>
<summary>Diff</summary>
````diff
@@ -244,7 +244,7 @@ response = client.complete(
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -512,7 +512,7 @@ var response = await client.path("/chat/completions").post({
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -802,7 +802,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1125,7 +1125,7 @@ extra-parameters: pass-through
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更では、「コンテンツの安全性を適用」というセクションにおいて、Azure AIモデル推論APIに関連する文言が更新されました。具体的には、元々の「コンテンツフィルタリングシステム」という表現が「コンテンツフィルタリング（プレビュー）システム」と修正されています。この更新により、コンテンツフィルタリング機能が現在プレビュー段階にあることが明確となり、利用者に対してその状況を明示的に示すことができます。

修正は複数の箇所にわたり、情報の一貫性を保ちながら重要なコンテキストを継続的に伝えています。この更新により、ユーザーはモデルが有害なコンテンツを検出した場合の処理方法についての具体的な例を引き続き参照することができ、コンテンツ安全性の適用に関する理解が深まるでしょう。

## articles/ai-studio/how-to/deploy-models-jamba.md{#item-eeefca}

<details>
<summary>Diff</summary>
````diff
@@ -217,7 +217,7 @@ The `document` object has the following fields:
 - `id` (optional; str) - unique identifier. will be linked to in citations. up to 128 characters.
 - `content` (required; str) - the content of the document
 - `metadata` (optional; array of **Metadata)**
-  - `key` (required; str) - type of metadata, like ‘author’, ‘date’, ‘url’, etc. Should be things the model understands.
+  - `key` (required; str) - type of metadata, like 'author', 'date', 'url', etc. Should be things the model understands.
   - `value` (required; str) - value of the metadata
 
 #### Request example
@@ -410,7 +410,7 @@ Quota is managed per deployment. Each deployment has a rate limit of 200,000 tok
 
 ## Content filtering
 
-Models deployed as a serverless API are protected by Azure AI content safety. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](/azure/ai-services/content-safety/overview).
+Models deployed as a serverless API are protected by Azure AI content safety. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](/azure/ai-services/content-safety/overview).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「Jamba」モデルのデプロイ方法に関するドキュメントのいくつかの箇所において、コンテンツフィルタリングシステムについての説明文が修正されています。具体的には、コンテンツフィルタリングシステムに関する言及が以前の「コンテンツフィルタリングシステム」から「コンテンツフィルタリング（プレビュー）システム」に変更され、プレビュー段階であることが明示化されました。

この更新により、ユーザーはAzure AIコンテンツ安全性機能についてのより明確な情報を得ることができ、モデルが有害なコンテンツを検出し防ぐためのプロセスについて理解を深めることができます。また、「document」オブジェクトのメタデータにも細かい修正が加えられ、内容が一貫性を持って更新されています。これにより、開発者が実装を行う際の読みやすさと理解が向上します。

## articles/ai-studio/how-to/deploy-models-llama.md{#item-6274a7}

<details>
<summary>Diff</summary>
````diff
@@ -323,7 +323,7 @@ The following extra parameters can be passed to Meta Llama models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -665,7 +665,7 @@ The following extra parameters can be passed to Meta Llama models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1025,7 +1025,7 @@ The following extra parameters can be passed to Meta Llama models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1410,7 +1410,7 @@ The following extra parameters can be passed to Meta Llama chat models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更では、「Llama」モデルのデプロイ方法に関するドキュメントの「コンテンツ安全性を適用」セクションにおいて、いくつかの表現が更新されました。具体的には、以前の「コンテンツフィルタリングシステム」という語句が「コンテンツフィルタリング（プレビュー）システム」に修正され、これはこの機能が現在プレビュー段階であることを示しています。

この更新により、Azure AIモデル推論APIを利用したモデルのデプロイ時に、コンテンツ安全性が有効化されている場合の入力および出力に関する説明が一貫して提供されるようになります。特に、ユーザーが有害なコンテンツを検出し防ぐための処理についての理解を得やすくなるでしょう。また、関連する例も引き続き提供され、実際の実装方法についての情報が強化されています。これにより、開発者が安全性を確保したモデルを構築する際の指針が明確になります。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -428,7 +428,7 @@ response = client.complete(
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -881,7 +881,7 @@ var result = await client.path("/chat/completions").post({
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1362,7 +1362,7 @@ response = client.Complete(requestOptions);
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1970,7 +1970,7 @@ View the response from the model:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「Mistral-NeMo」モデルのデプロイ方法に関するドキュメントの「コンテンツ安全性を適用」セクションにおいて、コンテンツフィルタリングシステムに関する記述を更新しています。具体的には、コンテンツフィルタリングシステムが「プレビュー」段階にあることを示すために、表現が「コンテンツフィルタリングシステム」から「コンテンツフィルタリング（プレビュー）システム」に変更されました。

この更新により、Azure AIモデル推論APIを利用してデプロイする際のコンテンツ安全性の使用に関するガイドラインが明確化されています。具体的には、入力および出力が有害なコンテンツを検出し防ぐためのプロセスを通過することが強調されており、システムがどのようにして危険なコンテンツを特定し、対処するかの詳細が提供されています。また、関連する例が含まれており、開発者が実装を行う際の参考となる情報が強化されています。これにより、ユーザーは安全性を考慮したモデルのデプロイに関する理解を深めることができます。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -458,7 +458,7 @@ response = client.complete(
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -941,7 +941,7 @@ var result = await client.path("/chat/completions").post({
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1452,7 +1452,7 @@ response = client.Complete(requestOptions);
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -2090,7 +2090,7 @@ View the response from the model:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「Mistral」モデルをデプロイする方法に関するドキュメントの「コンテンツ安全性を適用」セクションにおいて、コンテンツフィルタリングシステムの説明に関する修正が行われています。具体的には、「コンテンツフィルタリングシステム」という表現が「コンテンツフィルタリング（プレビュー）システム」に変更され、これによりこの機能が現時点でプレビュー版であることが明示されました。

この更新により、Azure AIモデル推論APIを使用している際のコンテンツ安全性の実装に関する情報が補強され、ユーザーは入力および出力において有害な内容を検出し防止するためのプロセスについての理解を深めることができます。また、「危険なコンテンツを検出した場合の処理例」が引き続き提供されており、開発者が具体的な実装方法を理解するのに役立つ情報が強化されています。これにより、ユーザーはより安全で効果的にモデルをデプロイできるようになります。

## articles/ai-studio/how-to/deploy-models-phi-3-5-vision.md{#item-8d6d7d}

<details>
<summary>Diff</summary>
````diff
@@ -280,7 +280,7 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -665,7 +665,7 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1074,7 +1074,7 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1493,7 +1493,7 @@ The following extra parameters can be passed to Phi-3.5 chat model with vision:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「Phi-3.5ビジョン」モデルのデプロイ方法に関するドキュメントの「コンテンツ安全性を適用」セクションにおいて、コンテンツフィルタリングシステムの説明を更新するものです。具体的には、「コンテンツフィルタリングシステム」という用語が「コンテンツフィルタリング（プレビュー）システム」に変更され、この機能がプレビュー状態であることを明確に示しています。

この更新は、Azure AIモデル推論APIを使用する際のコンテンツ安全性の実装に関する情報を強化し、ユーザーが入力および出力において有害なコンテンツを検出し防ぐためのプロセスを理解するのに役立ちます。また、システムの動作およびその重要性についての具体的な例が維持されており、開発者はコンテンツ安全性が有効な場合のリスク管理方法を適切に学ぶことができます。このようにして、ユーザーはより安全にモデルをデプロイし、運用することが可能となります。

## articles/ai-studio/how-to/deploy-models-phi-3.md{#item-47e305}

<details>
<summary>Diff</summary>
````diff
@@ -314,7 +314,7 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -659,7 +659,7 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1022,7 +1022,7 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
@@ -1410,7 +1410,7 @@ The following extra parameters can be passed to Phi-3 family chat models:
 
 ### Apply content safety
 
-The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングシステムのプレビュー通知の追加"
}
```

### Explanation
この変更は、「Phi-3」モデルのデプロイ方法に関するドキュメントの「コンテンツ安全性を適用」セクションにおいて、コンテンツフィルタリングシステムの説明を改訂したものです。具体的には、「コンテンツフィルタリングシステム」という表現が「コンテンツフィルタリング（プレビュー）システム」に変更され、これによりこの機能が現在プレビューにあることを明確に示しています。

この更新により、Azure AIモデル推論APIを使用する際のコンテンツ安全性についての理解が深まります。ユーザーは、デプロイメント時にコンテンツ安全性を有効にすると、入力と出力が有害なコンテンツを検出し防止するための分類モデルの集合を通過することを理解できます。また、モデルが入力プロンプト内に危険なコンテンツを検出した場合の処理方法について、具体的な例が示されており、開発者が安全にモデルを運用するための手助けが強化されています。こうした内容の明確化により、ユーザーはより安心してモデルを活用できるようになります。

## articles/ai-studio/how-to/deploy-models-serverless.md{#item-f8177f}

<details>
<summary>Diff</summary>
````diff
@@ -325,7 +325,7 @@ In this section, you create an endpoint with the name **meta-llama3-8b-qwerty**.
 
         :::image type="content" source="../media/deploy-monitor/serverless/deployment-name.png" alt-text="A screenshot showing how to specify the name of the deployment you want to create." lightbox="../media/deploy-monitor/serverless/deployment-name.png":::
        > [!TIP]
-       > The **Content filter (preview)** option is enabled by default. Leave the default setting for the service to detect harmful content such as hate, self-harm, sexual, and violent content. For more information about content filtering, see [Content filtering in Azure AI Studio](../concepts/content-filtering.md).
+       > The **Content filter (preview)** option is enabled by default. Leave the default setting for the service to detect harmful content such as hate, self-harm, sexual, and violent content. For more information about content filtering (preview), see [Content filtering in Azure AI Studio](../concepts/content-filtering.md).
 
     1. Select **Deploy**. Wait until the deployment is ready and you're redirected to the Deployments page.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングのプレビュー通知の更新"
}
```

### Explanation
この変更は、サーバーレスモデルのデプロイ方法に関するドキュメントの一部を更新するもので、特にコンテンツフィルタリング機能に関する情報が改訂されています。具体的には、「コンテンツフィルタリング」の説明が「コンテンツフィルタリング（プレビュー）」に変更され、フィルタリング機能が現在プレビュー段階にあることを明確に伝える内容になっています。

この更新は、利用者がデフォルト設定のままで有害なコンテンツ（ヘイト、自己傷害、性的、暴力的なコンテンツ）を検出するサービスの機能を理解しやすくすることを目的としています。また、文書内のリファレンスも更新され、ユーザーはコンテンツフィルタリングの詳細にアクセスしやすくなっています。これにより、Azure AI Studioを利用するユーザーは、コンテンツ安全性についての理解を深め、安全にサービスを活用できるようになります。

## articles/ai-studio/how-to/fine-tune-model-llama.md{#item-2a42d8}

<details>
<summary>Diff</summary>
````diff
@@ -269,7 +269,7 @@ For more information on how to track costs, see [monitor costs for models offere
 
 ## Content filtering
 
-Models deployed as a service with pay-as-you-go billing are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](../concepts/content-filtering.md).
+Models deployed as a service with pay-as-you-go billing are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](../concepts/content-filtering.md).
 
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングのプレビュー通知の追加"
}
```

### Explanation
この変更は、Llamaモデルのファインチューニングに関するドキュメントの「コンテンツフィルタリング」セクションを更新したものです。具体的には、従来の「コンテンツフィルタリングシステム」という表現が「コンテンツフィルタリング（プレビュー）システム」に変更され、フィルタリング機能が現在プレビュー段階であることが明確に示されています。

これにより、ユーザーは、ペイ・アズ・ユー・ゴーの課金が適用されたサービスとしてデプロイされたモデルが、Azure AIコンテンツ安全性によって保護されることを理解しやすくなります。また、リアルタイムエンドポイントにデプロイされた場合にこの機能からオプトアウトできることや、入力プロンプトと出力の両方が有害なコンテンツを検出するための分類モデルを通過することが強調されています。これにより、ユーザーはコンテンツ安全性の重要性を認識し、安全にサービスを利用できるよう指針が与えられています。

## articles/ai-studio/how-to/fine-tune-phi-3.md{#item-5b722a}

<details>
<summary>Diff</summary>
````diff
@@ -130,8 +130,8 @@ To fine-tune a Phi-3 model:
 
     > [!NOTE]
     > If the you have your training/validation files in a credential less datastore, you will need to allow workspace managed identity access to your datastore in order to proceed with MaaS fine-tuning with a credential less storage. On the "Datastore" page, after clicking "Update authentication" > Select the following option: 
-	
-	![Use workspace managed identity for data preview and profiling in Azure Machine Learning Studio.](../media/how-to/fine-tune/phi-3/credentials.png)
+    
+    ![Use workspace managed identity for data preview and profiling in Azure Machine Learning Studio.](../media/how-to/fine-tune/phi-3/credentials.png)
 
     Make sure all your training examples follow the expected format for inference. To fine-tune models effectively, ensure a balanced and diverse dataset. This involves maintaining data balance, including various scenarios, and periodically refining training data to align with real-world expectations, ultimately leading to more accurate and balanced model responses.
     - The batch size to use for training. When set to -1, batch_size is calculated as 0.2% of examples in training set and the max is 256.
@@ -167,8 +167,8 @@ To fine-tune a Phi-3 model:
 
     > [!NOTE]
     > If you have your training/validation files in a credential less datastore, you will need to allow workspace managed identity access to your datastore in order to proceed with MaaS finetuning with a credential less storage. On the "Datastore" page, after clicking "Update authentication" > Select the following option: 
-	
-	![Use workspace managed identity for data preview and profiling in Azure Machine Learning Studio.](../media/how-to/fine-tune/phi-3/credentials.png)
+    
+    ![Use workspace managed identity for data preview and profiling in Azure Machine Learning Studio.](../media/how-to/fine-tune/phi-3/credentials.png)
 
     Make sure all your training examples follow the expected format for inference. To fine-tune models effectively, ensure a balanced and diverse dataset. This involves maintaining data balance, including various scenarios, and periodically refining training data to align with real-world expectations, ultimately leading to more accurate and balanced model responses.
     - The batch size to use for training. When set to -1, batch_size is calculated as 0.2% of examples in training set and the max is 256.
@@ -199,7 +199,7 @@ Phi models fine-tuned as a service are offered by Microsoft and integrated with
 
 ## Content filtering
 
-Models deployed as a service with pay-as-you-go are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](../concepts/content-filtering.md).
+Models deployed as a service with pay-as-you-go are protected by Azure AI Content Safety. When deployed to real-time endpoints, you can opt out of this capability. With Azure AI content safety enabled, both the prompt and completion pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions. Learn more about [Azure AI Content Safety](../concepts/content-filtering.md).
 
 
 ## Next steps
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングのプレビュー通知の追加と注意点の明確化"
}
```

### Explanation
この変更は、Phi-3モデルのファインチューニングに関するドキュメントの更新です。主な変更点は二つあります。一つ目は、認証なしのデータストアにおけるトレーニングおよびバリデーションファイルに関する注意事項が改訂され、画像が適切に表示されるようにマークアップが修正されました。これによりユーザーは、Azure Machine Learning StudioにおけるデータのプレビューとプロファイリングのためにワークスペースのManaged Identityを使用するオプションをより簡単に確認できるようになります。

二つ目は、「コンテンツフィルタリング」セクションの更新で、コンテンツフィルタリングシステムが「コンテンツフィルタリング（プレビュー）」に改名され、現在プレビュー段階であることが明示されました。これにより、ユーザーはAzure AIコンテンツ安全性に関する重要な情報をより明確に理解でき、デフォルトで有害なコンテンツを検出するシステムの利用についての認識が高まります。この更新は、利用者が安全にサービスを利用するための手助けとなります。

## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -455,7 +455,7 @@ __Response__
 
 ## Content safety
 
-The Azure AI model inference API supports [Azure AI Content Safety](../concepts/content-filtering.md). When using deployments with Azure AI Content Safety on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+The Azure AI model inference API supports [Azure AI Content Safety](../concepts/content-filtering.md). When using deployments with Azure AI Content Safety on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
 
 The following example shows the response for a chat completion request that has triggered content safety. 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コンテンツフィルタリングのプレビュー通知の追加"
}
```

### Explanation
この変更は、Azure AIモデル推論APIに関するドキュメントの「コンテンツ安全性」セクションの更新です。主な修正点は、Azure AIコンテンツ安全性が提供されていることを説明する部分で、「コンテンツフィルタリングシステム」が「コンテンツフィルタリング（プレビュー）システム」に変更されました。

この変更により、ユーザーはコンテンツフィルタリング機能が現在プレビュー段階であることを明確に理解できるようになります。具体的には、Azure AIコンテンツ安全性を利用したデプロイメントにおいて、入力と出力が有害なコンテンツを検出し防止するための分類モデルのエンサンブルを通過するプロセスが説明されています。この更新により、ユーザーはシステムの使用状況をより正確に把握でき、コンテンツ安全性の重要性についての理解を深めることができます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -315,9 +315,8 @@ items:
     - name: Configure managed network
       href: how-to/configure-managed-network.md
     - name: Configure private link
+      displayName: custom dns
       href: how-to/configure-private-link.md
-    - name: Configure custom DNS
-      href: /azure/machine-learning/how-to-custom-dns?context=/azure/ai-studio/context/context
     - name: Secure playground chat
       href: how-to/secure-data-playground.md
     - name: Troubleshoot secure project connectivity
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムDNSの表示名の追加と不要な項目の削除"
}
```

### Explanation
この変更は、AIスタジオに関連するドキュメントの目次ファイル（toc.yml）の更新です。主な内容としては、以下の点が挙げられます。

1. **カスタムDNSに関する表示名の追加**: 「Configure private link」の下に、「custom dns」という表示名が新しく追加されました。これにより、ユーザーに対してそのセクションの内容がより分かりやすくなります。

2. **不要な項目の削除**: 「Configure custom DNS」という項目が完全に削除されました。これにより、目次が整理され、より簡潔な情報提供が可能になります。

この更新により、AIスタジオに関する情報がより明確に整理され、ユーザーが必要な情報にアクセスしやすくなります。

## articles/ai-studio/tutorials/deploy-chat-web-app.md{#item-987845}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ The steps in this tutorial are:
 
 - An [Azure AI Search service connection](../how-to/connections-add.md#create-a-new-connection) to index the sample product data. 
 
-- You need a local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. Specifically, the `product_info_11.md` file contains product information about the TrailWalker hiking shoes that's relevant for this tutorial example. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/raw/main/tutorial/data.zip) to your local machine.
+- You need a local copy of product data. The [Azure-Samples/rag-data-openai-python-promptflow repository on GitHub](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/) contains sample retail product information that's relevant for this tutorial scenario. Specifically, the `product_info_11.md` file contains product information about the TrailWalker hiking shoes that's relevant for this tutorial example. [Download the example Contoso Trek retail product data in a ZIP file](https://github.com/Azure-Samples/rag-data-openai-python-promptflow/raw/refs/heads/main/tutorial/data/product-info.zip) to your local machine.
 
 - You need to have **Microsoft.Web** resource provider registered in the selected subscription, to be able to deploy to a web app.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "製品データのダウンロードリンクの更新"
}
```

### Explanation
この変更は、チャットウェブアプリをデプロイするためのチュートリアルに関するドキュメントを更新したものです。具体的には、製品データのダウンロードリンクが修正されました。

変更内容は以下の通りです：

1. **ダウンロードリンクの更新**: 元のダウンロードリンクは、製品データのZIPファイルにアクセスするためのものでしたが、それが新しいリンクに変更されました。新しいリンクは、データが正しい場所に配置されていることを反映しています（`refs/heads/main/tutorial/data/product-info.zip`）。この変更により、ユーザーは最新の製品データにアクセスしやすくなります。

この修正により、チュートリアルがより正確になり、ユーザーが必要な製品データを簡単に取得できるようになります。


