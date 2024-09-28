---
date: '2024-09-15'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b0d11e...MicrosoftDocs:804ee13
summary: この変更の要約は、Azure OpenAIサービスに関するドキュメントの更新です。主な変更点には、新しい機能に関するガイドラインの追加、いくつかの注意事項の追加、ならびにメタデータやスクリーンショットの更新が含まれています。具体的には、GPT-4
  Turbo with Vision用のJavaScript SDKのクイックスタートガイドが追加され、複数のドキュメントでメタデータが更新されました。また、JSONモードや構造化出力に関する新しい注意事項も盛り込まれています。このような改訂により、ユーザーは最新の情報をもとにより適切にサービスを利用できるようになります。特に、料金確認に関する情報とDALL-Eを使った画像生成のガイドが更新され、実用性が向上しています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:3b0d11e...MicrosoftDocs:804ee13){target="_blank"}

# Highlights
今回のコードの差分は主に、Azure OpenAIの各種サービスに関するドキュメントの更新です。特に目立つ変更点としては、新しい注意事項の追加、新機能のガイドラインの追加、およびメタデータやスクリーンショットの更新が挙げられます。以下に、各主要な変更点をまとめます。

## New features
- GPT-4 Turbo with VisionのためのJavaScript SDKクイックスタートガイドの追加。
- 価格確認のための画像の追加。

## Breaking changes
- 特記すべきブレイキングチェンジはありません。

## Other updates
- 複数のドキュメントに対するメタデータの更新。
- JSONモードや構造化出力に関する新しい注意事項の追加。
- クイックスタートガイドのTypeScriptサポートの追加。
- デプロイメントスクリーン及び価格確認に関連する新しい注意事項の追加。

# Insights
この差分の変更は、Azure OpenAIサービスのドキュメントがより現実的で実用的な内容になるように意図されています。以下に主要な変更点について詳しく解説します。

## Azure OpenAI モデルの引退日と自動更新の日付の更新
モデルの引退日に関する最新情報が更新されており、ユーザーは終了日と自動更新日に関する正確な情報を得られます。このような情報の更新は、特定のバージョンに依存するユーザーにとって非常に重要です。

## DALL·Eクイックスタートのメタデータの更新
メタデータにTypeScriptのデータを追加したことで、TypeScriptを使用する開発者が関連情報を容易に見つけ、活用できるように配慮されています。

## GPT-VクイックスタートのメタデータとJavaScriptサポートの追加
JavaScript及びTypeScriptのトラッキングが追加され、マルチプラットフォームでの利用が進化しました。この変更により、より多くの開発者が参加しやすくなります。

## JSONモードに関する注意事項の追加
特定のシナリオで構造化出力がサポートされていないという重要な制約が明記されました。このような注意喚起は、ユーザーが適切にツールを使用し、誤解や無駄な試行錯誤を避ける助けとなります。

## プロビジョンドデプロイメント利用時の価格確認と注意事項の追加
デプロイメントの価格確認に関する新しい情報が追加され、誤解を避けるための推奨事項が明記されています。これにより、ユーザーが予期しないコストを避けるための具体的な手段が示されます。

## 構造化出力に関する注意事項の追加
こちらもJSONモードと同様に、構造化出力の制約について明記されています。これにより、ユーザーはどのシナリオで構造化出力を有効に活用できるかを正確に理解できるでしょう。

## DALL-Eを使用した画像生成のJavaScriptガイドの更新
新しいバージョン(dall-e-3)に対応したガイドが追加され、使用するライブラリやコード例が最新のものに更新されました。このアップデートにより、ユーザーは最新の環境で適切にDALL-Eを使用できるようになります。

## JavaScript SDKを使用したGPT-4 Turbo with Visionのクイックスタートガイドの追加
実践的なサンプルコードを含む詳細なガイドが追加され、ユーザーが簡単にGPT-4 Turbo with Visionを使い始めることができます。この新機能ガイドは特に新しい機能を一迅に学びたいユーザーにとって有用です。

## デプロイメントスクリーン画像の更新
最新のUIを反映したスクリーンショットが提供されており、実際の操作手順が視覚的に理解しやすくなるよう配慮されています。

