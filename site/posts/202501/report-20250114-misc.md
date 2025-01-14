---
date: '2025-01-14'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62
summary: この更新のハイライトは、Azure AI FoundryでのCodestralチャットモデルに関する新しいMarkdownファイルの追加です。このファイルには、モデルの概要や導入手順、APIクライアントの使用方法、コード例が含まれています。破壊的変更はなく、文書の表現修正や書式統一などの軽微な更新も行われました。特にAzure
  CLIコマンドの可読性が改善され、ドキュメントのナビゲーションが強化されています。全体として、これらの更新はAzureのAIサービスの利便性を向上させることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:70337bc...MicrosoftDocs:de17d62){target="_blank"}

# ハイライト

この更新でのハイライトは以下の通りです。

## 新機能

- Azure AI FoundryでのCodestralチャットモデルの使用方法に関する新しいMarkdownファイルの追加。このファイルは、モデルの概要や導入手順、APIクライアントの使用方法、コード例などを提供します。
  
## 破壊的変更

- なし

## その他の更新

- 文書インテリジェンスやプライベートリンク設定、Mistralモデルに関する文書の表現修正。
- W2モデルIDの表記が統一され、「prebuilt-tax.us.W-2」から「prebuilt-tax.us.w2」に変更。
- Azure CLIコマンドでのサブスクリプションプレースホルダー修正と可読性改善。
- CodestralモデルとMistralモデルに関する文書が更新され、ユーザーにより情報を把握しやすく。
- Mistralモデルの可用性に関する情報を整理。
- 目次にCodestralモデルの項目を追加。
- Azure AI Searchサービスでの価格ティアに関する推奨事項をチュートリアルに追加。

# インサイト

今回の更新は、いくつかの異なる技術領域にわたる軽微な改善と新機能の追加を含むものです。特に注目すべきは、Azure AI Foundryプラットフォームでの新しいCodestralチャットモデルの提供です。これは、ユーザーがコード生成タスクをより簡単に実行できるようにするもので、多様なプログラミング言語対応の支援を意図しています。

また、一連の変更は、技術文書の一貫性と可読性、そして実用性を向上させることを目的としており、表現や誤記の修正といった文書の品質向上に寄与しています。特に、Azure CLIコマンドの例では、使用頻度の高いコマンドの可読性を改善することによって、ユーザーがより理解しやすくなり、実行時の間違いを減少させる期待ができます。

さらに、ドキュメントの可用性や目次の整理を通じて、ユーザーが必要な情報に迅速にアクセスできる構造が形成されています。これはドキュメントにしっかりとしたナビゲーション軸を提供し、ユーザーエクスペリエンスを大幅に改善するものです。

