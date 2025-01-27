---
date: '2025-01-27'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c67b444...MicrosoftDocs:9cc44af
summary: この変更では、Azure AIモデル推論APIに関するドキュメントがマイナーアップデートされ、主に新しい情報の追加や用語の修正が行われました。特に「モデル/システム」への用語変更と、具体的なサポート対象モデルへのリンクの追加が強調されています。また、REST
  APIの使用に関する基本URL形式の情報も更新され、開発者の理解をサポートする資料が提供されています。全体として、今回の更新はAzure AIのモデル推論APIを利用する開発者にとって、より明確で詳細な情報を提供することを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:c67b444...MicrosoftDocs:9cc44af){target="_blank"}

# ハイライト
この変更では、Azure AIモデル推論APIに関するドキュメントがマイナーアップデートされました。主な焦点は、新しい情報の追加や用語の修正にあり、特に「モデル/システム」への用語の変更と具体的なサポート対象モデルへのリンクの追加が行われています。また、基本URL形式やREST APIの使用に関する情報も強調されています。これらはすべて開発者の理解をサポートするために行われています。

## 新機能
- 「Azure AI Servicesにおけるモデル推論」のセクションが新たに追加され、具体的なサポート対象モデルへのリンクが提供されています。
  
## 破壊的変更
- 特に破壊的変更はありませんが、用語の変更に伴い、「Azure AI Model Inference APIが利用可能なモデル」が「モデル/システム」へと名称が変更されています。

## その他の更新
- REST APIを使用する際の基本URL形式に関する記述が加わり、開発者にとって利用しやすい資料となっています。

# インサイト
今回のドキュメント更新は、Azure AIのモデル推論APIを利用する開発者に対して、より明確で詳細な情報を提供することを目的としています。新しい用語の採用により、一貫性のある表現が使われるようになり、開発者が混乱なくシステムを理解できることを目指しています。さらに、REST APIの基本URL形式や具体的なリンク情報が追加されたことで、高度な使用ケースに対するガイドが強化されました。これにより、開発者によるAPIの正確かつ効率的な利用が促進されることが期待されます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [reference-model-inference-api.md](#item-9fe240) | minor update | モデル推論APIに関するドキュメントの更新 | modified | 9 | 1 | 10 | 


# Modified Contents
## articles/ai-studio/reference/reference-model-inference-api.md{#item-9fe240}

<details>
<summary>Diff</summary>
````diff
@@ -36,7 +36,7 @@ Having a uniform way to consume foundational models allow developers to realize
 
 ## Availability
 
-The Azure AI Model Inference API is available in the following models:
+The Azure AI Model Inference API is available in the following models/systems:
 
 Models deployed to [serverless API endpoints](../how-to/deploy-models-serverless.md):
 
@@ -58,6 +58,11 @@ Models deployed to [managed inference](../concepts/deployments-overview.md):
 > * [Phi-3](../how-to/deploy-models-phi-3.md), and [Phi-4](../how-to/deploy-models-phi-4.md) family of models
 > * [Mistral](../how-to/deploy-models-mistral-open.md) and [Mixtral](../how-to/deploy-models-mistral-open.md?tabs=mistral-8x7B-instruct) family of models
 
+Models deployed to [Azure AI model inference in Azure AI Services](../../ai-foundry/model-inference/overview.md):
+
+> [!div class="checklist"]
+> * See [supported models](../../ai-foundry/model-inference/concepts/models.md).
+
 The API is compatible with Azure OpenAI model deployments.
 
 > [!NOTE]
@@ -81,6 +86,9 @@ The API indicates how developers can consume predictions for the following modal
 
 You can use streamlined inference clients in the language of your choice to consume predictions from models running the Azure AI model inference API.
 
+> [!IMPORTANT]
+> When working with the Azure AI model inference endpoint (preview), the base URL to connect to is of the form `https://<resource-name>.services.ai.azure.com/models`. Use this URL with the parameter `endpoint`. If using REST APIs, such is the base URL you have to append to the modality you want to consume. Read about [how to use the Azure AI model inference endpoint](../../ai-foundry/model-inference/how-to/inference.md).
+
 # [Python](#tab/python)
 
 Install the package `azure-ai-inference` using your package manager, like pip:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル推論APIに関するドキュメントの更新"
}
```

### Explanation
この変更は、Azure AIモデル推論APIに関するドキュメントの更新を反映しています。具体的には、いくつかの文の改善と追加情報の提供が行われています。

- 「Azure AI Model Inference APIが利用可能なモデル」に関する記述が更新され、「モデル/システム」へと用語が変更されました。
- 「Azure AI Servicesにおけるモデル推論」が新たに追加され、具体的なサポート対象モデルへのリンクが設けられました。
- 注意すべき点として、Azure AIモデル推論エンドポイントを使用する際の基本URL形式が記載され、REST APIの使用に関する情報も提供されています。

これにより、開発者がAPIを利用する際の理解が深まるよう、情報が整理されて強化されています。