これらの更新を通じて、Azure OpenAIのドキュメントがさらに実用的で最新

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [model-retirements.md](#item-03fc2e) | minor update | Azure OpenAI モデルの引退日と自動更新の日付の更新 | modified | 9 | 5 | 14 | 
| [dall-e-quickstart.md](#item-fcd528) | minor update | DALL·Eクイックスタートのメタデータの更新 | modified | 2 | 2 | 4 | 
| [gpt-v-quickstart.md](#item-2a6183) | minor update | GPT-VクイックスタートのメタデータとJavaScriptサポートの追加 | modified | 7 | 1 | 8 | 
| [json-mode.md](#item-50fa9e) | minor update | JSONモードに関する注意事項の追加 | modified | 3 | 0 | 3 | 
| [provisioned-get-started.md](#item-c8df1c) | minor update | プロビジョンドデプロイメント利用時の価格確認と注意事項の追加 | modified | 18 | 7 | 25 | 
| [provisioned-throughput-onboarding.md](#item-3eb72b) | minor update | プロビジョンドスループットのオンボーディングに関する警告と情報の追加 | modified | 8 | 5 | 13 | 
| [structured-outputs.md](#item-cc2557) | minor update | 構造化出力に関する注意事項の追加 | modified | 3 | 0 | 3 | 
| [dall-e-javascript.md](#item-6cffcf) | minor update | DALL-Eを使用した画像生成のJavaScriptガイドを更新 | modified | 114 | 23 | 137 | 
| [gpt-v-javascript.md](#item-a128c9) | new feature | JavaScript SDKを使用したGPT-4 Turbo with Visionのクイックスタートガイドの追加 | added | 246 | 0 | 246 | 
| [use-your-data-javascript.md](#item-786699) | minor update | JavaScriptでのデータ利用に関するガイドの更新 | modified | 192 | 59 | 251 | 
| [confirm-pricing.png](#item-761d2a) | new feature | 価格確認のための画像の追加 | added | 0 | 0 | 0 | 
| [deployment-screen.png](#item-5bc2ef) | minor update | デプロイメントスクリーン画像の更新 | modified | 0 | 0 | 0 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | クイックスタートガイドの内容更新 | modified | 22 | 3 | 25 | 
| [whats-new.md](#item-53303b) | minor update | 新機能ページの文言修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/openai/concepts/model-retirements.md{#item-03fc2e}

<details>
<summary>Diff</summary>
````diff
@@ -4,7 +4,7 @@ titleSuffix: Azure OpenAI
 description: Learn about the model deprecations and retirements in Azure OpenAI.
 ms.service: azure-ai-openai
 ms.topic: conceptual
-ms.date: 09/09/2024
+ms.date: 09/12/2024
 ms.custom: 
 manager: nitinme
 author: mrbullwinkle
@@ -91,9 +91,9 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Version | Retirement date | Suggested replacements |
 | ---- | ---- | ---- | --- |
-| `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
-| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
-| `gpt-35-turbo` | 1106 | No earlier than Nov 17, 2024 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
+| `gpt-35-turbo` | 0301 | January 27, 2025<br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.   | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`  |
+| `gpt-35-turbo`<br>`gpt-35-turbo-16k` | 0613 | January 27, 2025 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.  | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini`|
+| `gpt-35-turbo` | 1106 | No earlier than Nov 17, 2024 <br><br> Deployments set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024. | `gpt-35-turbo` (0125) <br><br> `gpt-4o-mini` |
 | `gpt-35-turbo` | 0125 | No earlier than Feb 22, 2025 | `gpt-4o-mini` |
 | `gpt-4`<br>`gpt-4-32k` | 0314 | June 6, 2025 | `gpt-4o` |
 | `gpt-4`<br>`gpt-4-32k` | 0613 | June 6, 2025 | `gpt-4o` |
@@ -115,7 +115,7 @@ These models are currently available for use in Azure OpenAI Service.
 
 | Model | Current default version | New default version | Default upgrade date |
 |---|---|---|---|
-| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 15, 2024.|
+| `gpt-35-turbo` | 0301 | 0125 | Deployments of versions `0301`, `0613`, and `1106` set to [**Auto-update to default**](/azure/ai-services/openai/how-to/working-with-models?tabs=powershell#auto-update-to-default) will be automatically upgraded to version: `0125`, starting on November 13, 2024.|
 
 
 
@@ -158,6 +158,10 @@ If you're an existing customer looking for information about these models, see [
 
 ## Retirement and deprecation history
 
+## September 12, 2024
+
+* `gpt-35-turbo` (0301), (0613), (1106) and `gpt-35-turbo-16k` (0613) auto-update to default upgrade date updated to November 13, 2024.
+
 ## September 9, 2024
 
 * `gpt-35-turbo` (0301) and (0613) retirement changed to January 27, 2025.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI モデルの引退日と自動更新の日付の更新"
}
```

### Explanation
この修正は、Azure OpenAI サービスにおけるモデルの引退日および自動更新の日付に関する情報を更新するものです。主な変更点は、特定のモデル（`gpt-35-turbo`の異なるバージョン）に対して、自動更新が行われる新しい日付が設定されたことです。具体的には、以前の更新日から変更され、 November 15, 2024 から November 13, 2024 に変更されました。

また、更新された日付に関連する内容も新たに追加され、ユーザーがモデルの引退プロセスをより理解しやすくしています。この修正により、ドキュメントは最新の情報を反映し、ユーザーにとって価値のある参考資料となっています。全体で、9行が追加され、5行が削除された結果、合計で14行の変更が行われました。

## articles/ai-services/openai/dall-e-quickstart.md{#item-fcd528}

<details>
<summary>Diff</summary>
````diff
@@ -5,11 +5,11 @@ description: Learn how to get started generating images with Azure OpenAI Servic
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: devx-track-python, devx-track-dotnet, devx-track-extended-java, devx-track-go, devx-track-js
+ms.custom: devx-track-python, devx-track-dotnet, devx-track-extended-java, devx-track-go, devx-track-js, devx-track-ts
 ms.topic: quickstart
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 08/21/2024
+ms.date: 09/06/2024
 zone_pivot_groups: openai-quickstart-dall-e
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·Eクイックスタートのメタデータの更新"
}
```

### Explanation
この変更は、DALL·Eのクイックスタートに関するドキュメントのメタデータを更新するものです。具体的には、`ms.custom`に新たに`devx-track-ts`が追加され、TypeScriptに関する追跡が含まれました。また、文書の日付が2024年8月21日から2024年9月6日に変更されています。

これにより、このドキュメントにはTypeScriptに関する情報が明確に示されるようになり、開発者がDALL·Eを使用する際の参考として役立つ情報が提供されます。全体として、2行が追加され、2行が削除され、合計4行の変更が行われました。

## articles/ai-services/openai/gpt-v-quickstart.md{#item-2a6183}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Use this article to get started using Azure OpenAI to deploy and us
 services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: devx-track-python
+ms.custom: devx-track-python, devx-track-js, devx-track-ts
 ms.topic: quickstart
 author: PatrickFarley
 ms.author: pafarley
@@ -39,6 +39,12 @@ Get started using GPT-4 Turbo with images with the Azure OpenAI Service.
 
 ::: zone-end
 
+::: zone pivot="programming-language-javascript"
+
+[!INCLUDE [JavaScript quickstart](includes/gpt-v-javascript.md)]
+
+::: zone-end
+
 ## Next steps
 
 * Learn more about these APIs in the [GPT-4 Turbo with Vision how-to guide](./gpt-v-quickstart.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "GPT-VクイックスタートのメタデータとJavaScriptサポートの追加"
}
```

### Explanation
この修正は、GPT-Vのクイックスタートに関するドキュメントのメタデータと内容を更新するものです。変更点として、`ms.custom`にJavaScriptおよびTypeScriptのトラッキングが追加され、開発者に向けた情報が充実しました。具体的には、`devx-track-js`と`devx-track-ts`が追加されており、これにより、JavaScriptとTypeScriptを使用するユーザーのための明確なサポートが提供されます。

さらに、新しいセクションが追加され、JavaScriptに関するクイックスタートへのリンクも組み込まれました。これにより、ユーザーはGPT-4 Turboを画像生成に使用する際の手順をより簡単に理解できるようになります。全体で、7行が追加され、1行が削除され、合計8行の変更が行われました。

## articles/ai-services/openai/how-to/json-mode.md{#item-50fa9e}

<details>
<summary>Diff</summary>
````diff
@@ -20,6 +20,9 @@ JSON mode allows you to set the models response format to return a valid JSON ob
 > [!NOTE]
 > While JSON mode is still supported, when possible we recommend using [structured outputs](./structured-outputs.md). Like JSON mode structured outputs generates valid JSON, but with the added benefit that you can constrain the model to use a specific JSON schema.
 
+>[!NOTE]
+> Currently Structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
+
 ## JSON mode support
 
 JSON mode is only currently supported with the following models:
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JSONモードに関する注意事項の追加"
}
```

### Explanation
この変更は、JSONモードに関するドキュメントに新しい注意事項を追加するもので、特に「データを持ち込む」シナリオにおいて構造化出力がサポートされていないことを明記しています。この修正により、ユーザーがJSONモードを使用する際の制限がより明確になり、誤解を避ける手助けとなります。

具体的には、3行が新たに追加され、構造化出力に関する新しい注記が導入されたことが主な変更点です。この改善により、ユーザーは利用可能な機能を理解しやすくなり、適切な選択ができるようになります。全体として、文書の明瞭さが向上しました。

## articles/ai-services/openai/how-to/provisioned-get-started.md{#item-c8df1c}

<details>
<summary>Diff</summary>
````diff
@@ -75,7 +75,17 @@ After you purchase a commitment on your quota, you can create a deployment. To c
 
 Important things to note: 
 * The deployment dialog contains a reminder that you can purchase an Azure Reservation for Azure OpenAI Provisioned to obtain a significant discount for a term commitment. 
-* There is a message that tells you the list, hourly price of the deployment that you would be charged if this deployment is not covered by a reservation.  This is a list price that does not include any negotiated discounts for your company. 
+
+Once you have entered the deployment settings, click **Confirm Pricing** to continue.  A pricing confirmation dialog will appear that will display the list price for the deployment, if you choose to pay for it on an hourly basis, with no Azure Reservation to provide a term discount.
+
+If you are unsure of the costs, cancel the deployment and proceed once you understand the payment model and underlying costs for provisioned deployment. This step may prevent unexpected, high charges on your payment invoice. Resources to educate yourself include: 
+
+* [Azure Pricing Portal](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/) 
+* [Understanding the provisioned throughput purchase model](provisioned-throughput-onboarding.md#understanding-the-provisioned-throughput-purchase-model) 
+
+The image below shows the pricing confirmation you will see. The price shown is an example only. 
+
+:::image type="content" source="../media/provisioned/confirm-pricing.png" alt-text="Screenshot showing the pricing confirmation screen." lightbox="../media/provisioned/confirm-pricing.png":::
 
 If you wish to create your deployment programmatically, you can do so with the following Azure CLI command. Update the `sku-capacity` with the desired number of provisioned throughput units.
 
@@ -110,16 +120,17 @@ Things to notice:
 
 Selecting a resource and clicking **Switch resource** will cause the deployment dialog to redisplay using the selected resource. You can then proceed to create your deployment in the new region. 
 
-Learn more about the purchase model and how to purchase a reservation: 
-
-* [Azure OpenAI provisioned onboarding guide](./provisioned-throughput-onboarding.md) 
-* [Guide for Azure OpenAI provisioned reservations](../concepts/provisioned-throughput.md) 
-
 ## Optionally purchase a reservation 
 
 Following the creation of your deployment, you might want to purchase a term discount via an Azure Reservation.  An Azure Reservation can provide a substantial discount on the hourly rate for users intending to use the deployment beyond a few days.   
 
-For more information on purchasing a reservation, see [Save costs with Microsoft Azure OpenAI service Provisioned Reservations](/azure/cost-management-billing/reservations/azure-openai).
+For more information on the purchase model and reservations, see:
+* [Save costs with Microsoft Azure OpenAI service provisioned reservations](/azure/cost-management-billing/reservations/azure-openai).
+* [Azure OpenAI provisioned onboarding guide](./provisioned-throughput-onboarding.md) 
+* [Guide for Azure OpenAI provisioned reservations](../concepts/provisioned-throughput.md) 
+
+> [!IMPORTANT]
+> Capacity availability for model deployments is dynamic and changes frequently across regions and models. To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed. This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use.
 
 ## Make your first inferencing calls
 The inferencing code for provisioned deployments is the same a standard deployment type. The following code snippet shows a chat completions call to a GPT-4 model. For your first time using these models programmatically, we recommend starting with our [quickstart guide](../quickstart.md). Our recommendation is to use the OpenAI library with version 1.0 or greater since this includes retry logic within the library.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョンドデプロイメント利用時の価格確認と注意事項の追加"
}
```

### Explanation
この変更は、Azure OpenAIのプロビジョンドデプロイメントに関するドキュメントの内容を改善し、価格確認手順や注意事項を追加するものです。主な修正点は、デプロイ設定を入力した後の**確定価格**ボタンに関する詳細な説明を加え、確認ダイアログによってデプロイのリスト価格が表示されることを明記しました。

また、予期しない高額請求を避けるために、デプロイをキャンセルし、料金モデルと基礎となるコストを理解してから進むことを推奨しています。さらに、追加の教育リソースへのリンクも提供され、利用者に継続的に情報を得る機会が与えられています。

修正の一環として、ダイナミックなモデルデプロイメントの容量可用性についての注意喚起や、デプロイを作成した後にAzure Reservationsを購入することを推奨する重要な情報が追加されました。全体的に、この更新により、デプロイメントのプロセスがより明確になり、ユーザーがコストをよりよく理解できるようになります。

## articles/ai-services/openai/how-to/provisioned-throughput-onboarding.md{#item-3eb72b}

<details>
<summary>Diff</summary>
````diff
@@ -3,7 +3,7 @@ title: Azure OpenAI Service Provisioned Throughput Units (PTU) onboarding
 description: Learn about provisioned throughput units onboarding and Azure OpenAI. 
 ms.service: azure-ai-openai
 ms.topic: conceptual 
-ms.date: 08/07/2024
+ms.date: 09/12/2024
 manager: nitinme
 author: mrbullwinkle 
 ms.author: mbullwin 
@@ -81,6 +81,7 @@ Customers that require long-term usage of provisioned deployments, however, migh
 > It is not recommended to scale production deployments according to incoming traffic and pay for them purely on an hourly basis. There are two reasons for this:
 > * The cost savings achieved by purchasing an Azure Reservation for Azure OpenAI Provisioned are significant, and it will be less expensive in many cases to maintain a deployment sized for full production volume paid for via a reservation than it would be to scale the deployment with incoming traffic.
 > * Having unused provisioned quota (PTUs) does not guarentee that capacity will be available to support increasing the size of the deployment when required. Quota limits the maximum number of PTUs that can be deployed, but it is not a capacity guarantee. Provisioned capacity for each region and modal dynamically changes throughout the day and might not be available when required. As a result, it is recommended to maintain a permanant deployment to cover your traffic needs (paid for via a reservation).
+> * Charges for deployments on a deleted resource will continue until the resource is purged.  To prevent this, delete a resource’s deployment before deleting the resource.  For more information, see [Recover or purge deleted Azure AI services resources](../../recover-purge-resources.md). 
 
 ## Azure Reservations for Azure OpenAI Provisioned   
 
@@ -103,9 +104,11 @@ Discounts on top of the hourly usage price can be obtained by purchasing an Azur
 * If the size of provisioned deployments within the scope of a reservation exceeds the amount of the reservation, the excess is charged at the hourly rate. For example, if deployments amounting to 250 PTUs exist within the scope of a 200 PTU reservation, 50 PTUs will be charged on an hourly basis until the deployment sizes are reduced to 200 PTUs, or a new reservation is created to cover the remaining 50. 
 
 * Reservations guarantee a discounted price for the selected term.  They do not reserve capacity on the service or guarantee that it will be available when a deployment is created.  It is highly recommended that customers create deployments prior to purchasing a reservation to prevent from over-purchasing a reservation. 
- 
-> [!NOTE]
-> The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
+
+> [!IMPORTANT] 
+> * Capacity availability for model deployments is dynamic and changes frequently across regions and models.  To prevent you from purchasing a reservation for more PTUs than you can use, create deployments first, and then purchase the Azure Reservation to cover the PTUs you have deployed.  This best practice will ensure that you can take full advantage of the reservation discount and prevent you from purchasing a term commitment that you cannot use. 
+>
+> * The Azure role and tenant policy requirements to purchase a reservation are different than those required to create a deployment or Azure OpenAI resource.  Verify authorization to purchase reservations in advance of needing to do so. See Azure OpenAI [Provisioned reservation documentation](https://aka.ms/oai/docs/ptum-reservations) for more details.
 
 ## Important: Sizing Azure OpenAI Provisioned Reservations 
 
@@ -119,7 +122,7 @@ To assist customers with purchasing the correct reservation amounts. The total n
 
 Managing Azure Reservations 
 
-After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you are expecting.  This may be done via the Azure Reservation Portal or Azure Monitor.  Details on these topics and others can be found here: 
+After a reservation is created, it is a best practice monitor it to ensure it is receiving the usage you are expecting.  This can be done via the Azure Reservation Portal or Azure Monitor.  Details on these topics and others can be found here: 
 
 * [View Azure reservation utilization](/azure/cost-management-billing/reservations/reservation-utilization) 
 * [View Azure Reservation purchase and refund transactions](/azure/cost-management-billing/reservations/view-purchase-refunds) 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロビジョンドスループットのオンボーディングに関する警告と情報の追加"
}
```

### Explanation
この変更は、Azure OpenAIサービスにおけるプロビジョンドスループットユニットのオンボードに関する文書を更新し、重要な警告と情報を追加することを目的としています。主な修正には、料金が発生するリソースの削除手順や、デプロイメント前に予約を購入することの重要性が新たに強調されています。

特に、削除されたリソースに対するデプロイメントの料金が、リソースが完全に消去されるまで続くことが明記されています。この点に関する注意喚起により、ユーザーはコストを適切に管理し、不要な請求を避けることができるようになります。

さらに、プロビジョンドデプロイメントの容量の可用性がダイナミックに変化し、モデル間および地域間で頻繁に変動することが強調されています。これにより、ユーザーは予約を購入する前にまずデプロイを作成するべきであるというベストプラクティスについての理解を深めることができます。

全体として、この更新は前の情報の明確化と重要な注意事項の追加を通じて、ユーザーがプロビジョンドスループットユニットを利用する際の手続きを向上させることを意図しています。

## articles/ai-services/openai/how-to/structured-outputs.md{#item-cc2557}

<details>
<summary>Diff</summary>
````diff
@@ -16,6 +16,9 @@ recommendations: false
 
 Structured outputs make a model follow a [JSON Schema](https://json-schema.org/overview/what-is-jsonschema) definition that you provide as part of your inference API call. This is in contrast to the older [JSON mode](./json-mode.md) feature, which guaranteed valid JSON would be generated, but was unable to ensure strict adherence to the supplied schema. Structured outputs is recommended for function calling, extracting structured data, and building complex multi-step workflows.
 
+>[!NOTE]
+> Currently Structured outputs is not supported on [bring your own data](../concepts/use-your-data.md) scenario.
+
 ## Supported models
 
 Currently only `gpt-4o` version: `2024-08-06` supports structured outputs.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "構造化出力に関する注意事項の追加"
}
```

### Explanation
この変更は、Azure OpenAIの構造化出力に関する文書を更新し、重要な注意事項を追加するものです。具体的には、構造化出力が現在「自分のデータを持ち込む」シナリオではサポートされていないことが明示されています。この注意事項により、ユーザーは適切なコンテキストで構造化出力機能を利用する際の制約を理解することができます。

構造化出力に関するその他の説明は、推論API呼び出しの一部として提供されるJSON Schema定義に沿ったモデルの動作について述べています。これにより、ユーザーは機能呼び出しや構造化データの抽出、複雑なマルチステップワークフローの構築において、この機能を効果的に利用できることが強調されています。

全体として、この更新は構造化出力の利用を検討しているユーザーに、より明確なガイダンスを提供し、使用時の注意事項を資料内に組み込むことを目的としています。

## articles/ai-services/openai/includes/dall-e-javascript.md{#item-6cffcf}

<details>
<summary>Diff</summary>
````diff
@@ -8,19 +8,30 @@ ms.service: azure-ai-openai
 ms.topic: include
 author: PatrickFarley
 ms.author: pafarley
-ms.date: 08/24/2023
+ms.date: 09/06/2024
 ---
 
 Use this guide to get started generating images with the Azure OpenAI SDK for JavaScript.
 
-[Library source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai) | [Package (npm)](https://www.npmjs.com/package/@azure/openai) | [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)
+[Reference documentation](https://platform.openai.com/docs/api-reference/images/create) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 ## Prerequisites
 
+#### [TypeScript](#tab/typescript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+#### [JavaScript](#tab/javascript)
+
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
 
+---
 
 ## Setup
 
@@ -39,10 +50,10 @@ npm init
 
 ## Install the client library
 
-Install the Azure OpenAI client library for JavaScript with npm:
+Install the client libraries with:
 
 ```console
-npm install @azure/openai
+npm install openai @azure/identity
 ```
 
 Your app's _package.json_ file will be updated with the dependencies.
@@ -51,43 +62,123 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Create a new file named _ImageGeneration.js_ and open it in your preferred code editor. Copy the following code into the _ImageGeneration.js_ file:
 
-```javascript
-const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");
+#### [TypeScript](#tab/typescript)
+
+```typescript
+import "dotenv/config";
+import { AzureOpenAI } from "openai";
 
 // You will need to set these environment variables or edit the following values
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] ;
-const azureApiKey = process.env["AZURE_OPENAI_API_KEY"] ;
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-07-01";
+const deploymentName = "dall-e-3";
 
 // The prompt to generate images from
 const prompt = "a monkey eating a banana";
-const size = "256x256";
+const numberOfImagesToGenerate = 1;
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function main() {
+  console.log("== Image Generation ==");
+
+  const client = getClient();
+
+  const results = await client.images.generate({
+    prompt,
+    size: "1024x1024",
+    n: numberOfImagesToGenerate,
+    model: "",
+    style: "vivid", // or "natural"
+  });
+
+  for (const image of results.data) {
+    console.log(`Image generation result URL: ${image.url}`);
+  }
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
 
-// The number of images to generate
-const n = 2;
+    ```console
+    node ImageGeneration.js
+    ```
 
+
+#### [JavaScript](#tab/javascript)
+
+```javascript
+require("dotenv/config");
+const { AzureOpenAI } = require("openai");
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-07-01";
+const deploymentName = "dall-e-3";
+
+// The prompt to generate images from
+const prompt = "a monkey eating a banana";
+const numberOfImagesToGenerate = 1;
+
+function getClient() {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
 async function main() {
-    console.log("== Batch Image Generation ==");
-  
-    const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
-    const deploymentName = "dall-e";
-    const results = await client.getImages(deploymentName, prompt, { n, size });
-  
-    for (const image of results.data) {
-      console.log(`Image generation result URL: ${image.url}`);
-    }
-    //console.log(`Image generation result URL: ${results.result.status}`);
+  console.log("== Image Generation ==");
+
+  const client = getClient();
+
+  const results = await client.images.generate({
+    prompt,
+    size: "1024x1024",
+    n: numberOfImagesToGenerate,
+    model: "",
+    style: "vivid", // or "natural"
+  });
+
+  for (const image of results.data) {
+    console.log(`Image generation result URL: ${image.url}`);
+  }
 }
 
 main().catch((err) => {
-console.error("The sample encountered an error:", err);
+  console.error("The sample encountered an error:", err);
 });
 ```
 
 Run the script with the following command:
 
 ```console
-node _ImageGeneration.js
+node ImageGeneration.js
 ```
+---
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eを使用した画像生成のJavaScriptガイドを更新"
}
```

### Explanation
この変更は、Azure OpenAIにおけるDALL-Eを使用した画像生成に関するJavaScriptのガイドを大幅に更新し、最新の情報を反映させることを目的としています。更新内容には、使用するライブラリの変更や新たなコード例の追加が含まれており、JavaScriptおよびTypeScriptの両方での画像生成のためのセットアップ手順が詳述されています。

特に、DALL-Eの新しいバージョン（dall-e-3）に対応したAPIの利用方法が明確に示されており、環境変数の設定や、Node.jsのLTSバージョンの指定といった事前条件も新たに重要な情報として追加されています。

また、サンプルコードが改善され、より簡潔でわかりやすい形式で提供されているため、ユーザーは指定されたプロンプトに基づいて画像を生成し、生成結果のURLを取得する手順を容易に理解できるようになっています。

全体として、このドキュメントの更新は、ユーザーがDALL-Eを使用して画像生成機能を効果的に活用できるように、最新のベストプラクティスと手順を提供することを目指しています。

## articles/ai-services/openai/includes/gpt-v-javascript.md{#item-a128c9}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,246 @@
+---
+title: 'Quickstart: Use GPT-4 Turbo with Vision on your images and videos with the JavaScript SDK'
+titleSuffix: Azure OpenAI
+description: Get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model.
+services: cognitive-services
+manager: nitinme
+ms.service: azure-ai-openai
+ms.topic: include
+ms.custom: references_regions
+ms.date: 09/06/2024
+---
+
+Use this article to get started using the OpenAI JavaScript SDK to deploy and use the GPT-4 Turbo with Vision model. 
+
+This SDK is provided by OpenAI with Azure specific types provided by Azure. 
+
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Library source code](https://github.com/openai/openai-node?azure-portal=true) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+
+## Prerequisites
+
+## [**TypeScript**](#tab/typescript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+
+## [**JavaScript**](#tab/javascript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- An Azure OpenAI resource created in a supported region (see [Region availability](/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)). For more information, see [Create a resource and deploy a model with Azure OpenAI](../how-to/create-resource.md).
+
+---
+
+
+> [!NOTE]
+> This library is maintained by OpenAI. Refer to the [release history](https://github.com/openai/openai-node/releases) to track the latest updates to the library.
+
+[!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
+
+[!INCLUDE [environment-variables](environment-variables.md)]
+
+
+## Create a Node application
+
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. Then run the `npm init` command to create a node application with a _package.json_ file.
+
+```console
+npm init
+```
+
+## Install the client library
+
+Install the client libraries with:
+
+```console
+npm install openai @azure/identity
+```
+
+Your app's _package.json_ file will be updated with the dependencies.
+
+## Create a new JavaScript application for image prompts
+
+Select an image from the [azure-samples/cognitive-services-sample-data-files](https://github.com/Azure-Samples/cognitive-services-sample-data-files/tree/master/ComputerVision/Images) and set the URL for an image in the environment variables.
+
+## [**TypeScript**](#tab/typescript)
+
+1. Create a _quickstart.ts_ and paste in the following code. 
+    
+    ```typescript
+    import "dotenv/config";
+    import { AzureOpenAI } from "openai";
+    import type {
+      ChatCompletion,
+      ChatCompletionCreateParamsNonStreaming,
+    } from "openai/resources/index";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-07-01-preview";
+    const deploymentName = "gpt-4-with-turbo";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    function createMessages(): ChatCompletionCreateParamsNonStreaming {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: [
+              {
+                type: "text",
+                text: "Describe this picture:",
+              },
+              {
+                type: "image_url",
+                image_url: {
+                  url: imageUrl,
+                },
+              },
+            ],
+          },
+        ],
+        model: "",
+        max_tokens: 2000,
+      };
+    }
+    async function printChoices(completion: ChatCompletion): Promise<void> {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      console.log("== Get GPT-4 Turbo with vision Sample ==");
+    
+      const client = getClient();
+      const messages = createMessages();
+      const completion = await client.chat.completions.create(messages);
+      await printChoices(completion);
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    ```
+1. Make the following changes:
+    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
+    1. Change the value of the `"url"` field to the URL of your image.
+        > [!TIP]
+        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node quickstart.js
+    ```
+
+
+## [**JavaScript**](#tab/javascript)
+
+1. Replace the contents of _quickstart.js_ with the following code. 
+    
+    ```javascript
+    import "dotenv/config";
+    import { AzureOpenAI } from "openai";
+    
+    // You will need to set these environment variables or edit the following values
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+    const imageUrl = process.env["IMAGE_URL"] || "<image url>";
+    
+    // Required Azure OpenAI deployment name and API version
+    const apiVersion = "2024-07-01-preview";
+    const deploymentName = "gpt-4-with-turbo";
+    
+    function getClient() {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        apiVersion,
+        deployment: deploymentName,
+      });
+    }
+    function createMessages() {
+      return {
+        messages: [
+          { role: "system", content: "You are a helpful assistant." },
+          {
+            role: "user",
+            content: [
+              {
+                type: "text",
+                text: "Describe this picture:",
+              },
+              {
+                type: "image_url",
+                image_url: {
+                  url: imageUrl,
+                },
+              },
+            ],
+          },
+        ],
+        model: "",
+        max_tokens: 2000,
+      };
+    }
+    async function printChoices(completion) {
+      for (const choice of completion.choices) {
+        console.log(choice.message);
+      }
+    }
+    export async function main() {
+      console.log("== Get GPT-4 Turbo with vision Sample ==");
+    
+      const client = getClient();
+      const messages = createMessages();
+      const completion = await client.chat.completions.create(messages);
+      await printChoices(completion);
+    }
+    
+    main().catch((err) => {
+      console.error("Error occurred:", err);
+    });
+    ```
+
+1. Make the following changes:
+    1. Enter the name of your GPT-4 Turbo with Vision deployment in the appropriate field.
+    1. Change the value of the `"url"` field to the URL of your image.
+        > [!TIP]
+        > You can also use a base 64 encoded image data instead of a URL. For more information, see the [GPT-4 Turbo with Vision how-to guide](../how-to/gpt-with-vision.md#use-a-local-image).
+1. Run the application with the following command:
+
+    ```console
+    node quickstart.js
+    ```
+
+---
+
+## Clean up resources
+
+If you want to clean up and remove an Azure OpenAI resource, you can delete the resource or resource group. Deleting the resource group also deletes any other resources associated with it.
+
+- [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
+- [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "JavaScript SDKを使用したGPT-4 Turbo with Visionのクイックスタートガイドの追加"
}
```

### Explanation
この変更は、OpenAI JavaScript SDKを使用してGPT-4 Turbo with Visionモデルを展開および利用するための新しいガイドを追加するものです。このガイドは、ユーザーが新しい機能を簡単に理解し、実装できるように設計されています。

新しい文書には、必要な前提条件としてAzureのサブスクリプション、Node.jsのLTSバージョン、TypeScriptのインストール、および対応するリージョンに作成されたAzure OpenAIリソースが含まれています。また、SDKのインストール方法や、画像のURLを指定してAIに指示を与える手順も詳述されています。

具体的には、ユーザーは環境変数を利用して必要な情報を設定し、サンプルコードを使って画像を説明するためのリクエストを作成します。さらに、TypeScriptとJavaScriptの両方のサンプルコードが含まれており、ユーザーは自分のニーズに応じて適切な言語を選択できます。

加えて、リソースのクリーンアップ方法についても言及されており、AzureにおけるOpenAIリソースの管理を容易にしています。このガイドは、ユーザーが迅速にGPT-4 Turbo with Visionを活用するための実用的な道筋を提供することを目指しています。

## articles/ai-services/openai/includes/use-your-data-javascript.md{#item-786699}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ author: glharper
 ms.author: glharper
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/04/2024
+ms.date: 09/06/2024
 ---
 
 [!INCLUDE [Set up required variables](./use-your-data-common-variables.md)]
@@ -23,81 +23,214 @@ npm init
 
 Install the Azure OpenAI client and Azure Identity libraries for JavaScript with npm:
 
+#### [TypeScript](#tab/typescript)
+
+```console
+npm install openai @azure/identity @azure/openai 
+```
+
+The `@azure/openai/types` dependency is included to extend the Azure OpenAI model for the `data_sources` property. This import is only necessary for TypeScript.
+
+#### [JavaScript](#tab/javascript)
+
 ```console
 npm install @azure/openai @azure/identity
 ```
 
+---
+
 Your app's _package.json_ file will be updated with the dependencies.
 
 ## Create a sample application
 
-Open a command prompt where you want the new project, and create a new file named ChatWithOwnData.js. Copy the following code into the ChatWithOwnData.js file.
-
-
-
-```javascript
-const { OpenAIClient, AzureKeyCredential } = require("@azure/openai");
-
-// Set the Azure and AI Search values from environment variables
-const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
-const azureApiKey = process.env["AZURE_OPENAI_API_KEY"];
-const deploymentId = process.env["AZURE_OPENAI_DEPLOYMENT_ID"];
-const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
-const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
-const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
-
-
-async function main(){
-  const client = new OpenAIClient(endpoint, new AzureKeyCredential(azureApiKey));
-
-  const messages = [
-    { role: "user", content: "What are my available health plans?" },
-  ];
-
-  console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);
-
-  const events = await client.streamChatCompletions(deploymentId, messages, { 
-    maxTokens: 128,
-    azureExtensionOptions: {
-      extensions: [
-        {
-          type: "AzureCognitiveSearch",
-          endpoint: searchEndpoint,
-          key: searchKey,
-          indexName: searchIndex,
-        },
-      ],
-    },
-  });
-  let response = "";
-  for await (const event of events) {
-    for (const choice of event.choices) {
-      const newText = choice.delta?.content;
-      if (!!newText) {
-        response += newText;
-        // To see streaming results as they arrive, uncomment line below
-        // console.log(newText);
+#### [TypeScript](#tab/typescript)
+
+1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.ts`. Copy the following code into the `ChatWithOwnData.ts` file.
+    
+    ```typescript
+    import "dotenv/config";
+    import { AzureOpenAI } from "openai";
+    import "@azure/openai/types";
+    
+    // Set the Azure and AI Search values from environment variables
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
+    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
+    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "gpt-4";
+    const apiVersion = "2024-07-01-preview";
+    
+    function getClient(): AzureOpenAI {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        deployment: deploymentName,
+        apiVersion,
+      });
+    }
+    
+    async function main() {
+      const client = getClient();
+    
+      const messages = [
+        { role: "user", content: "What are my available health plans?" },
+      ];
+    
+      console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);
+    
+      const events = await client.chat.completions.create({
+        stream: true,
+        messages: [
+          {
+            role: "user",
+            content:
+              "What's the most common feedback we received from our customers about the product?",
+          },
+        ],
+        max_tokens: 128,
+        model: "",
+        data_sources: [
+          {
+            type: "azure_search",
+            parameters: {
+              endpoint: searchEndpoint,
+              index_name: searchIndex,
+              authentication: {
+                type: "api_key",
+                key: searchKey,
+              },
+            },
+          },
+        ],
+      });
+    
+      let response = "";
+      for await (const event of events) {
+        for (const choice of event.choices) {
+          const newText = choice.delta?.content;
+          if (newText) {
+            response += newText;
+            // To see streaming results as they arrive, uncomment line below
+            // console.log(newText);
+          }
+        }
       }
+      console.log(response);
     }
-  }
-  console.log(response);
-}
-
-main().catch((err) => {
-  console.error("The sample encountered an error:", err);
-});
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
+
+1. Build the application with the following command:
+
+    ```console
+    tsc
+    ```
+
+1. Run the application with the following command:
+
+    ```console
+    node ChatWithOwnData.js
+    ```
+
+#### [JavaScript](#tab/javascript)
+
+1. Open a command prompt where you want the new project, and create a new file named `ChatWithOwnData.js`. Copy the following code into the `ChatWithOwnData.js` file.
+    
+    ```javascript
+    require("dotenv/config");
+    const { AzureOpenAI } = require("openai");
+    
+    // Set the Azure and AI Search values from environment variables
+    const endpoint = process.env["AZURE_OPENAI_ENDPOINT"];
+    const apiKey = process.env["AZURE_OPENAI_API_KEY"];
+    const searchEndpoint = process.env["AZURE_AI_SEARCH_ENDPOINT"];
+    const searchKey = process.env["AZURE_AI_SEARCH_API_KEY"];
+    const searchIndex = process.env["AZURE_AI_SEARCH_INDEX"];
+    
+    // Required Azure OpenAI deployment name and API version
+    const deploymentName = "gpt-4";
+    const apiVersion = "2024-07-01-preview";
+    
+    function getClient() {
+      return new AzureOpenAI({
+        endpoint,
+        apiKey,
+        deployment: deploymentName,
+        apiVersion,
+      });
+    }
+    
+    async function main() {
+      const client = getClient();
+    
+      const messages = [
+        { role: "user", content: "What are my available health plans?" },
+      ];
+    
+      console.log(`Message: ${messages.map((m) => m.content).join("\n")}`);
+    
+      const events = await client.chat.completions.create({
+        stream: true,
+        messages: [
+          {
+            role: "user",
+            content:
+              "What's the most common feedback we received from our customers about the product?",
+          },
+        ],
+        max_tokens: 128,
+        model: "",
+        data_sources: [
+          {
+            type: "azure_search",
+            parameters: {
+              endpoint: searchEndpoint,
+              index_name: searchIndex,
+              authentication: {
+                type: "api_key",
+                key: searchKey,
+              },
+            },
+          },
+        ],
+      });
+    
+      let response = "";
+      for await (const event of events) {
+        for (const choice of event.choices) {
+          const newText = choice.delta?.content;
+          if (newText) {
+            response += newText;
+            // To see streaming results as they arrive, uncomment line below
+            // console.log(newText);
+          }
+        }
+      }
+      console.log(response);
+    }
+    
+    main().catch((err) => {
+      console.error("The sample encountered an error:", err);
+    });
+    ```
 
+1. Run the application with the following command:
 
+    ```console
+    node ChatWithOwnData.js
+    ```
 
-module.exports = { main };
-```
+---
 
 > [!IMPORTANT]
 > For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information about credential security, see the Azure AI services [security](../../security-features.md) article.
 
-```cmd
-node.exe ChatWithOwnData.js
-```
 
 ## Output
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptでのデータ利用に関するガイドの更新"
}
```

### Explanation
この変更は、JavaScriptにおけるAzure OpenAIを使ったユーザーデータの利用に関するガイドを更新したものです。主な目的は、最新のライブラリの使用法や新機能を反映し、ユーザーが自身のデータを用いてAIモデルと対話する方法を明確に示すことです。

更新内容としては、新しい依存関係の追加や、TypeScriptとJavaScriptのための具体的なサンプルコードが含まれています。たとえば、環境変数からAzureのエンドポイントやAPIキーを取得する部分が改良され、さらにストリーミング応答を取り扱うコードが簡潔になっています。

具体的には、TypeScriptのサンプルでは、OpenAIライブラリに加えて`@azure/openai/types`をインポートするようになり、データソースを指定するための新しい機能が強調されています。また、エラーハンドリングや出力が整理され、コンソールに表示される情報がより分かりやすくなった点もポイントです。

最終的に、ユーザーはガイドに従って新しいプロジェクトを構築し、Azure Cognitive Searchを使用して特定のデータに基づいたChatGPTの応答を受け取ることができるようになります。この更新は、JavaScriptを使用したAzure OpenAIの利便性を高め、実際のプロジェクトでの利用を促進することを目指しています。

## articles/ai-services/openai/media/provisioned/confirm-pricing.png{#item-761d2a}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "価格確認のための画像の追加"
}
```

### Explanation
この変更は、価格確認に関する情報を示すための画像ファイル「confirm-pricing.png」を新たに追加するものです。この画像は、Azure OpenAIサービスに関連する価格の詳細や確認手順を視覚的にサポートするために使用されます。

画像が追加されることで、ユーザーが情報をより簡単に理解できるようになり、ドキュメントの視覚的な効果が向上します。このようなビジュアルコンテンツは、特に価格と構成に関連する複雑な情報を説明する際に、テキストだけでは伝わりにくい部分を補完する役割を果たします。

URLを通じて画像にアクセスできるため、ドキュメント内で参照されれば、ユーザーは具体的なビジュアルを確認しながら必要な情報を得ることができます。これは、特に価格設定やサービスの提供に関心のあるユーザーにとって、有益なリソースとなるでしょう。

## articles/ai-services/openai/media/provisioned/deployment-screen.png{#item-5bc2ef}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントスクリーン画像の更新"
}
```

### Explanation
今回の変更は、Azure OpenAIサービスに関連するデプロイメントスクリーンの画像「deployment-screen.png」を更新したものです。この変更により、最新の画面キャプチャやUIの変更が反映され、ユーザーに最新の情報を提供します。

画像の更新は、特にサービスや製品の使用方法を示す際に重要な役割を果たします。ユーザーは、実際の画面を参考にすることで、手順を理解しやすくなり、作業の正確性が向上します。デプロイメントに関するガイドラインやプロセスが視覚的に明確化されることにより、ユーザーが必要な操作を行う際の助けとなるでしょう。

インターネット上で画像にアクセスできるため、ドキュメント内での参照が容易で、必要に応じて簡単にチェックできる利便性も提供しています。このような更新は、ドキュメント全体の有用性を高め、ユーザーの体験を向上させるために重要です。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Use this article to import and use your data in Azure OpenAI.
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-go, devx-track-python
+ms.custom: devx-track-dotnet, devx-track-extended-java, devx-track-js, devx-track-ts, devx-track-go, devx-track-python
 ms.topic: quickstart
 author: aahill
 ms.author: aahi
@@ -24,7 +24,7 @@ zone_pivot_groups: openai-use-your-data
 
 ::: zone pivot="programming-language-javascript"
 
-[Reference](/javascript/api/@azure/openai) | [Source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai) | [Package (npm)](https://www.npmjs.com/package/@azure/openai) | [Samples](https://github.com/Azure/azure-sdk-for-net/blob/main/sdk/openai/Azure.AI.OpenAI/tests/Samples)
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 ::: zone-end
 
@@ -46,16 +46,35 @@ In this quickstart, you can use your own data with Azure OpenAI models. Using Az
 
 ## Prerequisites
 
+#### [TypeScript](#tab/typescript)
+
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+
 - An Azure OpenAI resource deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
 
-- Be sure that you are assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
+#### [JavaScript](#tab/javascript)
+
+- An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- An Azure OpenAI resource deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+
+- Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+
+---
+
 ::: zone pivot="programming-language-javascript"
 
+
+
 - [Long Term Support (LTS) versions of Node.js](https://github.com/nodejs/release#release-schedule)
 
 ::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドの内容更新"
}
```

### Explanation
この変更は、Azure OpenAIサービスに関する「自分のデータを使用するクイックスタート」ガイドを更新したもので、具体的にはいくつかの内容が追加および修正されています。主な変更点は以下の通りです。

1. **TypeScriptの追加**: これまでの説明にTypeScriptに関する情報が新たに追加され、TypeScriptユーザーに対する指示が明確になりました。
   
2. **参照リンクの更新**: JavaScriptに関する外部リンクが見直され、最新のソースコードやリファレンスドキュメントへのリンクが提供されるようになりました。これにより、読み手がより関連性の高い情報にアクセスできるようになります。

3. **コントリビューターロールの確認**: 「Cognitive Services Contributor」ロールについての説明が若干の文言修正を受けましたが、意図は変わっていません。

4. **データのダウンロードリンク**: サンプルデータの取得方法が再度明記され、自分のデータがないユーザーに対する具体的な指示が強化されました。

これらの変更により、ドキュメントはより包括的で、利用者がAzure OpenAIサービスを使用する際の理解と容易さが向上します。また、TypeScriptユーザーに向けた情報が追加された点は、幅広いプログラミング言語を使用するユーザーに配慮した重要な改訂です。全体として、ユーザーが必要な情報をより迅速に獲得できるようになることが目指されています。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -42,7 +42,7 @@ Request access: [limited access model application](https://aka.ms/oai/modelacces
 
 ### Limitations
 
-The `o1-preview` and `o1-mini` models are currently in preview and do not include some features available in other models, such as image understanding and structured outputs found in the GPT-4o and GPT-4o-mini models. For many tasks, the generally available GPT-4o models may still be more suitable.
+The `o1` series models are currently in preview and do not include some features available in other models, such as image understanding and structured outputs which are available in the latest GPT-4o model. For many tasks, the generally available GPT-4o models may still be more suitable.
 
 ### Safety
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "新機能ページの文言修正"
}
```

### Explanation
この変更は、Azure OpenAIサービスの「新機能」ページにおける文言の修正を含んでいます。具体的な変更点は以下の通りです。

1. **モデル名の修正**: `o1-preview`および`o1-mini`というモデル名が、より一般的な`o1`シリーズモデルに変更されました。これにより、ユーザーに対して最新のモデル名を適切に反映させています。

2. **機能に関する説明の更新**: 修正された文の中で、他のモデルに備わっている画像理解や構造化出力の機能が、最新のGPT-4oモデルに存在することが強調されています。これは、利用者に対して新しいモデルの機能に関する明確な情報を提供することを目的としています。

このようなマイナーな更新は、ドキュメントの正確性と明確性を向上させ、ユーザーがより適切な情報に基づいて判断や操作を行えるようにするために重要です。また、特定のモデル名の変更やその機能に対する説明の明確化は、今後の利用者が最新の情報を理解しやすくするための配慮がなされています。