全体として、これらの更新は、利用者がAzureのAIサービスをさらに効率的に使用できるようにサポートし、技術的労力を軽減することを目指したものです。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [overview.md](#item-4e36ba) | minor update | W2モデルIDの表記変更 | modified | 1 | 1 | 2 | 
| [tax-document.md](#item-e19fe5) | minor update | W2モデルIDの表記変更に関する更新 | modified | 3 | 3 | 6 | 
| [configure-private-link.md](#item-bbf93d) | minor update | プライベートリンク設定手順の修正 | modified | 8 | 4 | 12 | 
| [deploy-models-mistral-codestral.md](#item-83ba03) | new feature | Codestralチャットモデルの使用方法に関する新規記事 | added | 2067 | 0 | 2067 | 
| [deploy-models-mistral-nemo.md](#item-e7b729) | minor update | Mistral Nemoモデル使用に関するドキュメントの更新 | modified | 17 | 13 | 30 | 
| [deploy-models-mistral-open.md](#item-84e005) | minor update | Mistralオープンモデルに関するドキュメントの更新 | modified | 26 | 22 | 48 | 
| [deploy-models-mistral.md](#item-487a41) | minor update | Mistralプレミアムモデルに関するドキュメントの更新 | modified | 7 | 4 | 11 | 
| [model-catalog-overview.md](#item-278001) | minor update | Mistralモデルに関する文書の小規模更新 | modified | 1 | 1 | 2 | 
| [region-availability-maas.md](#item-35d79c) | minor update | モデルの可用性に関するドキュメントの更新 | modified | 5 | 4 | 9 | 
| [toc.yml](#item-2745cd) | minor update | 目次にCodestralモデルの項目を追加 | modified | 2 | 0 | 2 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | チュートリアルに価格ティアに関する推奨事項を追加 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/overview.md{#item-4e36ba}

<details>
<summary>Diff</summary>
````diff
@@ -471,7 +471,7 @@ You can use Document Intelligence to automate document processing in application
 
 | Model ID| Description |Automation use cases | Development options |
 |----------|--------------|-------------------------|-----------|
-|[**prebuilt-tax.us.W-2**](prebuilt/tax-document.md) |&#9679; Extract key information from IRS US W2 tax forms (year 2018-2021).</br>&#9679;|&#9679; Automated tax document management.</br>&#9679; Mortgage loan application processing. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.w2&formType=tax.us.w2)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model) |
+|[**prebuilt-tax.us.w2**](prebuilt/tax-document.md) |&#9679; Extract key information from IRS US W2 tax forms (year 2018-2021).</br>&#9679;|&#9679; Automated tax document management.</br>&#9679; Mortgage loan application processing. |&#9679; [**Document Intelligence Studio**](https://documentintelligence.ai.azure.com/studio/prebuilt?formCategory=tax.us.w2&formType=tax.us.w2)</br>&#9679; [**REST API**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true&pivots=programming-language-rest-api#analyze-document-post-request)</br>&#9679; [**C# SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Python SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**Java SDK**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model)</br>&#9679; [**JavaScript**](quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true#prebuilt-model) |
 
 > [!div class="nextstepaction"]
 > [Return to model types](#prebuilt-models)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "W2モデルIDの表記変更"
}
```

### Explanation
この変更は、文書インテリジェンスの概要に関するMarkdownファイル内で、W2モデルIDの表記を修正するもので、具体的には「prebuilt-tax.us.W-2」から「prebuilt-tax.us.w2」に変更されました。この変更により、整合性が保たれるとともに、W2文書に関連する情報がより明確に読者に伝わるようになります。改行やリンクはそのまま保持されており、内容の本質には影響を与えない軽微な更新です。

## articles/ai-services/document-intelligence/prebuilt/tax-document.md{#item-e19fe5}

<details>
<summary>Diff</summary>
````diff
@@ -57,7 +57,7 @@ Document Intelligence v4.0: **2024-11-30** (GA) supports the following tools, ap
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us</br>&bullet; prebuilt-tax.us.W-2</br>&bullet;  prebuilt-tax.us.W-4</br>&bullet;  prebuilt-tax.us.1095A</br>&bullet; prebuilt-tax.us.1095C</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T</br>&bullet; prebuilt-tax.us.1099A</br>&bullet; prebuilt-tax.us.1099B</br>&bullet; prebuilt-tax.us.1099C</br>&bullet; prebuilt-tax.us.1099CAP</br>&bullet; prebuilt-tax.us.1099Combo</br>&bullet; prebuilt-tax.us.1099DIV</br>&bullet; prebuilt-tax.us.1099G</br>&bullet; prebuilt-tax.us.1099H</br>&bullet; prebuilt-tax.us.1099INT</br>&bullet; prebuilt-tax.us.1099K</br>&bullet; prebuilt-tax.us.1099LS</br>&bullet; prebuilt-tax.us.1099LTC</br>&bullet; prebuilt-tax.us.1099MISC</br>&bullet; prebuilt-tax.us.1099NEC</br>&bullet; prebuilt-tax.us.1099OID</br>&bullet; prebuilt-tax.us.1099PATR</br>&bullet; prebuilt-tax.us.1099Q</br>&bullet; prebuilt-tax.us.1099QA</br>&bullet; prebuilt-tax.us.1099R</br>&bullet; prebuilt-tax.us.1099S</br>&bullet; prebuilt-tax.us.1099SA</br>&bullet; prebuilt-tax.us.1099SB</br>&bullet; prebuilt-tax.us.1099SSA</br>&bullet; prebuilt-tax.us.1040</br>&bullet; prebuilt-tax.us.1040Schedule1</br>&bullet; prebuilt-tax.us.1040Schedule2</br>&bullet; prebuilt-tax.us.1040Schedule3</br>&bullet; prebuilt-tax.us.1040Schedule8812</br>&bullet; prebuilt-tax.us.1040ScheduleA</br>&bullet; prebuilt-tax.us.1040ScheduleB</br>&bullet; prebuilt-tax.us.1040ScheduleC</br>&bullet; prebuilt-tax.us.1040ScheduleD</br>&bullet; prebuilt-tax.us.1040ScheduleE</br>&bullet; prebuilt-tax.us.1040ScheduleEIC</br>&bullet; prebuilt-tax.us.1040ScheduleF</br>&bullet; prebuilt-tax.us.1040ScheduleH</br>&bullet; prebuilt-tax.us.1040ScheduleJ</br>&bullet; prebuilt-tax.us.1040ScheduleR</br>&bullet; prebuilt-tax.us.1040ScheduleSE</br>&bullet; prebuilt-tax.us.1040Senior**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/operation-groups?view=rest-aiservices-v4.0%20(2024-11-30)&preserve-view=true)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-4.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us</br>&bullet; prebuilt-tax.us.w2</br>&bullet;  prebuilt-tax.us.W-4</br>&bullet;  prebuilt-tax.us.1095A</br>&bullet; prebuilt-tax.us.1095C</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T</br>&bullet; prebuilt-tax.us.1099A</br>&bullet; prebuilt-tax.us.1099B</br>&bullet; prebuilt-tax.us.1099C</br>&bullet; prebuilt-tax.us.1099CAP</br>&bullet; prebuilt-tax.us.1099Combo</br>&bullet; prebuilt-tax.us.1099DIV</br>&bullet; prebuilt-tax.us.1099G</br>&bullet; prebuilt-tax.us.1099H</br>&bullet; prebuilt-tax.us.1099INT</br>&bullet; prebuilt-tax.us.1099K</br>&bullet; prebuilt-tax.us.1099LS</br>&bullet; prebuilt-tax.us.1099LTC</br>&bullet; prebuilt-tax.us.1099MISC</br>&bullet; prebuilt-tax.us.1099NEC</br>&bullet; prebuilt-tax.us.1099OID</br>&bullet; prebuilt-tax.us.1099PATR</br>&bullet; prebuilt-tax.us.1099Q</br>&bullet; prebuilt-tax.us.1099QA</br>&bullet; prebuilt-tax.us.1099R</br>&bullet; prebuilt-tax.us.1099S</br>&bullet; prebuilt-tax.us.1099SA</br>&bullet; prebuilt-tax.us.1099SB</br>&bullet; prebuilt-tax.us.1099SSA</br>&bullet; prebuilt-tax.us.1040</br>&bullet; prebuilt-tax.us.1040Schedule1</br>&bullet; prebuilt-tax.us.1040Schedule2</br>&bullet; prebuilt-tax.us.1040Schedule3</br>&bullet; prebuilt-tax.us.1040Schedule8812</br>&bullet; prebuilt-tax.us.1040ScheduleA</br>&bullet; prebuilt-tax.us.1040ScheduleB</br>&bullet; prebuilt-tax.us.1040ScheduleC</br>&bullet; prebuilt-tax.us.1040ScheduleD</br>&bullet; prebuilt-tax.us.1040ScheduleE</br>&bullet; prebuilt-tax.us.1040ScheduleEIC</br>&bullet; prebuilt-tax.us.1040ScheduleF</br>&bullet; prebuilt-tax.us.1040ScheduleH</br>&bullet; prebuilt-tax.us.1040ScheduleJ</br>&bullet; prebuilt-tax.us.1040ScheduleR</br>&bullet; prebuilt-tax.us.1040ScheduleSE</br>&bullet; prebuilt-tax.us.1040Senior**|
 
 ::: moniker-end
 
@@ -67,7 +67,7 @@ Document Intelligence v3.1 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-2023-07-31&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.1.0&preserve-view=true)|**&bullet; prebuilt-tax.us.w2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.0.0"
@@ -76,7 +76,7 @@ Document Intelligence v3.0 supports the following tools, applications, and libra
 
 | Feature | Resources | Model ID |
 |----------|-------------|-----------|
-|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us.W-2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
+|**US tax form models**|&bullet; [**Document Intelligence Studio**](https://formrecognizer.appliedai.azure.com)</br>&bullet;  [**REST API**](/rest/api/aiservices/document-models/analyze-document?view=rest-aiservices-v3.0%20(2022-08-31)&preserve-view=true&tabs=HTTP)</br>&bullet;  [**C# SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Python SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**Java SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)</br>&bullet;  [**JavaScript SDK**](../quickstarts/get-started-sdks-rest-api.md?view=doc-intel-3.0.0&preserve-view=true)|**&bullet; prebuilt-tax.us.w2</br>&bullet; prebuilt-tax.us.1098</br>&bullet; prebuilt-tax.us.1098E</br>&bullet; prebuilt-tax.us.1098T**|
 ::: moniker-end
 
 ## Input requirements
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "W2モデルIDの表記変更に関する更新"
}
```

### Explanation
このコードの変更は、税務ドキュメントに関連するMarkdownファイルにおいて、モデルIDの表記を修正することを目的としています。具体的には、表内の「prebuilt-tax.us.W-2」を「prebuilt-tax.us.w2」と修正し、表記の統一を図っています。また、他のモデルIDにも同様の修正を加えて、整合性を保つことが目的です。この修正により、他の関連情報との整合性が向上し、ドキュメントがより明確になります。全体として、内容には大きな影響を与えない軽微な更新が行われています。

## articles/ai-studio/how-to/configure-private-link.md{#item-bbf93d}

<details>
<summary>Diff</summary>
````diff
@@ -55,9 +55,11 @@ az network private-endpoint create \
     --name <private-endpoint-name> \
     --vnet-name <vnet-name> \
     --subnet <subnet-name> \
-    --private-connection-resource-id "/subscriptions/<subscription>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>" \
+    --private-connection-resource-id "/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>" \
     --group-id amlworkspace \
-    --connection-name workspace -l <location>
+    --connection-name workspace \
+    --location <location> \
+    --resource-group <resource-group-name>
 ```
 
 To create the private DNS zone entries for the workspace, use the following commands:
@@ -127,9 +129,11 @@ az network private-endpoint create \
     --name <private-endpoint-name> \
     --vnet-name <vnet-name> \
     --subnet <subnet-name> \
-    --private-connection-resource-id "/subscriptions/<subscription>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>" \
+    --private-connection-resource-id "/subscriptions/<subscription-id>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>" \
     --group-id amlworkspace \
-    --connection-name workspace -l <location>
+    --connection-name workspace \
+    --location <location> \
+    --resource-group <resource-group-name>
 ```
 
 To create the private DNS zone entries for the workspace, use the following commands:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プライベートリンク設定手順の修正"
}
```

### Explanation
この変更では、プライベートリンクの設定手順に関するMarkdownファイルが更新されています。具体的には、Azure CLIコマンドのパラメータの一部が修正・追加されています。特に、「--private-connection-resource-id」で使用されるサブスクリプションのプレースホルダーが「<subscription>」から「<subscription-id>」に変更されたのが主なポイントです。また、「--location」の指定方法が改善され、「--resource-group」のオプションが新たに追加され、コマンドの可読性と明確性が向上しています。この修正により、ユーザーがプライベートリンク設定を行う際の手順がより正確で分かりやすくなります。全体として、軽微な更新が行われています。

## articles/ai-studio/how-to/deploy-models-mistral-codestral.md{#item-83ba03}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,2067 @@
+---
+title: How to use Codestral chat model with Azure AI Foundry
+titleSuffix: Azure AI Foundry
+description: Learn how to use Codestral chat model with Azure AI Foundry.
+ms.service: azure-ai-studio
+manager: scottpolly
+ms.topic: how-to
+ms.date: 01/08/2025
+ms.reviewer: kritifaujdar
+reviewer: fkriti
+ms.author: mopeakande
+author: msakande
+ms.custom: references_regions, generated
+zone_pivot_groups: azure-ai-model-catalog-samples-chat
+---
+
+# How to use Codestral chat model
+
+[!INCLUDE [feature-preview](../includes/feature-preview.md)]
+
+In this article, you learn about Codestral chat model and how to use it.
+Mistral AI offers two categories of models, namely:
+
+- _Premium models_: These include [Mistral Large, Mistral Small, and Ministral 3B](deploy-models-mistral.md) models, and are available as serverless APIs with pay-as-you-go token-based billing.  
+- _Open models_: These include Codestral and [Mistral Nemo](deploy-models-mistral-nemo.md) (that are available as serverless APIs with pay-as-you-go token-based billing), and [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md)(that are available to download and run on self-hosted managed endpoints).
+
+[!INCLUDE [models-preview](../includes/models-preview.md)]
+
+
+
+::: zone pivot="programming-language-python"
+
+## Codestral chat model
+
+Codestral 2501 is explicitly designed for code generation tasks. It helps developers write and interact with code through a shared instruction and completion API endpoint. As Codestral 2501 can master code and also converse in various languages, it's also useful for designing advanced AI applications for software developers.
+
+Codestral 2501 is fluent in more than 80 programming languages including Python, Java, C, C++, JavaScript, and Bash. It also performs well on more specific ones like Swift and Fortran.
+The model improves developers productivity and reduces errors as it can complete coding functions, write tests, and complete any partial code using a fill-in-the-middle mechanism.
+
+
+Codestral 2501 supports a context length of 256K, and it accepts only text inputs and generates text outputs.
+
+Use-cases for Codestral 2501 include:
+
+- _Code generation_: code completion, suggestions, and translation
+- _Code understanding and documentation_: code summarization and explanation
+- _Code quality_: code review, refactoring, bug fixing, and test case generation
+- _Code generation with fill-in-the-middle (FIM) completion_: users can define the starting point of the code using a prompt, and the ending point of the code using an optional suffix and an optional stop. The Codestral model then generates the code that fits in-between, making it ideal for tasks that require a specific piece of code to be generated.
+
+
+You can learn more about the models in their respective model card:
+
+* [Codestral-2501](https://aka.ms/aistudio/landing/mistral-codestral-2501)
+
+
+> [!TIP]
+> Additionally, MistralAI supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [MistralAI documentation](https://docs.mistral.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Codestral chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Codestral chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `azure-ai-inference` package with Python. To install this package, you need the following prerequisites:
+
+* Python 3.8 or later installed, including pip.
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+  
+Once you have these prerequisites, install the Azure AI inference package with the following command:
+
+```bash
+pip install azure-ai-inference
+```
+
+Read more about the [Azure AI inference package and reference](https://aka.ms/azsdk/azure-ai-inference/python/reference).
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Codestral chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```python
+import os
+from azure.ai.inference import ChatCompletionsClient
+from azure.core.credentials import AzureKeyCredential
+
+client = ChatCompletionsClient(
+    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
+    credential=AzureKeyCredential(os.environ["AZURE_INFERENCE_CREDENTIAL"]),
+)
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```python
+model_info = client.get_model_info()
+```
+
+The response is as follows:
+
+
+```python
+print("Model name:", model_info.model_name)
+print("Model type:", model_info.model_type)
+print("Model provider name:", model_info.model_provider_name)
+```
+
+```console
+Model name: Codestral-2501
+Model type: chat-completions
+Model provider name: MistralAI
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```python
+from azure.ai.inference.models import SystemMessage, UserMessage
+
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+)
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```python
+print("Response:", response.choices[0].message.content)
+print("Model:", response.model)
+print("Usage:")
+print("\tPrompt tokens:", response.usage.prompt_tokens)
+print("\tTotal tokens:", response.usage.total_tokens)
+print("\tCompletion tokens:", response.usage.completion_tokens)
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: Codestral-2501
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```python
+result = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    temperature=0,
+    top_p=1,
+    max_tokens=2048,
+    stream=True,
+)
+```
+
+To stream completions, set `stream=True` when you call the model.
+
+To visualize the output, define a helper function to print the stream.
+
+```python
+def print_stream(result):
+    """
+    Prints the chat completion with streaming.
+    """
+    import time
+    for update in result:
+        if update.choices:
+            print(update.choices[0].delta.content, end="")
+```
+
+You can visualize how streaming generates content:
+
+
+```python
+print_stream(result)
+```
+
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatText
+
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    presence_penalty=0.1,
+    frequency_penalty=0.8,
+    max_tokens=2048,
+    stop=["<|endoftext|>"],
+    temperature=0,
+    top_p=1,
+    response_format={ "type": ChatCompletionsResponseFormatText() },
+)
+```
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+#### Create JSON outputs
+
+Codestral chat model can create JSON outputs. Set `response_format` to `json_object` to enable JSON mode and guarantee that the message the model generates is valid JSON. You must also instruct the model to produce JSON yourself via a system or user message. Also, the message content might be partially cut off if `finish_reason="length"`, which indicates that the generation exceeded `max_tokens` or that the conversation exceeded the max context length.
+
+
+```python
+from azure.ai.inference.models import ChatCompletionsResponseFormatJSON
+
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant that always generate responses in JSON format, using."
+                      " the following format: { ""answer"": ""response"" }."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    response_format={ "type": ChatCompletionsResponseFormatJSON() }
+)
+```
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```python
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    model_extras={
+        "logprobs": True
+    }
+)
+```
+
+The following extra parameters can be passed to Codestral chat model:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `ignore_eos` | Whether to ignore the EOS token and continue generating tokens after the EOS token is generated. | `boolean` |
+| `safe_mode` | Whether to inject a safety prompt before all conversations. | `boolean` |
+
+
+### Safe mode
+
+Codestral chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+
+> Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
+
+The Azure AI Model Inference API allows you to pass this extra parameter as follows:
+
+
+```python
+response = client.complete(
+    messages=[
+        SystemMessage(content="You are a helpful assistant."),
+        UserMessage(content="How many languages are in the world?"),
+    ],
+    model_extras={
+        "safe_mode": True
+    }
+)
+```
+
+### Use tools
+
+Codestral chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+
+The following code example creates a tool definition that is able to look from flight information from two different cities.
+
+
+```python
+from azure.ai.inference.models import FunctionDefinition, ChatCompletionsFunctionToolDefinition
+
+flight_info = ChatCompletionsFunctionToolDefinition(
+    function=FunctionDefinition(
+        name="get_flight_info",
+        description="Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+        parameters={
+            "type": "object",
+            "properties": {
+                "origin_city": {
+                    "type": "string",
+                    "description": "The name of the city where the flight originates",
+                },
+                "destination_city": {
+                    "type": "string",
+                    "description": "The flight destination city",
+                },
+            },
+            "required": ["origin_city", "destination_city"],
+        },
+    )
+)
+
+tools = [flight_info]
+```
+
+In this example, the function's output is that there are no flights available for the selected route, but the user should consider taking a train.
+
+
+```python
+def get_flight_info(loc_origin: str, loc_destination: str):
+    return { 
+        "info": f"There are no flights available from {loc_origin} to {loc_destination}. You should take a train, specially if it helps to reduce CO2 emissions."
+    }
+```
+
+Prompt the model to book flights with the help of this function:
+
+
+```python
+messages = [
+    SystemMessage(
+        content="You are a helpful assistant that help users to find information about traveling, how to get"
+                " to places and the different transportations options. You care about the environment and you"
+                " always have that in mind when answering inqueries.",
+    ),
+    UserMessage(
+        content="When is the next flight from Miami to Seattle?",
+    ),
+]
+
+response = client.complete(
+    messages=messages, tools=tools, tool_choice="auto"
+)
+```
+
+You can inspect the response to find out if a tool needs to be called. Inspect the finish reason to determine if the tool should be called. Remember that multiple tool types can be indicated. This example demonstrates a tool of type `function`.
+
+
+```python
+response_message = response.choices[0].message
+tool_calls = response_message.tool_calls
+
+print("Finish reason:", response.choices[0].finish_reason)
+print("Tool call:", tool_calls)
+```
+
+To continue, append this message to the chat history:
+
+
+```python
+messages.append(
+    response_message
+)
+```
+
+Now, it's time to call the appropriate function to handle the tool call. The following code snippet iterates over all the tool calls indicated in the response and calls the corresponding function with the appropriate parameters. The response is also appended to the chat history.
+
+
+```python
+import json
+from azure.ai.inference.models import ToolMessage
+
+for tool_call in tool_calls:
+
+    # Get the tool details:
+
+    function_name = tool_call.function.name
+    function_args = json.loads(tool_call.function.arguments.replace("\'", "\""))
+    tool_call_id = tool_call.id
+
+    print(f"Calling function `{function_name}` with arguments {function_args}")
+
+    # Call the function defined above using `locals()`, which returns the list of all functions 
+    # available in the scope as a dictionary. Notice that this is just done as a simple way to get
+    # the function callable from its string name. Then we can call it with the corresponding
+    # arguments.
+
+    callable_func = locals()[function_name]
+    function_response = callable_func(**function_args)
+
+    print("->", function_response)
+
+    # Once we have a response from the function and its arguments, we can append a new message to the chat 
+    # history. Notice how we are telling to the model that this chat message came from a tool:
+
+    messages.append(
+        ToolMessage(
+            tool_call_id=tool_call_id,
+            content=json.dumps(function_response)
+        )
+    )
+```
+
+View the response from the model:
+
+
+```python
+response = client.complete(
+    messages=messages,
+    tools=tools,
+)
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```python
+from azure.ai.inference.models import AssistantMessage, UserMessage, SystemMessage
+
+try:
+    response = client.complete(
+        messages=[
+            SystemMessage(content="You are an AI assistant that helps people find information."),
+            UserMessage(content="Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."),
+        ]
+    )
+
+    print(response.choices[0].message.content)
+
+except HttpResponseError as ex:
+    if ex.status_code == 400:
+        response = ex.response.json()
+        if isinstance(response, dict) and "error" in response:
+            print(f"Your request triggered an {response['error']['code']} error:\n\t {response['error']['message']}")
+        else:
+            raise
+    raise
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-javascript"
+
+## Codestral chat model
+
+Codestral 2501 is explicitly designed for code generation tasks. It helps developers write and interact with code through a shared instruction and completion API endpoint. As Codestral 2501 can master code and also converse in various languages, it's also useful for designing advanced AI applications for software developers.
+
+Codestral 2501 is fluent in more than 80 programming languages including Python, Java, C, C++, JavaScript, and Bash. It also performs well on more specific ones like Swift and Fortran.
+The model improves developers productivity and reduces errors as it can complete coding functions, write tests, and complete any partial code using a fill-in-the-middle mechanism.
+
+
+Codestral 2501 supports a context length of 256K, and it accepts only text inputs and generates text outputs.
+
+Use-cases for Codestral 2501 include:
+
+- _Code generation_: code completion, suggestions, and translation
+- _Code understanding and documentation_: code summarization and explanation
+- _Code quality_: code review, refactoring, bug fixing, and test case generation
+- _Code generation with fill-in-the-middle (FIM) completion_: users can define the starting point of the code using a prompt, and the ending point of the code using an optional suffix and an optional stop. The Codestral model then generates the code that fits in-between, making it ideal for tasks that require a specific piece of code to be generated.
+
+
+You can learn more about the models in their respective model card:
+
+* [Codestral-2501](https://aka.ms/aistudio/landing/mistral-codestral-2501)
+
+
+> [!TIP]
+> Additionally, MistralAI supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [MistralAI documentation](https://docs.mistral.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Codestral chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Codestral chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `@azure-rest/ai-inference` package from `npm`. To install this package, you need the following prerequisites:
+
+* LTS versions of `Node.js` with `npm`.
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+Once you have these prerequisites, install the Azure Inference library for JavaScript with the following command:
+
+```bash
+npm install @azure-rest/ai-inference
+```
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Codestral chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```javascript
+import ModelClient from "@azure-rest/ai-inference";
+import { isUnexpected } from "@azure-rest/ai-inference";
+import { AzureKeyCredential } from "@azure/core-auth";
+
+const client = new ModelClient(
+    process.env.AZURE_INFERENCE_ENDPOINT, 
+    new AzureKeyCredential(process.env.AZURE_INFERENCE_CREDENTIAL)
+);
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```javascript
+var model_info = await client.path("/info").get()
+```
+
+The response is as follows:
+
+
+```javascript
+console.log("Model name: ", model_info.body.model_name)
+console.log("Model type: ", model_info.body.model_type)
+console.log("Model provider name: ", model_info.body.model_provider_name)
+```
+
+```console
+Model name: Codestral-2501
+Model type: chat-completions
+Model provider name: MistralAI
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+    }
+});
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```javascript
+if (isUnexpected(response)) {
+    throw response.body.error;
+}
+
+console.log("Response: ", response.body.choices[0].message.content);
+console.log("Model: ", response.body.model);
+console.log("Usage:");
+console.log("\tPrompt tokens:", response.body.usage.prompt_tokens);
+console.log("\tTotal tokens:", response.body.usage.total_tokens);
+console.log("\tCompletion tokens:", response.body.usage.completion_tokens);
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: Codestral-2501
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+    }
+}).asNodeStream();
+```
+
+To stream completions, use `.asNodeStream()` when you call the model.
+
+You can visualize how streaming generates content:
+
+
+```javascript
+var stream = response.body;
+if (!stream) {
+    stream.destroy();
+    throw new Error(`Failed to get chat completions with status: ${response.status}`);
+}
+
+if (response.status !== "200") {
+    throw new Error(`Failed to get chat completions: ${response.body.error}`);
+}
+
+var sses = createSseStream(stream);
+
+for await (const event of sses) {
+    if (event.data === "[DONE]") {
+        return;
+    }
+    for (const choice of (JSON.parse(event.data)).choices) {
+        console.log(choice.delta?.content ?? "");
+    }
+}
+```
+
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+        presence_penalty: "0.1",
+        frequency_penalty: "0.8",
+        max_tokens: 2048,
+        stop: ["<|endoftext|>"],
+        temperature: 0,
+        top_p: 1,
+        response_format: { type: "text" },
+    }
+});
+```
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+#### Create JSON outputs
+
+Codestral chat model can create JSON outputs. Set `response_format` to `json_object` to enable JSON mode and guarantee that the message the model generates is valid JSON. You must also instruct the model to produce JSON yourself via a system or user message. Also, the message content might be partially cut off if `finish_reason="length"`, which indicates that the generation exceeded `max_tokens` or that the conversation exceeded the max context length.
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant that always generate responses in JSON format, using."
+        + " the following format: { \"answer\": \"response\" }." },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+        response_format: { type: "json_object" }
+    }
+});
+```
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    headers: {
+        "extra-params": "pass-through"
+    },
+    body: {
+        messages: messages,
+        logprobs: true
+    }
+});
+```
+
+The following extra parameters can be passed to Codestral chat model:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `ignore_eos` | Whether to ignore the EOS token and continue generating tokens after the EOS token is generated. | `boolean` |
+| `safe_mode` | Whether to inject a safety prompt before all conversations. | `boolean` |
+
+
+### Safe mode
+
+Codestral chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+
+> Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
+
+The Azure AI Model Inference API allows you to pass this extra parameter as follows:
+
+
+```javascript
+var messages = [
+    { role: "system", content: "You are a helpful assistant" },
+    { role: "user", content: "How many languages are in the world?" },
+];
+
+var response = await client.path("/chat/completions").post({
+    headers: {
+        "extra-params": "pass-through"
+    },
+    body: {
+        messages: messages,
+        safe_mode: true
+    }
+});
+```
+
+### Use tools
+
+Codestral chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+
+The following code example creates a tool definition that is able to look from flight information from two different cities.
+
+
+```javascript
+const flight_info = {
+    name: "get_flight_info",
+    description: "Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+    parameters: {
+        type: "object",
+        properties: {
+            origin_city: {
+                type: "string",
+                description: "The name of the city where the flight originates",
+            },
+            destination_city: {
+                type: "string",
+                description: "The flight destination city",
+            },
+        },
+        required: ["origin_city", "destination_city"],
+    },
+}
+
+const tools = [
+    {
+        type: "function",
+        function: flight_info,
+    },
+];
+```
+
+In this example, the function's output is that there are no flights available for the selected route, but the user should consider taking a train.
+
+
+```javascript
+function get_flight_info(loc_origin, loc_destination) {
+    return {
+        info: "There are no flights available from " + loc_origin + " to " + loc_destination + ". You should take a train, specially if it helps to reduce CO2 emissions."
+    }
+}
+```
+
+Prompt the model to book flights with the help of this function:
+
+
+```javascript
+var result = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+        tools: tools,
+        tool_choice: "auto"
+    }
+});
+```
+
+You can inspect the response to find out if a tool needs to be called. Inspect the finish reason to determine if the tool should be called. Remember that multiple tool types can be indicated. This example demonstrates a tool of type `function`.
+
+
+```javascript
+const response_message = response.body.choices[0].message;
+const tool_calls = response_message.tool_calls;
+
+console.log("Finish reason: " + response.body.choices[0].finish_reason);
+console.log("Tool call: " + tool_calls);
+```
+
+To continue, append this message to the chat history:
+
+
+```javascript
+messages.push(response_message);
+```
+
+Now, it's time to call the appropriate function to handle the tool call. The following code snippet iterates over all the tool calls indicated in the response and calls the corresponding function with the appropriate parameters. The response is also appended to the chat history.
+
+
+```javascript
+function applyToolCall({ function: call, id }) {
+    // Get the tool details:
+    const tool_params = JSON.parse(call.arguments);
+    console.log("Calling function " + call.name + " with arguments " + tool_params);
+
+    // Call the function defined above using `window`, which returns the list of all functions 
+    // available in the scope as a dictionary. Notice that this is just done as a simple way to get
+    // the function callable from its string name. Then we can call it with the corresponding
+    // arguments.
+    const function_response = tool_params.map(window[call.name]);
+    console.log("-> " + function_response);
+
+    return function_response
+}
+
+for (const tool_call of tool_calls) {
+    var tool_response = tool_call.apply(applyToolCall);
+
+    messages.push(
+        {
+            role: "tool",
+            tool_call_id: tool_call.id,
+            content: tool_response
+        }
+    );
+}
+```
+
+View the response from the model:
+
+
+```javascript
+var result = await client.path("/chat/completions").post({
+    body: {
+        messages: messages,
+        tools: tools,
+    }
+});
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```javascript
+try {
+    var messages = [
+        { role: "system", content: "You are an AI assistant that helps people find information." },
+        { role: "user", content: "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills." },
+    ];
+
+    var response = await client.path("/chat/completions").post({
+        body: {
+            messages: messages,
+        }
+    });
+
+    console.log(response.body.choices[0].message.content);
+}
+catch (error) {
+    if (error.status_code == 400) {
+        var response = JSON.parse(error.response._content);
+        if (response.error) {
+            console.log(`Your request triggered an ${response.error.code} error:\n\t ${response.error.message}`);
+        }
+        else
+        {
+            throw error;
+        }
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-csharp"
+
+## Codestral chat model
+
+Codestral 2501 is explicitly designed for code generation tasks. It helps developers write and interact with code through a shared instruction and completion API endpoint. As Codestral 2501 can master code and also converse in various languages, it's also useful for designing advanced AI applications for software developers.
+
+Codestral 2501 is fluent in more than 80 programming languages including Python, Java, C, C++, JavaScript, and Bash. It also performs well on more specific ones like Swift and Fortran.
+The model improves developers productivity and reduces errors as it can complete coding functions, write tests, and complete any partial code using a fill-in-the-middle mechanism.
+
+
+Codestral 2501 supports a context length of 256K, and it accepts only text inputs and generates text outputs.
+
+Use-cases for Codestral 2501 include:
+
+- _Code generation_: code completion, suggestions, and translation
+- _Code understanding and documentation_: code summarization and explanation
+- _Code quality_: code review, refactoring, bug fixing, and test case generation
+- _Code generation with fill-in-the-middle (FIM) completion_: users can define the starting point of the code using a prompt, and the ending point of the code using an optional suffix and an optional stop. The Codestral model then generates the code that fits in-between, making it ideal for tasks that require a specific piece of code to be generated.
+
+
+You can learn more about the models in their respective model card:
+
+* [Codestral-2501](https://aka.ms/aistudio/landing/mistral-codestral-2501)
+
+
+> [!TIP]
+> Additionally, MistralAI supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [MistralAI documentation](https://docs.mistral.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Codestral chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Codestral chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### The inference package installed
+
+You can consume predictions from this model by using the `Azure.AI.Inference` package from [NuGet](https://www.nuget.org/). To install this package, you need the following prerequisites:
+
+* The endpoint URL. To construct the client library, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name` is your unique model deployment host name and `your-azure-region` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+Once you have these prerequisites, install the Azure AI inference library with the following command:
+
+```dotnetcli
+dotnet add package Azure.AI.Inference --prerelease
+```
+
+You can also authenticate with Microsoft Entra ID (formerly Azure Active Directory). To use credential providers provided with the Azure SDK, install the `Azure.Identity` package:
+
+```dotnetcli
+dotnet add package Azure.Identity
+```
+
+Import the following namespaces:
+
+
+```csharp
+using Azure;
+using Azure.Identity;
+using Azure.AI.Inference;
+```
+
+This example also uses the following namespaces but you may not always need them:
+
+
+```csharp
+using System.Text.Json;
+using System.Text.Json.Serialization;
+using System.Reflection;
+```
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Codestral chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+
+```csharp
+ChatCompletionsClient client = new ChatCompletionsClient(
+    new Uri(Environment.GetEnvironmentVariable("AZURE_INFERENCE_ENDPOINT")),
+    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_INFERENCE_CREDENTIAL"))
+);
+```
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+
+```csharp
+Response<ModelInfo> modelInfo = client.GetModelInfo();
+```
+
+The response is as follows:
+
+
+```csharp
+Console.WriteLine($"Model name: {modelInfo.Value.ModelName}");
+Console.WriteLine($"Model type: {modelInfo.Value.ModelType}");
+Console.WriteLine($"Model provider name: {modelInfo.Value.ModelProviderName}");
+```
+
+```console
+Model name: Codestral-2501
+Model type: chat-completions
+Model provider name: MistralAI
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```csharp
+ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+};
+
+Response<ChatCompletions> response = client.Complete(requestOptions);
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```csharp
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+Console.WriteLine($"Model: {response.Value.Model}");
+Console.WriteLine("Usage:");
+Console.WriteLine($"\tPrompt tokens: {response.Value.Usage.PromptTokens}");
+Console.WriteLine($"\tTotal tokens: {response.Value.Usage.TotalTokens}");
+Console.WriteLine($"\tCompletion tokens: {response.Value.Usage.CompletionTokens}");
+```
+
+```console
+Response: As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.
+Model: Codestral-2501
+Usage: 
+  Prompt tokens: 19
+  Total tokens: 91
+  Completion tokens: 72
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```csharp
+static async Task StreamMessageAsync(ChatCompletionsClient client)
+{
+    ChatCompletionsOptions requestOptions = new ChatCompletionsOptions()
+    {
+        Messages = {
+            new ChatRequestSystemMessage("You are a helpful assistant."),
+            new ChatRequestUserMessage("How many languages are in the world? Write an essay about it.")
+        },
+        MaxTokens=4096
+    };
+
+    StreamingResponse<StreamingChatCompletionsUpdate> streamResponse = await client.CompleteStreamingAsync(requestOptions);
+
+    await PrintStream(streamResponse);
+}
+```
+
+To stream completions, use `CompleteStreamingAsync` method when you call the model. Notice that in this example we the call is wrapped in an asynchronous method.
+
+To visualize the output, define an asynchronous method to print the stream in the console.
+
+```csharp
+static async Task PrintStream(StreamingResponse<StreamingChatCompletionsUpdate> response)
+{
+    await foreach (StreamingChatCompletionsUpdate chatUpdate in response)
+    {
+        if (chatUpdate.Role.HasValue)
+        {
+            Console.Write($"{chatUpdate.Role.Value.ToString().ToUpperInvariant()}: ");
+        }
+        if (!string.IsNullOrEmpty(chatUpdate.ContentUpdate))
+        {
+            Console.Write(chatUpdate.ContentUpdate);
+        }
+    }
+}
+```
+
+You can visualize how streaming generates content:
+
+
+```csharp
+StreamMessageAsync(client).GetAwaiter().GetResult();
+```
+
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+    PresencePenalty = 0.1f,
+    FrequencyPenalty = 0.8f,
+    MaxTokens = 2048,
+    StopSequences = { "<|endoftext|>" },
+    Temperature = 0,
+    NucleusSamplingFactor = 1,
+    ResponseFormat = new ChatCompletionsResponseFormatText()
+};
+
+response = client.Complete(requestOptions);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+#### Create JSON outputs
+
+Codestral chat model can create JSON outputs. Set `response_format` to `json_object` to enable JSON mode and guarantee that the message the model generates is valid JSON. You must also instruct the model to produce JSON yourself via a system or user message. Also, the message content might be partially cut off if `finish_reason="length"`, which indicates that the generation exceeded `max_tokens` or that the conversation exceeded the max context length.
+
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage(
+            "You are a helpful assistant that always generate responses in JSON format, " +
+            "using. the following format: { \"answer\": \"response\" }."
+        ),
+        new ChatRequestUserMessage(
+            "How many languages are in the world?"
+        )
+    },
+    ResponseFormat = new ChatCompletionsResponseFormatJSON()
+};
+
+response = client.Complete(requestOptions);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+    AdditionalProperties = { { "logprobs", BinaryData.FromString("true") } },
+};
+
+response = client.Complete(requestOptions, extraParams: ExtraParameters.PassThrough);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+The following extra parameters can be passed to Codestral chat model:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `ignore_eos` | Whether to ignore the EOS token and continue generating tokens after the EOS token is generated. | `boolean` |
+| `safe_mode` | Whether to inject a safety prompt before all conversations. | `boolean` |
+
+
+### Safe mode
+
+Codestral chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+
+> Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
+
+The Azure AI Model Inference API allows you to pass this extra parameter as follows:
+
+
+```csharp
+requestOptions = new ChatCompletionsOptions()
+{
+    Messages = {
+        new ChatRequestSystemMessage("You are a helpful assistant."),
+        new ChatRequestUserMessage("How many languages are in the world?")
+    },
+    AdditionalProperties = { { "safe_mode", BinaryData.FromString("true") } },
+};
+
+response = client.Complete(requestOptions, extraParams: ExtraParameters.PassThrough);
+Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
+```
+
+### Use tools
+
+Codestral chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+
+The following code example creates a tool definition that is able to look from flight information from two different cities.
+
+
+```csharp
+FunctionDefinition flightInfoFunction = new FunctionDefinition("getFlightInfo")
+{
+    Description = "Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+    Parameters = BinaryData.FromObjectAsJson(new
+    {
+        Type = "object",
+        Properties = new
+        {
+            origin_city = new
+            {
+                Type = "string",
+                Description = "The name of the city where the flight originates"
+            },
+            destination_city = new
+            {
+                Type = "string",
+                Description = "The flight destination city"
+            }
+        }
+    },
+        new JsonSerializerOptions() { PropertyNamingPolicy = JsonNamingPolicy.CamelCase }
+    )
+};
+
+ChatCompletionsFunctionToolDefinition getFlightTool = new ChatCompletionsFunctionToolDefinition(flightInfoFunction);
+```
+
+In this example, the function's output is that there are no flights available for the selected route, but the user should consider taking a train.
+
+
+```csharp
+static string getFlightInfo(string loc_origin, string loc_destination)
+{
+    return JsonSerializer.Serialize(new
+    {
+        info = $"There are no flights available from {loc_origin} to {loc_destination}. You " +
+        "should take a train, specially if it helps to reduce CO2 emissions."
+    });
+}
+```
+
+Prompt the model to book flights with the help of this function:
+
+
+```csharp
+var chatHistory = new List<ChatRequestMessage>(){
+        new ChatRequestSystemMessage(
+            "You are a helpful assistant that help users to find information about traveling, " +
+            "how to get to places and the different transportations options. You care about the" +
+            "environment and you always have that in mind when answering inqueries."
+        ),
+        new ChatRequestUserMessage("When is the next flight from Miami to Seattle?")
+    };
+
+requestOptions = new ChatCompletionsOptions(chatHistory);
+requestOptions.Tools.Add(getFlightTool);
+requestOptions.ToolChoice = ChatCompletionsToolChoice.Auto;
+
+response = client.Complete(requestOptions);
+```
+
+You can inspect the response to find out if a tool needs to be called. Inspect the finish reason to determine if the tool should be called. Remember that multiple tool types can be indicated. This example demonstrates a tool of type `function`.
+
+
+```csharp
+var responseMenssage = response.Value.Choices[0].Message;
+var toolsCall = responseMenssage.ToolCalls;
+
+Console.WriteLine($"Finish reason: {response.Value.Choices[0].FinishReason}");
+Console.WriteLine($"Tool call: {toolsCall[0].Id}");
+```
+
+To continue, append this message to the chat history:
+
+
+```csharp
+requestOptions.Messages.Add(new ChatRequestAssistantMessage(response.Value.Choices[0].Message));
+```
+
+Now, it's time to call the appropriate function to handle the tool call. The following code snippet iterates over all the tool calls indicated in the response and calls the corresponding function with the appropriate parameters. The response is also appended to the chat history.
+
+
+```csharp
+foreach (ChatCompletionsToolCall tool in toolsCall)
+{
+    if (tool is ChatCompletionsFunctionToolCall functionTool)
+    {
+        // Get the tool details:
+        string callId = functionTool.Id;
+        string toolName = functionTool.Name;
+        string toolArgumentsString = functionTool.Arguments;
+        Dictionary<string, object> toolArguments = JsonSerializer.Deserialize<Dictionary<string, object>>(toolArgumentsString);
+
+        // Here you have to call the function defined. In this particular example we use 
+        // reflection to find the method we definied before in an static class called 
+        // `ChatCompletionsExamples`. Using reflection allows us to call a function 
+        // by string name. Notice that this is just done for demonstration purposes as a 
+        // simple way to get the function callable from its string name. Then we can call 
+        // it with the corresponding arguments.
+
+        var flags = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static;
+        string toolResponse = (string)typeof(ChatCompletionsExamples).GetMethod(toolName, flags).Invoke(null, toolArguments.Values.Cast<object>().ToArray());
+
+        Console.WriteLine("->", toolResponse);
+        requestOptions.Messages.Add(new ChatRequestToolMessage(toolResponse, callId));
+    }
+    else
+        throw new Exception("Unsupported tool type");
+}
+```
+
+View the response from the model:
+
+
+```csharp
+response = client.Complete(requestOptions);
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```csharp
+try
+{
+    requestOptions = new ChatCompletionsOptions()
+    {
+        Messages = {
+            new ChatRequestSystemMessage("You are an AI assistant that helps people find information."),
+            new ChatRequestUserMessage(
+                "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
+            ),
+        },
+    };
+
+    response = client.Complete(requestOptions);
+    Console.WriteLine(response.Value.Choices[0].Message.Content);
+}
+catch (RequestFailedException ex)
+{
+    if (ex.ErrorCode == "content_filter")
+    {
+        Console.WriteLine($"Your query has trigger Azure Content Safety: {ex.Message}");
+    }
+    else
+    {
+        throw;
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+
+::: zone pivot="programming-language-rest"
+
+## Codestral chat model
+
+Codestral 2501 is explicitly designed for code generation tasks. It helps developers write and interact with code through a shared instruction and completion API endpoint. As Codestral 2501 can master code and also converse in various languages, it's also useful for designing advanced AI applications for software developers.
+
+Codestral 2501 is fluent in more than 80 programming languages including Python, Java, C, C++, JavaScript, and Bash. It also performs well on more specific ones like Swift and Fortran.
+The model improves developers productivity and reduces errors as it can complete coding functions, write tests, and complete any partial code using a fill-in-the-middle mechanism.
+
+
+Codestral 2501 supports a context length of 256K, and it accepts only text inputs and generates text outputs.
+
+Use-cases for Codestral 2501 include:
+
+- _Code generation_: code completion, suggestions, and translation
+- _Code understanding and documentation_: code summarization and explanation
+- _Code quality_: code review, refactoring, bug fixing, and test case generation
+- _Code generation with fill-in-the-middle (FIM) completion_: users can define the starting point of the code using a prompt, and the ending point of the code using an optional suffix and an optional stop. The Codestral model then generates the code that fits in-between, making it ideal for tasks that require a specific piece of code to be generated.
+
+
+You can learn more about the models in their respective model card:
+
+* [Codestral-2501](https://aka.ms/aistudio/landing/mistral-codestral-2501)
+
+
+> [!TIP]
+> Additionally, MistralAI supports the use of a tailored API for use with specific features of the model. To use the model-provider specific API, check [MistralAI documentation](https://docs.mistral.ai/) or see the [inference examples](#more-inference-examples) section to code examples.
+
+## Prerequisites
+
+To use Codestral chat model with Azure AI Foundry, you need the following prerequisites:
+
+### A model deployment
+
+**Deployment to serverless APIs**
+
+Codestral chat model can be deployed to serverless API endpoints with pay-as-you-go billing. This kind of deployment provides a way to consume models as an API without hosting them on your subscription, while keeping the enterprise security and compliance that organizations need. 
+
+Deployment to a serverless API endpoint doesn't require quota from your subscription. If your model isn't deployed already, use the Azure AI Foundry portal, Azure Machine Learning SDK for Python, the Azure CLI, or ARM templates to [deploy the model as a serverless API](deploy-models-serverless.md).
+
+> [!div class="nextstepaction"]
+> [Deploy the model to serverless API endpoints](deploy-models-serverless.md)
+
+### A REST client
+
+Models deployed with the [Azure AI model inference API](https://aka.ms/azureai/modelinference) can be consumed using any REST client. To use the REST client, you need the following prerequisites:
+
+* To construct the requests, you need to pass in the endpoint URL. The endpoint URL has the form `https://your-host-name.your-azure-region.inference.ai.azure.com`, where `your-host-name`` is your unique model deployment host name and `your-azure-region`` is the Azure region where the model is deployed (for example, eastus2).
+* Depending on your model deployment and authentication preference, you need either a key to authenticate against the service, or Microsoft Entra ID credentials. The key is a 32-character string.
+
+## Work with chat completions
+
+In this section, you use the [Azure AI model inference API](https://aka.ms/azureai/modelinference) with a chat completions model for chat.
+
+> [!TIP]
+> The [Azure AI model inference API](https://aka.ms/azureai/modelinference) allows you to talk with most models deployed in Azure AI Foundry portal with the same code and structure, including Codestral chat model.
+
+### Create a client to consume the model
+
+First, create the client to consume the model. The following code uses an endpoint URL and key that are stored in environment variables.
+
+### Get the model's capabilities
+
+The `/info` route returns information about the model that is deployed to the endpoint. Return the model's information by calling the following method:
+
+```http
+GET /info HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+```
+
+The response is as follows:
+
+
+```json
+{
+    "model_name": "Codestral-2501",
+    "model_type": "chat-completions",
+    "model_provider_name": "MistralAI"
+}
+```
+
+### Create a chat completion request
+
+The following example shows how you can create a basic chat completions request to the model.
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ]
+}
+```
+
+The response is as follows, where you can see the model's usage statistics:
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726686,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.",
+                "tool_calls": null
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+Inspect the `usage` section in the response to see the number of tokens used for the prompt, the total number of tokens generated, and the number of tokens used for the completion.
+
+#### Stream content
+
+By default, the completions API returns the entire generated content in a single response. If you're generating long completions, waiting for the response can take many seconds.
+
+You can _stream_ the content to get it as it's being generated. Streaming content allows you to start processing the completion as content becomes available. This mode returns an object that streams back the response as [data-only server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html#server-sent-events). Extract chunks from the delta field, rather than the message field.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "stream": true,
+    "temperature": 0,
+    "top_p": 1,
+    "max_tokens": 2048
+}
+```
+
+You can visualize how streaming generates content:
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "role": "assistant",
+                "content": ""
+            },
+            "finish_reason": null,
+            "logprobs": null
+        }
+    ]
+}
+```
+
+The last message in the stream has `finish_reason` set, indicating the reason for the generation process to stop.
+
+
+```json
+{
+    "id": "23b54589eba14564ad8a2e6978775a39",
+    "object": "chat.completion.chunk",
+    "created": 1718726371,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "delta": {
+                "content": ""
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+#### Explore more parameters supported by the inference client
+
+Explore other parameters that you can specify in the inference client. For a full list of all the supported parameters and their corresponding documentation, see [Azure AI Model Inference API reference](https://aka.ms/azureai/modelinference).
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "presence_penalty": 0.1,
+    "frequency_penalty": 0.8,
+    "max_tokens": 2048,
+    "stop": ["<|endoftext|>"],
+    "temperature" :0,
+    "top_p": 1,
+    "response_format": { "type": "text" }
+}
+```
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726686,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "As of now, it's estimated that there are about 7,000 languages spoken around the world. However, this number can vary as some languages become extinct and new ones develop. It's also important to note that the number of speakers can greatly vary between languages, with some having millions of speakers and others only a few hundred.",
+                "tool_calls": null
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 19,
+        "total_tokens": 91,
+        "completion_tokens": 72
+    }
+}
+```
+
+If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
+
+#### Create JSON outputs
+
+Codestral chat model can create JSON outputs. Set `response_format` to `json_object` to enable JSON mode and guarantee that the message the model generates is valid JSON. You must also instruct the model to produce JSON yourself via a system or user message. Also, the message content might be partially cut off if `finish_reason="length"`, which indicates that the generation exceeded `max_tokens` or that the conversation exceeded the max context length.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant that always generate responses in JSON format, using the following format: { \"answer\": \"response\" }"
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "response_format": { "type": "json_object" }
+}
+```
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718727522,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "{\"answer\": \"There are approximately 7,117 living languages in the world today, according to the latest estimates. However, this number can vary as some languages become extinct and others are newly discovered or classified.\"}",
+                "tool_calls": null
+            },
+            "finish_reason": "stop",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 39,
+        "total_tokens": 87,
+        "completion_tokens": 48
+    }
+}
+```
+
+### Pass extra parameters to the model
+
+The Azure AI Model Inference API allows you to pass extra parameters to the model. The following code example shows how to pass the extra parameter `logprobs` to the model. 
+
+Before you pass extra parameters to the Azure AI model inference API, make sure your model supports those extra parameters. When the request is made to the underlying model, the header `extra-parameters` is passed to the model with the value `pass-through`. This value tells the endpoint to pass the extra parameters to the model. Use of extra parameters with the model doesn't guarantee that the model can actually handle them. Read the model's documentation to understand which extra parameters are supported.
+
+```http
+POST /chat/completions HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+extra-parameters: pass-through
+```
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "logprobs": true
+}
+```
+
+The following extra parameters can be passed to Codestral chat model:
+
+| Name           | Description           | Type            |
+| -------------- | --------------------- | --------------- |
+| `ignore_eos` | Whether to ignore the EOS token and continue generating tokens after the EOS token is generated. | `boolean` |
+| `safe_mode` | Whether to inject a safety prompt before all conversations. | `boolean` |
+
+
+### Safe mode
+
+Codestral chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+
+> Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
+
+The Azure AI Model Inference API allows you to pass this extra parameter as follows:
+
+```http
+POST /chat/completions HTTP/1.1
+Host: <ENDPOINT_URI>
+Authorization: Bearer <TOKEN>
+Content-Type: application/json
+extra-parameters: pass-through
+```
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant."
+        },
+        {
+            "role": "user",
+            "content": "How many languages are in the world?"
+        }
+    ],
+    "safemode": true
+}
+```
+
+### Use tools
+
+Codestral chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+
+The following code example creates a tool definition that is able to look from flight information from two different cities.
+
+
+```json
+{
+    "type": "function",
+    "function": {
+        "name": "get_flight_info",
+        "description": "Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+        "parameters": {
+            "type": "object",
+            "properties": {
+                "origin_city": {
+                    "type": "string",
+                    "description": "The name of the city where the flight originates"
+                },
+                "destination_city": {
+                    "type": "string",
+                    "description": "The flight destination city"
+                }
+            },
+            "required": [
+                "origin_city",
+                "destination_city"
+            ]
+        }
+    }
+}
+```
+
+In this example, the function's output is that there are no flights available for the selected route, but the user should consider taking a train.
+
+Prompt the model to book flights with the help of this function:
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant that help users to find information about traveling, how to get to places and the different transportations options. You care about the environment and you always have that in mind when answering inqueries"
+        },
+        {
+            "role": "user",
+            "content": "When is the next flight from Miami to Seattle?"
+        }
+    ],
+    "tool_choice": "auto",
+    "tools": [
+        {
+            "type": "function",
+            "function": {
+                "name": "get_flight_info",
+                "description": "Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+                "parameters": {
+                    "type": "object",
+                    "properties": {
+                        "origin_city": {
+                            "type": "string",
+                            "description": "The name of the city where the flight originates"
+                        },
+                        "destination_city": {
+                            "type": "string",
+                            "description": "The flight destination city"
+                        }
+                    },
+                    "required": [
+                        "origin_city",
+                        "destination_city"
+                    ]
+                }
+            }
+        }
+    ]
+}
+```
+
+You can inspect the response to find out if a tool needs to be called. Inspect the finish reason to determine if the tool should be called. Remember that multiple tool types can be indicated. This example demonstrates a tool of type `function`.
+
+
+```json
+{
+    "id": "0a1234b5de6789f01gh2i345j6789klm",
+    "object": "chat.completion",
+    "created": 1718726007,
+    "model": "Codestral-2501",
+    "choices": [
+        {
+            "index": 0,
+            "message": {
+                "role": "assistant",
+                "content": "",
+                "tool_calls": [
+                    {
+                        "id": "abc0dF1gh",
+                        "type": "function",
+                        "function": {
+                            "name": "get_flight_info",
+                            "arguments": "{\"origin_city\": \"Miami\", \"destination_city\": \"Seattle\"}",
+                            "call_id": null
+                        }
+                    }
+                ]
+            },
+            "finish_reason": "tool_calls",
+            "logprobs": null
+        }
+    ],
+    "usage": {
+        "prompt_tokens": 190,
+        "total_tokens": 226,
+        "completion_tokens": 36
+    }
+}
+```
+
+To continue, append this message to the chat history:
+
+Now, it's time to call the appropriate function to handle the tool call. The following code snippet iterates over all the tool calls indicated in the response and calls the corresponding function with the appropriate parameters. The response is also appended to the chat history.
+
+View the response from the model:
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are a helpful assistant that help users to find information about traveling, how to get to places and the different transportations options. You care about the environment and you always have that in mind when answering inqueries"
+        },
+        {
+            "role": "user",
+            "content": "When is the next flight from Miami to Seattle?"
+        },
+        {
+            "role": "assistant",
+            "content": "",
+            "tool_calls": [
+                {
+                    "id": "abc0DeFgH",
+                    "type": "function",
+                    "function": {
+                        "name": "get_flight_info",
+                        "arguments": "{\"origin_city\": \"Miami\", \"destination_city\": \"Seattle\"}",
+                        "call_id": null
+                    }
+                }
+            ]
+        },
+        {
+            "role": "tool",
+            "content": "{ \"info\": \"There are no flights available from Miami to Seattle. You should take a train, specially if it helps to reduce CO2 emissions.\" }",
+            "tool_call_id": "abc0DeFgH" 
+        }
+    ],
+    "tool_choice": "auto",
+    "tools": [
+        {
+            "type": "function",
+            "function": {
+            "name": "get_flight_info",
+            "description": "Returns information about the next flight between two cities. This includes the name of the airline, flight number and the date and time of the next flight",
+            "parameters":{
+                "type": "object",
+                "properties": {
+                    "origin_city": {
+                        "type": "string",
+                        "description": "The name of the city where the flight originates"
+                    },
+                    "destination_city": {
+                        "type": "string",
+                        "description": "The flight destination city"
+                    }
+                },
+                "required": ["origin_city", "destination_city"]
+            }
+            }
+        }
+    ]
+}
+```
+
+### Apply content safety
+
+The Azure AI model inference API supports [Azure AI content safety](https://aka.ms/azureaicontentsafety). When you use deployments with Azure AI content safety turned on, inputs and outputs pass through an ensemble of classification models aimed at detecting and preventing the output of harmful content. The content filtering (preview) system detects and takes action on specific categories of potentially harmful content in both input prompts and output completions.
+
+The following example shows how to handle events when the model detects harmful content in the input prompt and content safety is enabled.
+
+
+```json
+{
+    "messages": [
+        {
+            "role": "system",
+            "content": "You are an AI assistant that helps people find information."
+        },
+                {
+            "role": "user",
+            "content": "Chopping tomatoes and cutting them into cubes or wedges are great ways to practice your knife skills."
+        }
+    ]
+}
+```
+
+
+```json
+{
+    "error": {
+        "message": "The response was filtered due to the prompt triggering Microsoft's content management policy. Please modify your prompt and retry.",
+        "type": null,
+        "param": "prompt",
+        "code": "content_filter",
+        "status": 400
+    }
+}
+```
+
+> [!TIP]
+> To learn more about how you can configure and control Azure AI content safety settings, check the [Azure AI content safety documentation](https://aka.ms/azureaicontentsafety).
+
+::: zone-end
+
+## More inference examples
+
+For more examples of how to use Mistral models, see the following examples and tutorials:
+
+| Description                               | Language          | Sample                                                          |
+|-------------------------------------------|-------------------|-----------------------------------------------------------------|
+| CURL request                              | Bash              | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
+| Azure AI Inference package for C#         | C#                | [Link](https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/ai/Azure.AI.Inference/samples)  |
+| Azure AI Inference package for JavaScript | JavaScript        | [Link](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/ai/ai-inference-rest/samples)  |
+| Azure AI Inference package for Python     | Python            | [Link](https://aka.ms/azsdk/azure-ai-inference/python/samples)  |
+| Python web requests                       | Python            | [Link](https://aka.ms/mistral-large/webrequests-sample)         |
+| OpenAI SDK (experimental)                 | Python            | [Link](https://aka.ms/mistral-large/openaisdk)                  |
+| LangChain                                 | Python            | [Link](https://aka.ms/mistral-large/langchain-sample)           |
+| Mistral AI                                | Python            | [Link](https://aka.ms/mistral-large/mistralai-sample)           |
+| LiteLLM                                   | Python            | [Link](https://aka.ms/mistral-large/litellm-sample)             | 
+
+
+## Cost and quota considerations for Mistral models deployed as serverless API endpoints
+
+Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
+
+Mistral models deployed as a serverless API are offered by MistralAI through Azure Marketplace and integrated with Azure AI Foundry for use. You can find Azure Marketplace pricing when deploying the model.
+
+Each time a project subscribes to a given offer from Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
+
+For more information on how to track costs, see [Monitor costs for models offered through Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
+
+## Related content
+
+
+* [Azure AI Model Inference API](../reference/reference-model-inference-api.md)
+* [Deploy models as serverless APIs](deploy-models-serverless.md)
+* [Consume serverless API endpoints from a different Azure AI Foundry project or hub](deploy-models-serverless-connect.md)
+* [Region availability for models in serverless API endpoints](deploy-models-serverless-availability.md)
+* [Plan and manage costs (marketplace)](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace)
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Codestralチャットモデルの使用方法に関する新規記事"
}
```

### Explanation
この変更は、Azure AI FoundryでのCodestralチャットモデルの使用方法に関する新しいMarkdownファイルが追加されたことを示しています。このファイルは、モデルの概要、導入手順、APIクライアントの使用方法、チャット補完のリクエスト作成、さらには安全性とツールの使用について詳細に説明しています。

具体的には、Codestral 2501モデルがコード生成タスクに特化しており、80以上のプログラミング言語での作業が可能であること、また、サーバーレスAPIとしてモデルがどのようにデプロイされるかについての手順が示されています。さらに、Python、JavaScript、C#、REST APIを使用してモデルを消費する具体的なコード例が含まれており、モデルの能力や使用法についての詳細な情報も提供されています。

この追加により、ユーザーはAzure AI Foundry環境でCodestralモデルを効率的に利用し、さまざまな機能を活用する方法を学ぶことができます。全体として、この文書は新機能としてユーザーに提供される情報資源です。

## articles/ai-studio/how-to/deploy-models-mistral-nemo.md{#item-e7b729}

<details>
<summary>Diff</summary>
````diff
@@ -18,8 +18,12 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
-In this article, you learn about Mistral Nemo chat model and how to use them.
-Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
+In this article, you learn about Mistral Nemo chat model and how to use it.
+Mistral AI offers two categories of models, namely:
+
+- _Premium models_: These include [Mistral Large, Mistral Small, and Ministral 3B](deploy-models-mistral.md) models, and are available as serverless APIs with pay-as-you-go token-based billing.  
+- _Open models_: These include [Codestral](deploy-models-mistral-codestral.md) and Mistral Nemo (that are available as serverless APIs with pay-as-you-go token-based billing), and [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md)(that are available to download and run on self-hosted managed endpoints).
+
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
@@ -276,7 +280,7 @@ The following extra parameters can be passed to Mistral Nemo chat model:
 
 ### Safe mode
 
-Mistral Nemo chat model support the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+Mistral Nemo chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
 
 > Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
 
@@ -297,7 +301,7 @@ response = client.complete(
 
 ### Use tools
 
-Mistral Nemo chat model support the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+Mistral Nemo chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
 
 The following code example creates a tool definition that is able to look from flight information from two different cities.
 
@@ -735,7 +739,7 @@ The following extra parameters can be passed to Mistral Nemo chat model:
 
 ### Safe mode
 
-Mistral Nemo chat model support the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+Mistral Nemo chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
 
 > Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
 
@@ -761,7 +765,7 @@ var response = await client.path("/chat/completions").post({
 
 ### Use tools
 
-Mistral Nemo chat model support the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+Mistral Nemo chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
 
 The following code example creates a tool definition that is able to look from flight information from two different cities.
 
@@ -1214,7 +1218,7 @@ The following extra parameters can be passed to Mistral Nemo chat model:
 
 ### Safe mode
 
-Mistral Nemo chat model support the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+Mistral Nemo chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
 
 > Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
 
@@ -1237,7 +1241,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 
 ### Use tools
 
-Mistral Nemo chat model support the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+Mistral Nemo chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
 
 The following code example creates a tool definition that is able to look from flight information from two different cities.
 
@@ -1752,7 +1756,7 @@ The following extra parameters can be passed to Mistral Nemo chat model:
 
 ### Safe mode
 
-Mistral Nemo chat model support the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
+Mistral Nemo chat model supports the parameter `safe_prompt`. You can toggle the safe prompt to prepend your messages with the following system prompt:
 
 > Always assist with care, respect, and truth. Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. Ensure replies promote fairness and positivity.
 
@@ -1785,7 +1789,7 @@ extra-parameters: pass-through
 
 ### Use tools
 
-Mistral Nemo chat model support the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
+Mistral Nemo chat model supports the use of tools, which can be an extraordinary resource when you need to offload specific tasks from the language model and instead rely on a more deterministic system or even a different language model. The Azure AI Model Inference API allows you to define tools in the following way.
 
 The following code example creates a tool definition that is able to look from flight information from two different cities.
 
@@ -2030,11 +2034,11 @@ For more examples of how to use Mistral models, see the following examples and t
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
-Mistral models deployed as a serverless API are offered by MistralAI through the Azure Marketplace and integrated with Azure AI Foundry for use. You can find the Azure Marketplace pricing when deploying the model.
+Mistral models deployed as a serverless API are offered by MistralAI through Azure Marketplace and integrated with Azure AI Foundry for use. You can find Azure Marketplace pricing when deploying the model.
 
-Each time a project subscribes to a given offer from the Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
+Each time a project subscribes to a given offer from Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
 
-For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
+For more information on how to track costs, see [Monitor costs for models offered through Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistral Nemoモデル使用に関するドキュメントの更新"
}
```

### Explanation
この変更は、Mistral Nemoチャットモデルに関連するドキュメントの一部が更新されたことを示しています。主な変更点には、モデルのカテゴリに関する説明が明確化され、モデル名やデプロイに関する情報が整理されています。具体的には、プレミアムモデルとオープンモデルの定義を改善し、Mistralモデルの利用方法がよりわかりやすくなっています。また、文中の誤字が修正され、文法が改善されることで、全体的な読みやすさが向上しています。

さらには、安全性のパラメータやツールの使用に関する説明が整頓され、Mistral Nemoモデルがどのように特定のタスクをオフロードできるかに関する情報が強調されています。これにより、ユーザーはMistral Nemoモデルをさらに効果的に活用できるようになります。この変更は軽微な更新ですが、ユーザー体験を向上させる重要な要素です。

## articles/ai-studio/how-to/deploy-models-mistral-open.md{#item-84e005}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,11 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral-7B and Mixtral chat models and how to use them.
-Mistral AI offers two categories of models. Premium models including [Mistral Large and Mistral Small](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
+Mistral AI offers two categories of models, namely:
+
+- _Premium models_: These include [Mistral Large, Mistral Small, and Ministral 3B](deploy-models-mistral.md) models, and are available as serverless APIs with pay-as-you-go token-based billing.  
+- _Open models_: These include [Codestral](deploy-models-mistral-codestral.md) and [Mistral Nemo](deploy-models-mistral-nemo.md) (that are available as serverless APIs with pay-as-you-go token-based billing), and Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01 (that are available to download and run on self-hosted managed endpoints).
+
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
@@ -64,7 +68,7 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Natively capable of function calling, enabling application development, and tech stack modernization at scale
 * Precise information recall from large documents, due to its 64K tokens context window
 
 
@@ -186,7 +190,7 @@ response = client.complete(
 ```
 
 > [!NOTE]
-> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02 and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02, and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -276,7 +280,7 @@ response = client.complete(
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -303,10 +307,10 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model before sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ::: zone-end
@@ -353,7 +357,7 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Natively capable of function calling, enabling application development, and tech stack modernization at scale
 * Precise information recall from large documents, due to its 64K tokens context window
 
 
@@ -475,7 +479,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!NOTE]
-> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02 and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02, and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -577,7 +581,7 @@ var response = await client.path("/chat/completions").post({
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -609,10 +613,10 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model before sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ::: zone-end
@@ -659,7 +663,7 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Natively capable of function calling, enabling application development, and tech stack modernization at scale
 * Precise information recall from large documents, due to its 64K tokens context window
 
 
@@ -795,7 +799,7 @@ Response<ChatCompletions> response = client.Complete(requestOptions);
 ```
 
 > [!NOTE]
-> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02 and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02, and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -898,7 +902,7 @@ Console.WriteLine($"Response: {response.Value.Choices[0].Message.Content}");
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -927,10 +931,10 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model before sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ::: zone-end
@@ -977,7 +981,7 @@ Mixtral 8x22B comes with the following strengths:
 
 * Fluent in English, French, Italian, German, and Spanish
 * Strong mathematics and coding capabilities
-* Natively capable of function calling, enabling application development and tech stack modernization at scale
+* Natively capable of function calling, enabling application development, and tech stack modernization at scale
 * Precise information recall from large documents, due to its 64K tokens context window
 
 
@@ -1068,7 +1072,7 @@ The following example shows how you can create a basic chat completions request
 ```
 
 > [!NOTE]
-> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02 and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
+> mistralai-Mistral-7B-Instruct-v01, mistralai-Mistral-7B-Instruct-v02, and mistralai-Mixtral-8x22B-Instruct-v0-1 don't support system messages (`role="system"`). When you use the Azure AI model inference API, system messages are translated to user messages, which is the closest capability available. This translation is offered for convenience, but it's important for you to verify that the model is following the instructions in the system message with the right level of confidence.
 
 The response is as follows, where you can see the model's usage statistics:
 
@@ -1231,7 +1235,7 @@ Explore other parameters that you can specify in the inference client. For a ful
 ```
 
 > [!WARNING]
-> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs are not guaranteed to be valid JSON.
+> Mistral models don't support JSON output formatting (`response_format = { "type": "json_object" }`). You can always prompt the model to generate JSON outputs. However, such outputs aren't guaranteed to be valid JSON.
 
 If you want to pass a parameter that isn't in the list of supported parameters, you can pass it to the underlying model using *extra parameters*. See [Pass extra parameters to the model](#pass-extra-parameters-to-the-model).
 
@@ -1270,10 +1274,10 @@ The following extra parameters can be passed to Mistral-7B and Mixtral chat mode
 
 | Name           | Description           | Type            |
 | -------------- | --------------------- | --------------- |
-| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
+| `logit_bias` | Accepts a JSON object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model before sampling. The exact effect varies per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token. | `float` |
 | `logprobs` | Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`. | `int` |
 | `top_logprobs` | An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used. | `float` |
-| `n` | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. | `int` |
+| `n` | How many chat completion choices to generate for each input message. You're charged based on the number of generated tokens across all of the choices. | `int` |
 
 
 ::: zone-end
@@ -1299,7 +1303,7 @@ For more examples of how to use Mistral models, see the following examples and t
 
 Mistral models deployed to managed compute are billed based on core hours of the associated compute instance. The cost of the compute instance is determined by the size of the instance, the number of instances running, and the run duration.
 
-It is a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
+It's a good practice to start with a low number of instances and scale up as needed. You can monitor the cost of the compute instance in the Azure portal.
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralオープンモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Mistralオープンモデルに関するドキュメントの一部が更新されたことを示しています。主な変更点には、モデルのカテゴリの明確化や、文中の表現の改善が含まれています。特に、プレミアムモデルとオープンモデルの説明が整理され、それぞれのモデルに関する具体的な情報が提供されるようになっています。

また、注意事項や警告の項目も改善され、ユーザーがMistralモデルを使用する際の理解が深まるように配慮されています。例えば、システムメッセージのサポートに関する注意や、JSON出力形式に関する警告がよりわかりやすく記述されています。これらの変更は、ドキュメント全体の可読性を向上させ、ユーザーがMistralモデルを効果的に利用するための支援となります。

## articles/ai-studio/how-to/deploy-models-mistral.md{#item-487a41}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,10 @@ zone_pivot_groups: azure-ai-model-catalog-samples-chat
 [!INCLUDE [feature-preview](../includes/feature-preview.md)]
 
 In this article, you learn about Mistral premium chat models and how to use them.
-Mistral AI offers two categories of models. Premium models including [Mistral Large, Mistral Small, and Ministral 3B](deploy-models-mistral.md), available as serverless APIs with pay-as-you-go token-based billing. Open models including [Mistral Nemo](deploy-models-mistral-nemo.md), [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md); available to also download and run on self-hosted managed endpoints.
+Mistral AI offers two categories of models, namely:
+
+- _Premium models_: These include Mistral Large, Mistral Small, and Ministral 3B models, and are available as serverless APIs with pay-as-you-go token-based billing.  
+- _Open models_: These include [Codestral](deploy-models-mistral-codestral.md) and [Mistral Nemo](deploy-models-mistral-nemo.md) (that are available as serverless APIs with pay-as-you-go token-based billing), and [Mixtral-8x7B-Instruct-v01, Mixtral-8x7B-v01, Mistral-7B-Instruct-v01, and Mistral-7B-v01](deploy-models-mistral-open.md)(that are available to download and run on self-hosted managed endpoints).
 
 [!INCLUDE [models-preview](../includes/models-preview.md)]
 
@@ -2230,11 +2233,11 @@ For more examples of how to use Mistral models, see the following examples and t
 
 Quota is managed per deployment. Each deployment has a rate limit of 200,000 tokens per minute and 1,000 API requests per minute. However, we currently limit one deployment per model per project. Contact Microsoft Azure Support if the current rate limits aren't sufficient for your scenarios.
 
-Mistral models deployed as a serverless API are offered by MistralAI through the Azure Marketplace and integrated with Azure AI Foundry for use. You can find the Azure Marketplace pricing when deploying the model.
+Mistral models deployed as a serverless API are offered by MistralAI through Azure Marketplace and integrated with Azure AI Foundry for use. You can find Azure Marketplace pricing when deploying the model.
 
-Each time a project subscribes to a given offer from the Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
+Each time a project subscribes to a given offer from Azure Marketplace, a new resource is created to track the costs associated with its consumption. The same resource is used to track costs associated with inference; however, multiple meters are available to track each scenario independently.
 
-For more information on how to track costs, see [Monitor costs for models offered through the Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
+For more information on how to track costs, see [Monitor costs for models offered through Azure Marketplace](costs-plan-manage.md#monitor-costs-for-models-offered-through-the-azure-marketplace).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralプレミアムモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、Mistralプレミアムモデルに関するドキュメントの更新を示しています。主な変更点は、モデルのカテゴリに関する説明がより明確になり、プレミアムモデルとオープンモデルの違いを強調するためのリスト形式が導入されたことです。これにより、ユーザーはそれぞれのモデルが持つ特徴をより分かりやすく把握できるようになりました。

具体的には、Mistral AIが提供するモデルカテゴリの説明が改善され、プレミアムモデルに関する情報が整理されています。また、注意事項や警告についての文言が修正され、文法の改善により読みやすさが向上しています。これらの更新は、Mistralモデルの利用を促進し、ユーザーがサービスや機能をより効率的に理解するのに役立ちます。

## articles/ai-studio/how-to/model-catalog-overview.md{#item-278001}

<details>
<summary>Diff</summary>
````diff
@@ -78,7 +78,7 @@ The following list contains Serverless API models. For Azure OpenAI models, see
 Model | Managed compute | Serverless API (pay-per-token)
 --|--|--
 Llama family models | Llama-3.3-70B-Instruct<BR> Llama-3.2-3B-Instruct<BR>  Llama-3.2-1B-Instruct<BR>  Llama-3.2-1B<BR>  Llama-3.2-90B-Vision-Instruct<BR>  Llama-3.2-11B-Vision-Instruct<BR>  Llama-3.1-8B-Instruct<BR>  Llama-3.1-8B<BR>  Llama-3.1-70B-Instruct<BR>  Llama-3.1-70B<BR>  Llama-3-8B-Instruct<BR>  Llama-3-70B<BR>  Llama-3-8B<BR>  Llama-Guard-3-1B<BR>  Llama-Guard-3-8B<BR>  Llama-Guard-3-11B-Vision<BR>  Llama-2-7b<BR>  Llama-2-70b<BR>  Llama-2-7b-chat<BR>  Llama-2-13b-chat<BR>  CodeLlama-7b-hf<BR>  CodeLlama-7b-Instruct-hf<BR>  CodeLlama-34b-hf<BR>  CodeLlama-34b-Python-hf<BR>  CodeLlama-34b-Instruct-hf<BR>  CodeLlama-13b-Instruct-hf<BR>  CodeLlama-13b-Python-hf<BR>  Prompt-Guard-86M<BR>  CodeLlama-70b-hf<BR> | Llama-3.3-70B-Instruct<BR> Llama-3.2-90B-Vision-Instruct<br>  Llama-3.2-11B-Vision-Instruct<br>  Llama-3.1-8B-Instruct<br>  Llama-3.1-70B-Instruct<br>  Llama-3.1-405B-Instruct<br>  Llama-3-8B-Instruct<br>  Llama-3-70B-Instruct<br>  Llama-2-7b<br>  Llama-2-7b-chat<br>  Llama-2-70b<br>  Llama-2-70b-chat<br>  Llama-2-13b<br>  Llama-2-13b-chat<br>
-Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo
+Mistral family models | mistralai-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x22B-Instruct-v0-1 <br> mistral-community-Mixtral-8x22B-v0-1 <br> mistralai-Mixtral-8x7B-v01 <br> mistralai-Mistral-7B-Instruct-v0-2 <br> mistralai-Mistral-7B-v01 <br> mistralai-Mixtral-8x7B-Instruct-v01 <br> mistralai-Mistral-7B-Instruct-v01 | Mistral-large (2402) <br> Mistral-large (2407) <br> Mistral-small <br> Ministral-3B <br> Mistral-NeMo <br> Codestral-2501
 Cohere family models | Not available | Cohere-command-r-plus-08-2024 <br> Cohere-command-r-08-2024 <br> Cohere-command-r-plus <br> Cohere-command-r <br> Cohere-embed-v3-english <br> Cohere-embed-v3-multilingual <br> Cohere-rerank-v3-english <br> Cohere-rerank-v3-multilingual
 JAIS | Not available | jais-30b-chat
 AI21 family models | Not available | Jamba-1.5-Mini <br> Jamba-1.5-Large
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Mistralモデルに関する文書の小規模更新"
}
```

### Explanation
この変更は、「Mistralモデル」に関する文書の内容を小規模に更新したものです。具体的には、Mistralモデルのリストに新しいモデル「Codestral-2501」が追加されました。この変更により、ユーザーは最新のMistralモデルの情報を把握しやすくなります。

また、文中の表記がわずかに修正され、モデルの説明がより明確になっています。これにより、モデルの種類やその利用方法に関する理解が深まり、文書全体の一貫性が向上しています。総じて、この更新はユーザーに対してMistralモデルに関する最新情報を提供することを目的としています。

## articles/ai-studio/includes/region-availability-maas.md{#item-35d79c}

<details>
<summary>Diff</summary>
````diff
@@ -57,10 +57,11 @@ Phi-3-Medium-4K-Instruct  <br>  Phi-3-Medium-128K-Instruct  | Not applicable | E
 
 |Model  |Offer Availability Region  | Hub/Project Region for Deployment  | Hub/Project Region for Fine tuning  |
 |---------|---------|---------|---------|
-Mistral Nemo     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong SAR<br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
-Ministral-3B     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong SAR <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
-Mistral Small     | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong SAR <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
-Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microsoft Managed countries/regions](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong SAR <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Codestral-2501    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Mistral Nemo     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel     | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
+Ministral-3B     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
+Mistral Small     | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)   <br> Brazil <br> Hong Kong <br> Israel      | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           |  Not available       |
+Mistral Large <br>  Mistral-Large (2407) <br> Mistral-Large (2411)    | [Microsoft Managed Countries](/partner-center/marketplace/tax-details-marketplace#microsoft-managed-countriesregions)  <br> Brazil <br> Hong Kong <br> Israel    | East US <br> East US 2 <br> North Central US <br> South Central US <br> Sweden Central <br> West US <br> West US 3           | Not available       |
 
 
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの可用性に関するドキュメントの更新"
}
```

### Explanation
この変更は、「モデルの可用性」についてのドキュメントに対する小規模な更新を示しています。具体的には、新たに「Codestral-2501」というモデルが追加され、他のMistral関連モデルについても可用性が整理されました。

変更により、以下のモデルに関する情報が更新されました:

- **Codestral-2501**: モデルの可用性とHub/Project地域の情報が明示的に追加されました。
- 他のMistralモデル（Mistral Nemo、Ministral-3B、Mistral Small、Mistral Large）についても同様に、可用性が整理され、必要に応じて地域名が正確に表記されています。

これらの更新により、ユーザーは各モデルの地域ごとの利用可能性をより正確に把握できるようになります。また、ドキュメントの一貫性と可読性が向上し、情報の信頼性も高まる結果につながっています。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -153,6 +153,8 @@ items:
       items:
         - name: Mistral premium models
           href: how-to/deploy-models-mistral.md
+        - name: Codestral model
+          href: how-to/deploy-models-mistral-codestral.md
         - name: Mistral Nemo model
           href: how-to/deploy-models-mistral-nemo.md
         - name: Mistral-7B and Mixtral models
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次にCodestralモデルの項目を追加"
}
```

### Explanation
この変更は、目次ファイル（toc.yml）に対する小規模な更新を示しています。具体的には、新しい「Codestralモデル」に関する項目が追加されました。これにより、ユーザーはCodestralモデルの関連ページに直接アクセスできるようになります。

変更内容は以下の通りです：

- **Codestralモデル**: 新たに目次に追加された項目で、リンク先として「how-to/deploy-models-mistral-codestral.md」が設定されています。
- これにより、ユーザーはMistralプレミアムモデルのセクション内でCodestralモデルに関する情報を容易に見つけることができるようになります。

この更新は、関連情報へのナビゲーションを改善し、最新のモデルに関するリソースを簡単に参照できるようにすることを目的としています。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -77,7 +77,7 @@ The goal with this application is to ground the model responses in your custom d
 You need an Azure AI Search service and connection in order to create a search index.
 
 > [!NOTE]
-> Creating an [Azure AI Search service](/azure/search/) and subsequent search indexes has associated costs. You can see details about pricing and pricing tiers for the Azure AI Search service on the creation page, to confirm cost before creating the resource.
+> Creating an [Azure AI Search service](/azure/search/) and subsequent search indexes has associated costs. You can see details about pricing and pricing tiers for the Azure AI Search service on the creation page, to confirm cost before creating the resource. For this tutorial, we recommend using a pricing tier of **Basic** or above.
 
 If you already have an Azure AI Search service, you can skip to the [next section](#connect).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルに価格ティアに関する推奨事項を追加"
}
```

### Explanation
この変更は、「コパイロットSDKリソースの作成」に関するチュートリアルのドキュメントに対する小規模な更新を示しています。具体的には、Azure AI Searchサービスの価格ティアに関する推奨事項が追加されました。

変更の内容は以下の通りです：

- **価格ティアの推奨**: 元の文の最後に、「このチュートリアルでは、**Basic**以上の価格ティアを使用することを推奨します。」という文章が追加されました。これにより、ユーザーは推奨される価格ティアを事前に知ることができ、リソースを作成する際の判断材料になります。

この更新は、ユーザーに対してより明確な指示を提供し、適切な価格プランを選択する手助けをすることを目的としています。また、サービスの使用に伴うコストについての理解を深めるのにも寄与します。


