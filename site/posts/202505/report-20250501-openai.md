---
date: '2025-05-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8a8182...MicrosoftDocs:0ff32a6
summary: このコード修正では、Azure OpenAIに関するドキュメント全体で軽微な修正が行われました。主な変更点は、各ドキュメントの日付更新、GPT-4.1およびGPT-4.1-miniモデルの追加支援、用語の整理とモデル名の改善です。特に注意すべき破壊的な変更はありませんが、用語やモデルバージョンの変更が見られます。これらの更新は、ドキュメントの最新性と正確性を確保するために重要であり、情報の鮮度を保ち、ユーザーが最新の技術にアクセスできるようにしています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8a8182...MicrosoftDocs:0ff32a6){target="_blank"}

<format>
# Highlights
このコード修正では、Azure OpenAIに関するドキュメント全体にわたる軽微な修正が行われています。主な変更は各ドキュメントの日付更新、モデル名やバージョンの改善、そして用語の整理です。

## New features
- GPT-4.1モデルおよびGPT-4.1-miniモデルのサポートが追加され、ファインチューニングおよびモデルのデプロイに関するドキュメントが更新されました。

## Breaking changes
- 特記すべき破壊的な変更はありませんが、用語やモデルバージョンが一部で変更されており、注意が必要です。

## Other updates
- 多くのドキュメントで`ms.date`の日付が最新情報を反映するように更新されています。
- モデル名やAPIバージョンの変更、用語の変更が複数のセクションで実施され、ドキュメントの一貫性が向上しています。

# Insights
この一連の変更は、Azure OpenAIのドキュメントの最新性と正確性を保つためのものでした。日付の更新により、情報鮮度がユーザーに伝わりやすくなり、モデルの名称やバージョンの変更により、ユーザーが最新の技術や更新にアクセスできるようになっています。

Azure OpenAIのサービスでは、モデルの進化が非常に速いため、ドキュメントもその変化に合わせて迅速に更新される必要があります。例えば、GPT-4.1やGPT-4.1-miniの追加により、AIの可能性をさらに広げることができ、これに関するファインチューニングのドキュメント更新は重要な役割を果たします。また、用語の整理により一貫性が確保され、ユーザーは混乱することなくサービスを利用できます。

日付の更新は見た目には小さな変更に見えるかもしれませんが、実際には情報が古くなっていないことをユーザーに示す重要な手段です。これにより、ユーザーは最適な情報に基づいて行動でき、特にビジネス上の意思決定を支える正確な情報を利用できるようになります。

</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [legacy-models.md](#item-f6918a) | minor update | レガシーモデルの日付更新 | modified | 1 | 1 | 2 | 
| [model-versions.md](#item-304d14) | minor update | モデルバージョンの日付更新とテキストの明確化 | modified | 2 | 2 | 4 | 
| [create-resource.md](#item-c1c8a3) | minor update | リソース作成に関する日付更新 | modified | 1 | 1 | 2 | 
| [dall-e.md](#item-ac9616) | minor update | DALL-Eの応答フォーマットのテキスト修正 | modified | 1 | 1 | 2 | 
| [deployment-types.md](#item-210814) | minor update | デプロイメントタイプに関する日付更新 | modified | 1 | 1 | 2 | 
| [dynamic-quota.md](#item-b774ca) | minor update | ダイナミッククォータに関する日付の更新 | modified | 1 | 1 | 2 | 
| [evaluations.md](#item-dfaa1c) | minor update | 評価に関する日付の更新 | modified | 1 | 1 | 2 | 
| [manage-costs.md](#item-93c3f3) | minor update | コスト管理に関する日付と内容の更新 | modified | 2 | 2 | 4 | 
| [managed-identity.md](#item-1a0afd) | minor update | マネージドIDに関する日付とAPIバージョンの更新 | modified | 3 | 3 | 6 | 
| [migration-javascript.md](#item-19dac7) | minor update | JavaScriptマイグレーションに関する日付の更新 | modified | 1 | 1 | 2 | 
| [quota.md](#item-9440c2) | minor update | クォータに関する情報の更新 | modified | 15 | 15 | 30 | 
| [assistants-ai-studio.md](#item-1632e2) | minor update | AIスタジオの前提条件に関する更新 | modified | 1 | 1 | 2 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | ChatGPT JavaScriptに関する日付情報の更新 | modified | 1 | 1 | 2 | 
| [create-resource-cli.md](#item-0c4e91) | minor update | リソース作成CLIに関するモデル名とバージョンの更新 | modified | 3 | 3 | 6 | 
| [create-resource-powershell.md](#item-df9cc4) | minor update | PowerShellリソース作成に関するモデル名とバージョンの更新 | modified | 3 | 3 | 6 | 
| [fine-tune-models.md](#item-2aadea) | minor update | ファインチューニングモデルの文書における出力形式の更新 | modified | 1 | 1 | 2 | 
| [fine-tuning-openai-in-ai-studio.md](#item-723c8d) | minor update | AI Studioにおけるファインチューニングサポートモデルの更新 | modified | 2 | 1 | 3 | 
| [fine-tuning-python.md](#item-976f58) | minor update | ファインチューニングに関するPythonドキュメントの更新 | modified | 4 | 2 | 6 | 
| [fine-tuning-rest.md](#item-9add3e) | minor update | REST APIによるファインチューニングサポートモデルの更新 | modified | 2 | 0 | 2 | 
| [fine-tuning-studio.md](#item-439f1e) | minor update | スタジオによるファインチューニングサポートモデルの更新 | modified | 2 | 0 | 2 | 
| [fine-tuning-unified.md](#item-718336) | minor update | ファインチューニングの表現更新 | modified | 1 | 1 | 2 | 
| [gpt-v-studio.md](#item-dcd50e) | minor update | Azure AI Foundry の用語変更 | modified | 2 | 2 | 4 | 
| [reference.md](#item-7b1183) | minor update | ドキュメントの日付の更新 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/legacy-models.md{#item-f6918a}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the deprecated models in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 ms.custom: references_regions, build-2023, build-2023-dataai
 manager: nitinme
 author: mrbullwinkle 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "レガシーモデルの日付更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するドキュメントのレガシーモデルのセクションにおける日付を更新することを目的としています。具体的には、`ms.date`フィールドの値を「2025年1月31日」から「2025年4月30日」へ変更しました。この修正により、ユーザーが最新の情報に基づいて内容を理解しやすくなります。変更されたファイルは、GitHubリポジトリの特定の場所にあり、リンク（[こちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fconcepts%2Flegacy-models.md)）からアクセスできます。

## articles/ai-services/openai/concepts/model-versions.md{#item-304d14}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about model versions in Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 01/09/2025
+ms.date: 04/30/2025
 manager: nitinme
 author: mrbullwinkle #ChrisHMSFT
 ms.author: mbullwin #chrhoder
@@ -45,7 +45,7 @@ As a customer of Azure OpenAI models, you might notice some changes in the model
 
 Yes, even in cases where the latest model version is not yet available in a region, we will automatically 
 upgrade deployments during the scheduled upgrade window. Our engineering team will begin rollout of the new model version starting on the announced 
-upgrade date. For example, if `gpt-35-turbo-0125` is not yet available in Japan East, we will deploy it to Japan East to upgrade older model 
+upgrade date. For example, if `gpt-35-turbo-0125` is not yet available in Japan East, we will deploy `gpt-35-turbo-0125` to Japan East to upgrade older model 
 versions as part of the default model version upgrade process. 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルバージョンの日付更新とテキストの明確化"
}
```

### Explanation
このコードの変更は、Azure OpenAIに関するモデルバージョンの説明ドキュメントに対するもので、二つの重要な修正が行われています。一つ目は、`ms.date`フィールドの更新です。日付が「2025年1月9日」から「2025年4月30日」に修正され、最新の情報が反映されています。二つ目は、テキストの明確化です。具体的には、モデルバージョンのアップグレードに関する説明文の一部が修正され、使用されるモデル名（`gpt-35-turbo-0125`）が記述され、より理解しやすくなりました。この変更により、ユーザーはAzure OpenAIのモデルバージョンの更新プロセスについて、より明瞭に把握できるようになります。変更内容は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fconcepts%2Fmodel-versions.md)）。

## articles/ai-services/openai/how-to/create-resource.md{#item-c1c8a3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: devx-track-azurecli, build-2023, build-2023-dataai, devx-track-azurepowershell, innovation-engine
 ms.topic: how-to
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 zone_pivot_groups: openai-create-resource
 author: mrbullwinkle
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース作成に関する日付更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのリソース作成に関するドキュメントの更新です。主な修正点は、`ms.date`フィールドの日付を「2025年1月31日」から「2025年4月30日」に変更したことです。この修正により、ドキュメントに記載されている情報が最新のものと一致するようになります。これによって、ユーザーは、リソース作成の手続きに関する情報が最新であることを確認できるため、より信頼性の高いガイダンスを得ることができます。変更内容の詳細は、こちらのリンクから閲覧できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fcreate-resource.md)）。

## articles/ai-services/openai/how-to/dall-e.md{#item-ac9616}

<details>
<summary>Diff</summary>
````diff
@@ -232,7 +232,7 @@ With DALL-E 3, you can't generate more than one image in a single API call: the
 
 #### Response format
 
-The format in which dall-e-3 generated images are returned. Must be one of `url` or `b64_json`. This parameter isn't supported for gpt-image-1 which will always return base64-encoded images.
+The format in which DALL-E 3 generated images are returned. Must be one of `url` or `b64_json`. This parameter isn't supported for GPT-image-1 which always returns base64-encoded images.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eの応答フォーマットのテキスト修正"
}
```

### Explanation
このコードの変更は、DALL-Eに関するドキュメントの一部を修正したものです。重要な修正点は、返される画像フォーマットに関する説明の文言を微調整したことです。具体的には、"dall-e-3"という表記が"DALL-E 3"に変更され、同様に"gpt-image-1"も"GPT-image-1"と修正されています。この変更により、製品名の表記が一貫性を持ち、より明確で読みやすくなります。ユーザーはDALL-Eの応答フォーマットについての理解を深めることができ、ドキュメントの信頼性が向上します。詳細については、こちらのリンクからご確認ください（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fdall-e.md)）。

## articles/ai-services/openai/how-to/deployment-types.md{#item-210814}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/24/2025
+ms.date: 04/30/2025
 ms.author: mbullwin
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントタイプに関する日付更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのデプロイメントタイプに関するドキュメントの日付を更新するものです。具体的には、`ms.date`フィールドの日付を「2025年1月24日」から「2025年4月30日」に変更しました。この修正により、ドキュメントの情報が最新のものと一致し、ユーザーは最新のガイダンスに基づいて適切な判断を行うことができるようになります。正確な情報は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fdeployment-types.md)）。

## articles/ai-services/openai/how-to/dynamic-quota.md{#item-b774ca}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 ms.author: mbullwin
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ダイナミッククォータに関する日付の更新"
}
```

### Explanation
このコードの変更は、ダイナミッククォータに関するドキュメントの日付を更新するもので、具体的には`ms.date`フィールドが「2025年1月31日」から「2025年4月30日」に変更されました。この更新により、ドキュメントは最新の情報を反映し、ユーザーに正確なガイダンスを提供することができます。日付の変更は、情報の整合性を確保し、利用者が最新のコンテンツにアクセスできるようにするための重要な手続きです。詳細は、こちらのリンクからご確認いただけます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fdynamic-quota.md)）。

## articles/ai-services/openai/how-to/evaluations.md{#item-dfaa1c}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
 ms.custom: references_regions
-ms.date: 01/29/2025
+ms.date: 04/30/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "評価に関する日付の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIの評価に関するドキュメントの日付を更新するもので、具体的には`ms.date`フィールドが「2025年1月29日」から「2025年4月30日」に変更されました。この更新は、ドキュメントの正確性を保つためのものであり、ユーザーに最新の情報を提供することを目的としています。正確で最新の情報は、利用者が適切な判断を下すために重要です。詳細は、こちらのリンクで確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fevaluations.md)）。

## articles/ai-services/openai/how-to/manage-costs.md{#item-93c3f3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ ms.author: mbullwin
 ms.custom: subject-cost-optimization
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 ---
 
 
@@ -30,7 +30,7 @@ Azure OpenAI Service runs on Azure infrastructure that accrues costs when you de
 
 ### Model inference chat completions
 
-Azure OpenAI chat completions model inference is [charged per 1,000 tokens with different rates](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) depending on model and [deployment type](./deployment-types.md).
+Azure OpenAI chat completions model inference is [charged per 1,000 tokens with different rates](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) depending on model and [deployment type](./deployment-types.md). For most models pricing is now listed in terms of 1 million tokens.
 
 Azure OpenAI models understand and process text by breaking it down into tokens. For reference, each token is roughly four characters for typical English text.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "コスト管理に関する日付と内容の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるコスト管理に関するドキュメントにおいて、日付の更新と内容の改訂を含んでいます。具体的には、`ms.date`フィールドが「2025年1月31日」から「2025年4月30日」に修正されました。また、チャット完了モデルの推論に関する料金情報が更新され、従来は1,000トークンごとに料金が発生していたところから、多くのモデルで料金が今後は1百万トークン単位で表示されることに言及されました。この変更は、利用者がコストの見積もりをより正確に行えるようにするためのものであり、最新の情報提供を目的としています。詳細は、こちらのリンクからご確認いただけます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fmanage-costs.md)）。

## articles/ai-services/openai/how-to/managed-identity.md{#item-1a0afd}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Provides guidance on how to set managed identity with Microsoft Entra ID
 ms.service: azure-ai-openai
 ms.topic: how-to 
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 author: mrbullwinkle
 ms.author: mbullwin
 recommendations: false
@@ -50,13 +50,13 @@ token_provider = get_bearer_token_provider(
 )
 
 client = AzureOpenAI(
-    api_version="2024-02-15-preview",
+    api_version="2024-04-01-preview",
     azure_endpoint="https://{your-custom-endpoint}.openai.azure.com/",
     azure_ad_token_provider=token_provider
 )
 
 response = client.chat.completions.create(
-    model="gpt-35-turbo-0125", # model = "deployment_name".
+    model="gpt-4o", # model = "deployment_name".
     messages=[
         {"role": "system", "content": "You are a helpful assistant."},
         {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マネージドIDに関する日付とAPIバージョンの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIにおけるマネージドアイデンティティに関するドキュメントに対するもので、日付の更新とAPIバージョンの変更が含まれています。具体的には、`ms.date`フィールドが「2025年1月31日」から「2025年4月30日」に更新されました。また、APIバージョンも「2024-02-15-preview」から「2024-04-01-preview」に変更され、モデル名が「gpt-35-turbo-0125」から「gpt-4o」に修正されました。これらの変更は、ドキュメントの最新性を保ち、利用者に正確で新しい情報を提供することを目指しています。詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fmanaged-identity.md)）。

## articles/ai-services/openai/how-to/migration-javascript.md{#item-19dac7}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.author: mbullwin
 ms.service: azure-ai-openai
 ms.custom: devx-track-python
 ms.topic: how-to
-ms.date: 01/31/2025
+ms.date: 04/30/2025
 manager: nitinme
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptマイグレーションに関する日付の更新"
}
```

### Explanation
このコードの変更は、JavaScriptマイグレーションに関するドキュメントに対するもので、主に日付の atualizaçãoが含まれています。具体的には、`ms.date`フィールドが「2025年1月31日」から「2025年4月30日」に修正されました。この変更は、ドキュメントの適時性を保つことを目指しており、最新の情報を利用者に提供するために行われました。詳細については、以下のリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fmigration-javascript.md)）。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: mrbullwinkle
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: how-to
-ms.date: 01/09/2025
+ms.date: 04/30/2025
 ms.author: mbullwin
 ---
 
@@ -28,11 +28,11 @@ Quota provides the flexibility to actively manage the allocation of rate limits
 Azure OpenAI's quota feature enables assignment of rate limits to your deployments, up-to a global limit called your *quota*. Quota is assigned to your subscription on a per-region, per-model basis in units of **Tokens-per-Minute (TPM)**. When you onboard a subscription to Azure OpenAI, you'll receive default quota for most available models. Then, you'll assign TPM to each deployment as it is created, and the available quota for that model will be reduced by that amount. You can continue to create deployments and assign them TPM until you reach your quota limit. Once that happens, you can only create new deployments of that model by reducing the TPM assigned to other deployments of the same model (thus freeing TPM for use), or by requesting and being approved for a model quota increase in the desired region.
 
 > [!NOTE]
-> With a quota of 240,000 TPM for GPT-35-Turbo in East US, a customer can create a single deployment of 240 K TPM, 2 deployments of 120 K TPM each, or any number of deployments in one or multiple Azure OpenAI resources as long as their TPM adds up to less than 240 K total in that region.
+> With a quota of 240,000 TPM for GPT-4o in East US, a customer can create a single deployment of 240 K TPM, 2 deployments of 120 K TPM each, or any number of deployments in one or multiple Azure OpenAI resources as long as their TPM adds up to less than 240 K total in that region.
 
 When a deployment is created, the assigned TPM will directly map to the tokens-per-minute rate limit enforced on its inferencing requests. A **Requests-Per-Minute (RPM)** rate limit will also be enforced whose value is set proportionally to the TPM assignment using the following ratio:
 
-6 RPM per 1000 TPM.
+6 RPM per 1000 TPM. (This ratio can vary by model for more information, see [quota, and limits](../quotas-limits.md#o-series-rate-limits).)
 
 The flexibility to distribute TPM globally within a subscription and region has allowed Azure OpenAI Service to loosen other restrictions:
 
@@ -145,10 +145,10 @@ This is only a subset of the available request body parameters. For the full lis
 #### Example request
 
 ```Bash
-curl -X PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-temp/providers/Microsoft.CognitiveServices/accounts/docs-openai-test-001/deployments/gpt-35-turbo-test-deployment?api-version=2023-05-01 \
+curl -X PUT https://management.azure.com/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/resource-group-temp/providers/Microsoft.CognitiveServices/accounts/docs-openai-test-001/deployments/gpt-4o-test-deployment?api-version=2023-05-01 \
   -H "Content-Type: application/json" \
   -H 'Authorization: Bearer YOUR_AUTH_TOKEN' \
-  -d '{"sku":{"name":"Standard","capacity":10},"properties": {"model": {"format": "OpenAI","name": "gpt-35-turbo","version": "0613"}}}'
+  -d '{"sku":{"name":"Standard","capacity":10},"properties": {"model": {"format": "OpenAI","name": "gpt-4o","version": "2024-11-20"}}}'
 ```
 
 > [!NOTE]
@@ -215,7 +215,7 @@ az login
 By setting sku-capacity to 10 in the command below this deployment will be set with a 10K TPM limit.
 
 ```azurecli
-az cognitiveservices account deployment create -g test-resource-group -n test-resource-name --deployment-name test-deployment-name --model-name gpt-35-turbo --model-version "0613" --model-format OpenAI --sku-capacity 10 --sku-name "Standard"
+az cognitiveservices account deployment create -g test-resource-group -n test-resource-name --deployment-name test-deployment-name --model-name gpt-4o --model-version "2024-11-20" --model-format OpenAI --sku-capacity 10 --sku-name "Standard"
 ```
 
 ### Usage
@@ -272,8 +272,8 @@ $cognitiveServicesDeploymentParams = @{
     Name = 'test-deployment-name'
     Properties = @{
         Model = @{
-            Name = 'gpt-35-turbo'
-            Version = '0613'
+            Name = 'gpt-4o'
+            Version = '2024-11-20'
             Format  = 'OpenAI'
         }
     }
@@ -301,7 +301,7 @@ Get-AzCognitiveServicesUsage -Location eastus
 
 This command runs in the context of the currently active subscription for Azure PowerShell. Use `Set-AzContext` to [modify the active subscription](/powershell/azure/manage-subscriptions-azureps#change-the-active-subscription).
 
-For more details on `New-AzCognitiveServicesAccountDeployment` and `Get-AzCognitiveServicesUsage`, consult the [Azure PowerShell reference documentation](/powershell/module/az.cognitiveservices/).
+For more information on `New-AzCognitiveServicesAccountDeployment` and `Get-AzCognitiveServicesUsage`, see [Azure PowerShell reference documentation](/powershell/module/az.cognitiveservices/).
 
 # [Azure Resource Manager](#tab/arm)
 
@@ -324,8 +324,8 @@ For more details on `New-AzCognitiveServicesAccountDeployment` and `Get-AzCognit
     "properties": {
         "model": {
             "format": "OpenAI",
-            "name": "gpt-35-turbo",
-            "version": "0613"        // Version 0613 of gpt-35-turbo will be used
+            "name": "gpt-4o",
+            "version": "2024-11-20"       
         }
     }
 }
@@ -350,8 +350,8 @@ resource arm_je_std_deployment 'Microsoft.CognitiveServices/accounts/deployments
   properties: {
     model: {
       format: 'OpenAI'
-      name: 'gpt-35-turbo'
-      version: '0613'           // gpt-35-turbo version 0613 will be used
+      name: 'gpt-4o'
+      version: '2024-11-20'          
     }
   }
 }
@@ -425,8 +425,8 @@ resource "azapi_resource" "TERRAFORM-AOAI-STD-DEPLOYMENT" {
     properties = {
         model = {
             format = "OpenAI",
-            name = "gpt-35-turbo",
-            version = "0613"           # Deploy gpt-35-turbo version 0613
+            name = "gpt-4o",
+            version = "2024-11-20"           
         }
     }
   })
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クォータに関する情報の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのクォータに関するドキュメントにおける情報の更新を含んでいます。具体的には、`ms.date`が「2025年1月9日」から「2025年4月30日」に更新され、モデルの名称とバージョンが「gpt-35-turbo」および「0613」から「gpt-4o」と「2024-11-20」に変更されました。これにより、最新のモデルに基づく内容が反映され、ユーザーがクォータの管理に関する正確な情報を得ることができます。さらに、APIエンドポイントにおけるJSONリクエストの一部も対応する新しいモデルに合わせて修正されています。詳細については、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fhow-to%2Fquota.md)）。

## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ ms.author: aahi
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An [Azure AI hub resource](../../../ai-foundry/how-to/create-azure-ai-resource.md) with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+- A GTP-4 model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 - An [Azure AI project](../../../ai-foundry/how-to/create-projects.md) in Azure AI Foundry portal.
 
 ## Go to the Azure AI Foundry portal
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオの前提条件に関する更新"
}
```

### Explanation
このコードの変更は、AIスタジオに関するドキュメントの前提条件に関する情報の更新を含んでいます。具体的には、要求されるモデルに関する記述が変更されました。以前は「デプロイされたAzure AIハブリソース」と記載されていましたが、現在は「デプロイされたGTP-4モデル」に更新されています。この変更は、ユーザーが必要なリソースを正確に理解できるようにするためのもので、正確な情報を提供することを目的としています。詳細については、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Fassistants-ai-studio.md)）。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: mrbullwinkle
 ms.author: mbullwin
-ms.date: 10/22
+ms.date: 04/30/2025
 ---
 
 [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPT JavaScriptに関する日付情報の更新"
}
```

### Explanation
このコードの変更は、ChatGPTに関するJavaScriptのドキュメントにおける日付情報の更新を含んでいます。具体的には、`ms.date`の値が「10/22」から「2025年4月30日」に変更されました。この更新により、ドキュメントの内容が最新になるように整えられています。ユーザーが情報の鮮度を把握できるようにするため、日付が明示されていることは重要です。詳細については、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Fchatgpt-javascript.md)）。

## articles/ai-services/openai/includes/create-resource-cli.md{#item-0c4e91}

<details>
<summary>Diff</summary>
````diff
@@ -77,15 +77,15 @@ az cognitiveservices account keys list \
 
 ## Deploy a model
 
-To deploy a model, use the [az cognitiveservices account deployment create](/cli/azure/cognitiveservices/account/deployment?view=azure-cli-latest&preserve-view=true#az-cognitiveservices-account-deployment-create) command. In the following example, you deploy an instance of the `text-embedding-ada-002` model and give it the name _MyModel_. When you try the example, update the code to use your values for the resource group and resource. You don't need to change the `model-version`, `model-format` or `sku-capacity`, and `sku-name` values.
+To deploy a model, use the [az cognitiveservices account deployment create](/cli/azure/cognitiveservices/account/deployment?view=azure-cli-latest&preserve-view=true#az-cognitiveservices-account-deployment-create) command. In the following example, you deploy an instance of the `gpt-4o` model and give it the name _MyModel_. When you try the example, update the code to use your values for the resource group and resource. You don't need to change the `model-version`, `model-format` or `sku-capacity`, and `sku-name` values.
 
 ```azurecli
 az cognitiveservices account deployment create \
 --name <myResourceName> \
 --resource-group  <myResourceGroupName> \
 --deployment-name MyModel \
---model-name text-embedding-ada-002 \
---model-version "1"  \
+--model-name gpt-4o \
+--model-version "2024-11-20"  \
 --model-format OpenAI \
 --sku-capacity "1" \
 --sku-name "Standard"
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース作成CLIに関するモデル名とバージョンの更新"
}
```

### Explanation
このコードの変更は、Azure CLIを使用したモデルのデプロイに関するドキュメントの内容に対する更新を含んでいます。具体的には、デプロイされるモデルが「text-embedding-ada-002」から「gpt-4o」に変更され、同時にモデルのバージョンも「1」から「2024年11月20日」に更新されています。この変更により、ユーザーは最新のモデルをデプロイするための正確な手順を把握できるようになります。具体的なコマンドにおいても、モデル名とバージョンに関する部分が修正されています。詳細については、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Fcreate-resource-cli.md)）。

## articles/ai-services/openai/includes/create-resource-powershell.md{#item-df9cc4}

<details>
<summary>Diff</summary>
````diff
@@ -64,12 +64,12 @@ Get-AzCognitiveServicesAccountKey -Name MyOpenAIResource -ResourceGroupName OAIR
 
 ## Deploy a model
 
-To deploy a model, use the [New-AzCognitiveServicesAccountDeployment](/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccountdeployment) command. In the following example, you deploy an instance of the `text-embedding-ada-002` model and give it the name _MyModel_. When you try the example, update the code to use your values for the resource group and resource. You don't need to change the `model-version`, `model-format` or `sku-capacity`, and `sku-name` values. 
+To deploy a model, use the [New-AzCognitiveServicesAccountDeployment](/powershell/module/az.cognitiveservices/new-azcognitiveservicesaccountdeployment) command. In the following example, you deploy an instance of the `gpt-4o` model and give it the name _MyModel_. When you try the example, update the code to use your values for the resource group and resource. You don't need to change the `model-version`, `model-format` or `sku-capacity`, and `sku-name` values. 
 
 ```azurepowershell-interactive
 $model = New-Object -TypeName 'Microsoft.Azure.Management.CognitiveServices.Models.DeploymentModel' -Property @{
-    Name = 'text-embedding-ada-002'
-    Version = '2'
+    Name = 'gpt-4o'
+    Version = '2024-11-20'
     Format = 'OpenAI'
 }
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "PowerShellリソース作成に関するモデル名とバージョンの更新"
}
```

### Explanation
このコードの変更は、PowerShellを使用したモデルのデプロイに関するドキュメントの修正を含んでいます。具体的には、デプロイされるモデル名が「text-embedding-ada-002」から「gpt-4o」に変更され、モデルのバージョンも「2」から「2024年11月20日」に更新されています。この変更により、ユーザーは最新のモデルを使用して正確にデプロイするための手順を得ることができます。また、手順の説明においても、リソースグループやリソースについて自身の値に更新する必要があることが強調されています。詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Fcreate-resource-powershell.md)）。

## articles/ai-services/openai/includes/fine-tune-models.md{#item-2aadea}

<details>
<summary>Diff</summary>
````diff
@@ -21,5 +21,5 @@ manager: nitinme
 | `gpt-35-turbo` (0125)  | East US2 <br> North Central US <br> Sweden Central <br> Switzerland West | 16,385 | Sep 2021 | Text to Text |
 | `gpt-4o-mini` (2024-07-18) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 65,536 | Oct 2023 | Text to Text |
 | `gpt-4o` (2024-08-06) | East US2 <br> North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384  <br> Training example context length: 65,536 | Oct 2023 | Text & Vision to Text |
-| `gpt-4.1` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
+| `gpt-4.1` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text & Vision to Text |
 | `gpt-4.1-mini` (2025-04-14) | North Central US <br> Sweden Central | Input: 128,000 <br> Output: 16,384 <br> Training example context length: 65,536 | May 2024 | Text to Text |
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングモデルの文書における出力形式の更新"
}
```

### Explanation
このコードの変更は、ファインチューニングモデルに関するドキュメントの内容に対する軽微な修正を含んでいます。具体的には、`gpt-4.1`モデルのデプロイに関連する情報が更新され、出力形式の説明が「Text to Text」から「Text & Vision to Text」に変更されました。この変更は、ユーザーがモデルの機能をより正確に理解できるようにするためのものです。モデルの詳細な仕様に応じた正確な出力形式が反映されており、今後の使用時に重要な情報となります。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tune-models.md)）。

## articles/ai-services/openai/includes/fine-tuning-openai-in-ai-studio.md{#item-723c8d}

<details>
<summary>Diff</summary>
````diff
@@ -16,7 +16,6 @@ ms.custom: include, build-2024
 - Read the [When to use Azure OpenAI fine-tuning guide](../concepts/fine-tuning-considerations.md).
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
-- An [Azure AI hub resource](../../../ai-foundry/how-to/create-azure-ai-resource.md).
 - An [Azure AI project](../../../ai-foundry/how-to/create-projects.md) in Azure AI Foundry portal.
 - An [Azure OpenAI connection](/azure/ai-foundry/how-to/connections-add?tabs=azure-openai#connection-details) to a resource in a [region where fine-tuning is supported](/azure/ai-services/openai/concepts/models#fine-tuning-models).
     > [!NOTE]
@@ -32,6 +31,8 @@ The following models support fine-tuning:
 - `gpt-35-turbo` (0125)
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
+- `gpt-4.1` (2024-04-14)
+- `gpt-4.1-mini`(2025-04-14)
 
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AI Studioにおけるファインチューニングサポートモデルの更新"
}
```

### Explanation
このコードの変更は、AI Studioにおけるファインチューニングに関連するドキュメントの内容に関する軽微な修正を示しています。具体的には、ファインチューニングをサポートするモデルのリストに新たに`gpt-4.1`（2024年4月14日リリース）および`gpt-4.1-mini`（2025年4月14日リリース）が追加されました。また、`Azure AI hub resource`に関する行が削除され、文書がより簡潔になっています。この更新により、ユーザーはファインチューニングの際に利用可能な最新のモデル情報を取得でき、より効率的なAI開発が可能になります。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tuning-openai-in-ai-studio.md)）。

## articles/ai-services/openai/includes/fine-tuning-python.md{#item-976f58}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to create your own customized model with Azure OpenAI Ser
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 02/27/2025
+ms.date: 04/30/2025
 author: mrbullwinkle
 ms.author: mbullwin
 ---
@@ -29,6 +29,8 @@ The following models support fine-tuning:
 - `gpt-35-turbo` (0125)
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
+- `gpt-4.1` (2024-04-14)
+- `gpt-4.1-mini`(2025-04-14)
 
 Or you can fine tune a previously fine-tuned model, formatted as `base-model.ft-{jobid}`.
 
@@ -235,7 +237,7 @@ print(response.model_dump_json(indent=2))
 
 Azure OpenAI attaches a result file named _results.csv_ to each fine-tune job after it completes. You can use the result file to analyze the training and validation performance of your customized model. The file ID for the result file is listed for each customized model, and you can use the Python SDK to retrieve the file ID and download the result file for analysis.
 
-The following Python example retrieves the file ID of the first result file attached to the fine-tuning job for your customized model, and then uses the Python SDK to download the file to your working directory for analysis.
+The following Python example retrieves the file ID of the first result file attached to the fine-tuning job for your customized model, and then uses the Python SDK to download the file to your current working directory for analysis.
 
 ```python
 # Retrieve the file ID of the first result file from the fine-tuning job
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関するPythonドキュメントの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるファインチューニングに関連するPythonの使用方法についてのドキュメントの軽微な修正を含んでいます。主な変更点は以下の通りです。

1. ドキュメントの日付が2025年2月27日から2025年4月30日に更新されました。
2. ファインチューニングをサポートするモデルのリストに、`gpt-4.1`（2024年4月14日リリース）および`gpt-4.1-mini`（2025年4月14日リリース）が追加されました。
3. Pythonコードの説明が、「working directory」から「current working directory」に修正され、より明確な表現となっています。

これらの変更により、ユーザーは最新のモデル情報と、ファインチューニング作業の結果ファイルの取り扱いについてのより具体的な説明を得ることができるようになります。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tuning-python.md)）。

## articles/ai-services/openai/includes/fine-tuning-rest.md{#item-9add3e}

<details>
<summary>Diff</summary>
````diff
@@ -28,6 +28,8 @@ The following models support fine-tuning:
 - `gpt-35-turbo` (0125)
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
+- `gpt-4.1` (2024-04-14)
+- `gpt-4.1-mini`(2025-04-14)
 
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "REST APIによるファインチューニングサポートモデルの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるREST APIを使用したファインチューニングに関するドキュメントの軽微な修正を示しています。具体的には、ファインチューニングをサポートするモデルのリストに新たに`gpt-4.1`（2024年4月14日リリース）および`gpt-4.1-mini`（2025年4月14日リリース）が追加されました。この追加により、ユーザーは最新のモデル情報をより正確に把握できるようになっています。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tuning-rest.md)）。

## articles/ai-services/openai/includes/fine-tuning-studio.md{#item-439f1e}

<details>
<summary>Diff</summary>
````diff
@@ -26,6 +26,8 @@ The following models support fine-tuning:
 - `gpt-35-turbo` (0125)
 - `gpt-4o` (2024-08-06)
 - `gpt-4o-mini` (2024-07-18)
+- `gpt-4.1` (2024-04-14)
+- `gpt-4.1-mini`(2025-04-14)
 
 Or you can fine tune a previously fine-tuned model, formatted as base-model.ft-{jobid}.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタジオによるファインチューニングサポートモデルの更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスのスタジオにおけるファインチューニングに関連するドキュメントの軽微な修正を示しています。具体的には、ファインチューニングをサポートするモデルのリストに新たに`gpt-4.1`（2024年4月14日リリース）および`gpt-4.1-mini`（2025年4月14日リリース）が追加されました。この更新により、ユーザーは最新のモデルの利用可能性を把握しやすくなっています。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tuning-studio.md)）。

## articles/ai-services/openai/includes/fine-tuning-unified.md{#item-718336}

<details>
<summary>Diff</summary>
````diff
@@ -23,6 +23,6 @@ If you are only fine-tuning Azure OpenAI models, we recommend the Azure OpenAI c
 
 # [Hub/Project](#tab/hub)
 
-[!INCLUDE [Azure AI Foundry Hub/Project fine-tuning](../includes/fine-tuning-openai-in-ai-studio.md)]
+[!INCLUDE [Azure AI Foundry project fine-tuning](../includes/fine-tuning-openai-in-ai-studio.md)]
 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングの表現更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスにおけるファインチューニングに関するドキュメントの軽微な修正を表しています。具体的には、ファインチューニングに関連するインクルード文のタイトルが修正されました。以前は「Azure AI Foundry Hub/Project fine-tuning」と記載されていましたが、現在は「Azure AI Foundry project fine-tuning」に変更されています。この修正により、表現が一貫性を持つようになり、ユーザーにとってより明確な情報提供がなされています。変更の詳細は、こちらのリンクから確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Ffine-tuning-unified.md)）。

## articles/ai-services/openai/includes/gpt-v-studio.md{#item-dcd50e}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,7 @@ Use this article to get started using [Azure AI Foundry](https://ai.azure.com) t
 - An Azure subscription. <a href="https://azure.microsoft.com/free/ai-services" target="_blank">Create one for free</a>.
 - Once you have your Azure subscription, <a href="/azure/ai-services/openai/how-to/create-resource?pivots=web-portal"  title="Create an Azure OpenAI resource."  target="_blank">create an Azure OpenAI resource </a>.
  For more information about resource creation, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
-- An [Azure AI Foundry hub](/azure/ai-foundry/how-to/create-azure-ai-resource) with your Azure OpenAI resource added as a connection. 
+- An [Azure AI Foundry project](/azure/ai-foundry/how-to/create-projects) with your Azure OpenAI resource added as a connection. 
 
 ## Prepare your media
 
@@ -29,7 +29,7 @@ You need an image to complete this quickstart. You can use this sample image or
 ## Go to Azure AI Foundry
 
 1. Browse to [Azure AI Foundry](https://ai.azure.com/) and sign in with the credentials associated with your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
-1. Select the hub you'd like to work in.
+1. Select the project you'd like to work in.
 1. On the left nav menu, select **Models + endpoints** and select **+ Deploy model**.
 1. Choose an image-capable deployment by selecting model name: **gpt-4o** or **gpt-4o-mini**. In the window that appears, select a name and deployment type. Make sure your Azure OpenAI resource is connected. For more information about model deployment, see the [resource deployment guide](/azure/ai-services/openai/how-to/create-resource).
 1. Select **Deploy**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundry の用語変更"
}
```

### Explanation
このコードの変更は、Azure OpenAIサービスに関連するドキュメントにおける用語の軽微な修正を示しています。具体的には、Azure AI Foundryでの用語が「hub」から「project」に変更されました。この変更は、ユーザーが作業する際の用語を一貫性のあるものにするためのものであり、理解を容易にします。具体的な修正内容としては、リソースを接続するための要件が「Azure AI Foundry hub」から「Azure AI Foundry project」に変わり、ユーザーが選択するべき項目が更新されています。この変更の詳細は、以下のリンクで確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Fincludes%2Fgpt-v-studio.md)）。

## articles/ai-services/openai/reference.md{#item-7b1183}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Learn how to use Azure OpenAI's REST API. In this article, you lear
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 01/29/2025
+ms.date: 04/30/2025
 author: mrbullwinkle 
 ms.author: mbullwin
 recommendations: false
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付の更新"
}
```

### Explanation
このコードの変更は、Azure OpenAIのリファレンス文書における日付の修正を示しています。具体的には、文書の「ms.date」フィールドが「2025年1月29日」から「2025年4月30日」に更新されました。この変更により、記事がより最新の情報を反映することができるようになります。日付の更新は、コンテンツが古くなっていないかを示すために重要であり、読者にとって有用な情報源としての信頼性を高めます。変更の詳細は、以下のリンクで確認できます（[リンクはこちら](https://github.com/MicrosoftDocs/azure-ai-docs/blob/0ff32a60972f3b5792cd0aa4e4b4626f5335696d/articles%2Fai-services%2Fopenai%2Freference.md)）。


