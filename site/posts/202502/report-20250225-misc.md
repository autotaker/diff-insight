---
date: '2025-02-25'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684
summary: 今回の変更では、いくつかの文書に対するマイナーな更新とバグ修正が行われました。これにより、内容の正確性と一貫性が向上しています。新たにAzure
  AI Studioのドキュメントにエンタープライズシナリオが追加され、特にポータルやゾーン設定の修正、説明の明確化が含まれています。破壊的な変更はなく、全体的な精度が向上するよう、さまざまな修正が施されています。これにより、ユーザーがAzureサービスをより容易に利用できるようにすることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8c6e364...MicrosoftDocs:50dc684){target="_blank"}

<format>
# ハイライト
今回の変更では、いくつかの文書に対するマイナーな更新およびバグ修正が行われ、内容の正確性と一貫性が向上しました。特に、ポータルやゾーン設定の修正、ドキュメントの説明の明確化、Azure AI Studioにおける新たな使用シナリオの追加が含まれています。

## 新機能
- Azure AI Studioのドキュメントにおける新しいエンタープライズシナリオの追加。

## 破壊的変更
- 破壊的な変更はありませんでした。

## その他の更新
- 精度と信頼スコアに関する表現と説明の修正。
- Java SDKのコード内でセミコロンの削除によるバグ修正。
- Azure AI Documentationのポータルリンクの修正。
- モデルライフサイクル情報の更新。
- クイックスタートガイドの手順と目次の更新。

# インサイト
この一連の更新は、Azureに関連する技術文書の整合性とユーザーフレンドリーさを高めることを目的としています。

まず、`精度と信頼スコア`のドキュメントにおける文言の変更は、ユーザーがより具体的な情報を把握しやすくするための工夫です。特に、技術的な用語を平易な表現に統一することで、エキスパートだけでなく、より広いユーザー層に訴求しています。

Java SDKのコード修正はバグフィックスと可読性向上が狙いであり、特にメソッド呼び出し部分の余分なセミコロンを削除することでエラーの防止を図っっています。

各サービスのクイックスタートガイドでは、ポータルの設定が更新され、ユーザーがコンテンツを見つけやすくアクセスしやすくなるよう調整されています。これにより、関連リソースへのアクセス性が向上し、ユーザーエクスペリエンスが改善されます。

AIスタジオのモデルライフサイクル情報では、Cohere社の引退モデルに関する具体的なスケジュールが追加され、ユーザーがモデル変更に対して準備ができるようになっています。

Azure AI Studioドキュメントでは、特にファインチューニングに関するセクションでエンタープライズシナリオが追加され、実用面での活用がしやすい構成となっています。これは、エンタープライズユーザーに向け、拡張された利用シナリオを提供することで、実務への適用を促進します。

こうした改善は、ドキュメントの精度と利便性を高め、ユーザーがより容易にAzureサービスを利用し、技術的な問題に対処するための道標として機能することを意図しています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [accuracy-confidence.md](#item-56cda7) | minor update | 精度と信頼スコアの解釈と改善 | modified | 4 | 4 | 8 | 
| [java-sdk.md](#item-65f910) | bug fix | Java SDKのコード修正 | modified | 2 | 2 | 4 | 
| [quickstart.md](#item-a6bafe) | minor update | Azure AI Foundryポータルのピボット修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-636553) | minor update | 言語検出クイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-c084f9) | minor update | 固有表現認識クイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-94affd) | minor update | 本人確認情報クイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-8c5758) | minor update | センチメント分析クイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-bff856) | minor update | 要約サービスクイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-9b06f2) | minor update | ヘルスケア向けテキスト分析クイックスタートのポータル修正 | modified | 1 | 1 | 2 | 
| [model-lifecycle-retirement.md](#item-f0fc21) | minor update | モデルライフサイクルの引退に関する情報の追加 | modified | 2 | 0 | 2 | 
| [configure-managed-network.md](#item-dc9c50) | minor update | 管理されたネットワークの構成ガイドの修正 | modified | 23 | 17 | 40 | 
| [fine-tune-serverless.md](#item-ce4817) | minor update | ファインチューニングに関するエンタープライズシナリオの追加 | modified | 26 | 0 | 26 | 
| [install-cli.md](#item-868060) | minor update | Azure CLI インストールガイドの更新 | modified | 3 | 0 | 3 | 
| [get-started-code.md](#item-8a5082) | minor update | クイックスタートガイドの内容更新 | modified | 8 | 4 | 12 | 
| [toc.yml](#item-2745cd) | minor update | 目次の内容更新 | modified | 3 | 1 | 4 | 
| [copilot-sdk-create-resources.md](#item-552960) | minor update | チュートリアルの手順更新 | modified | 8 | 3 | 11 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/accuracy-confidence.md{#item-56cda7}

<details>
<summary>Diff</summary>
````diff
@@ -1,18 +1,18 @@
 ---
-title:  Interpret and improve model accuracy and analysis confidence scores
+title:  Interpret and improve model accuracy and confidence scores
 titleSuffix: Azure AI services
-description: Best practices to interpret the accuracy score from the train model operation and the confidence score from analysis operations.
+description: Best practices to interpret and improve Azure AI Document Intelligence accuracy scores from train model operations and confidence scores from analysis operations.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
-ms.date: 11/19/2024
+ms.date: 02/21/2025
 ms.author: lajanuar
 ---
 
 <!-- markdownlint-disable MD033 -->
 
-# Interpret and improve model accuracy and analysis confidence scores
+# Interpret and improve accuracy and confidence scores
 
 A confidence score indicates probability by measuring the degree of statistical certainty that the extracted result is detected correctly. The estimated accuracy is calculated by running a few different combinations of the training data to predict the labeled values. In this article, learn to interpret accuracy and confidence scores and best practices for using those scores to improve accuracy and confidence results.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "精度と信頼スコアの解釈と改善"
}
```

### Explanation
この変更は、ドキュメントのタイトルと説明を更新し、精度スコアと信頼スコアに関連する内容を明確に活用できるようにしています。具体的には、タイトルから「モデル」という言葉を削除し、「分析信頼スコア」という表現を「信頼スコア」に簡略化しています。また、説明文では、Azure AI Document Intelligenceの訓練モデル操作からの精度スコアと分析操作からの信頼スコアを強調し、改善のためのベストプラクティスを明示しています。さらに、文書の更新日も2024年から2025年に変更されました。全体として、ユーザーにとってより具体的で役立つ情報が提供されることを目指した更新です。

## articles/ai-services/document-intelligence/how-to-guides/includes/v4-0/java-sdk.md{#item-65f910}

<details>
<summary>Diff</summary>
````diff
@@ -177,7 +177,7 @@ String documentUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-
 String modelId = "prebuilt-read";
 
 SyncPoller < OperationResult, AnalyzeResult > analyzeLayoutResultPoller =
-  client.beginAnalyzeDocument(modelId, invoiceUrl);;
+  client.beginAnalyzeDocument(modelId, invoiceUrl);
 
 AnalyzeResult analyzeLayoutResult = analyzeLayoutResultPoller.getFinalResult().getAnalyzeResult();
 
@@ -338,7 +338,7 @@ String modelId = "prebuilt-document";
 SyncPoller < OperationResult, AnalyzeResult > analyzeDocumentPoller =
   client.beginAnalyzeDocument(modelId, generalDocumentUrl);
 
-AnalyzeResult analyzeResult = analyzeDocumentPoller.getFinalResult().getAnalyzeResult();;
+AnalyzeResult analyzeResult = analyzeDocumentPoller.getFinalResult().getAnalyzeResult();
 
 // pages
 analyzeResult.getPages().forEach(documentPage -> {
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "Java SDKのコード修正"
}
```

### Explanation
この変更は、Java SDKに関するドキュメント内のコードの小さな修正を行っています。具体的には、`beginAnalyzeDocument`メソッドと`getFinalResult`メソッドの呼び出し部分から余分なセミコロンを削除しました。この変更により、コードの正確性と可読性が向上し、使用者がこれらのメソッドを正しく理解し、利用できるようになります。全体として、この修正はプログラムのエラーを防ぎ、コードの実行が期待通りに機能するようにするためのものです。

## articles/ai-services/language-service/key-phrase-extraction/quickstart.md{#item-a6bafe}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryポータルのピボット修正"
}
```

### Explanation
この変更は、Azure AI Documentationにおけるクイックスタートガイドの一部で、特定のゾーン設定に関連する修正を行っています。具体的には、`zone pivot`の属性値を`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更しました。この修正により、ユーザーは正しいポータルに関連づけられた情報を参照できるようになります。この変更は、文書の一貫性を保ち、ユーザーが正確なリソースにアクセスできるようにするための重要な更新です。

## articles/ai-services/language-service/language-detection/quickstart.md{#item-636553}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語検出クイックスタートのポータル修正"
}
```

### Explanation
この変更は、言語サービスのクイックスタートガイドにおけるゾーン設定の修正を表しています。具体的には、`zone pivot`の属性値を`"azure-ai-foundry"`から`"ai-foundry-portal"`に更新しました。この修正により、資料が正確なポータルにリンクされ、ユーザーが適切なリソースを使用できるようになります。この変更は、文書の整合性を保ちつつ、ユーザーが必要とする情報に確実にアクセスできることを目的としています。

## articles/ai-services/language-service/named-entity-recognition/quickstart.md{#item-c084f9}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "固有表現認識クイックスタートのポータル修正"
}
```

### Explanation
この変更は、固有表現認識のクイックスタートガイドに関連しており、ゾーン設定の修正が行われました。具体的には、`zone pivot`の値を`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更しました。この修正により、文書が正しいポータルにリンクされ、ユーザーは最新のリソースに簡単にアクセスできるようになります。この変更は、Azure AI Documentation の整合性と正確性を向上させるための小規模な更新です。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -50,7 +50,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "本人確認情報クイックスタートのポータル修正"
}
```

### Explanation
この変更は、本人確認情報に関するクイックスタートガイドのゾーン設定を修正するものです。具体的には、`zone pivot`の値を`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更しました。この更新により、ユーザーは適切なポータルへのリンクを得られ、関連するリソースへ簡単にアクセスできるようになります。この修正は、ドキュメントの正確性を維持するための小規模な更新です。

## articles/ai-services/language-service/sentiment-opinion-mining/quickstart.md{#item-8c5758}

<details>
<summary>Diff</summary>
````diff
@@ -48,7 +48,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "センチメント分析クイックスタートのポータル修正"
}
```

### Explanation
この変更は、センチメント分析に関するクイックスタートガイドにおけるゾーンの設定を修正しています。具体的には、`zone pivot`の設定を`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更しました。この変更により、ユーザーが正しいポータルにアクセスできるようになり、関連するリソースをより簡単に見つけることができるようになります。この修正は、ドキュメントの整合性を高めるための小規模な更新です。

## articles/ai-services/language-service/summarization/quickstart.md{#item-bff856}

<details>
<summary>Diff</summary>
````diff
@@ -49,7 +49,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "要約サービスクイックスタートのポータル修正"
}
```

### Explanation
この変更は、要約サービスに関するクイックスタートガイドにおいて、ゾーンの設定を修正したものです。具体的には、`zone pivot`の値を`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更しました。この修正により、ユーザーが適切なポータルにアクセスできるようになり、必要なリソースをより簡単に見つけることができるようになります。全体として、この更新はドキュメントの正確性を向上させるための小規模な修正です。

## articles/ai-services/language-service/text-analytics-for-health/quickstart.md{#item-9b06f2}

<details>
<summary>Diff</summary>
````diff
@@ -51,7 +51,7 @@ This article contains Text Analytics for health quickstarts that help with using
 
 ::: zone-end
 
-::: zone pivot="azure-ai-foundry"
+::: zone pivot="ai-foundry-portal"
 
 [!INCLUDE [Azure AI Foundry quickstart](includes/quickstarts/azure-ai-foundry.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ヘルスケア向けテキスト分析クイックスタートのポータル修正"
}
```

### Explanation
この変更は、ヘルスケア向けテキスト分析に関するクイックスタートガイドの中で、ゾーンの設定を修正したものです。具体的には、`zone pivot`の値が`"azure-ai-foundry"`から`"ai-foundry-portal"`に変更されました。この変更は、ユーザーが正しいポータルにアクセスできるようにし、関連する資源を効率的に探し出す手助けをします。この修正は、ドキュメントの整合性を向上させるための小さな更新です。

## articles/ai-studio/concepts/model-lifecycle-retirement.md{#item-f0fc21}

<details>
<summary>Diff</summary>
````diff
@@ -68,6 +68,8 @@ The following table lists the timelines for models that are on track for retirem
 | Model provider | Model | Legacy date (UTC) | Deprecation date (UTC) | Retirement date (UTC) | Suggested replacement model |
 | ---- | ---- | ---- | --- | ---- | --- |
 | AI21 Labs | Jamba Instruct | February 1, 2025 | February 1, 2025 | March 1, 2025 | [AI21-Jamba-1.5-Large](https://ai.azure.com/explore/models/AI21-Jamba-1.5-Large/version/1/registry/azureml-ai21) or [AI21-Jamba-1.5-Mini](https://ai.azure.com/explore/models/AI21-Jamba-1.5-Mini/version/1/registry/azureml-staging) |
+| Cohere | [Command R](https://aka.ms/azureai/landing/Cohere-command-r) | February 24, 2025 | March 25, 2025 | June 30, 2025 | [Cohere Command R 08-2024](https://aka.ms/azureai/landing/Cohere-command-r-08-2024) |
+| Cohere | [Command R+](https://aka.ms/azureai/landing/Cohere-command-r-plus) | February 24, 2025 | March 25, 2025 | June 30, 2025 | [Cohere Command R+ 08-2024](https://aka.ms/azureai/landing/Cohere-command-r-plus-08-2024) |
 | Mistral AI | [Mistral-large-2407](https://aka.ms/azureai/landing/Mistral-Large-2407) | January 13, 2025 | February 13, 2025 | May 13, 2025 | [Mistral-large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411) |
 | Mistral AI | [Mistral-large](https://aka.ms/azureai/landing/Mistral-Large) | December 15, 2024 | January 15, 2025 | April 15, 2025 | [Mistral-large-2411](https://aka.ms/aistudio/landing/Mistral-Large-2411) |
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルの引退に関する情報の追加"
}
```

### Explanation
この変更は、AIスタジオのモデルライフサイクルの引退に関するドキュメントに新たな情報を追加したものです。具体的には、Cohere社のモデル`Command R`および`Command R+`の引退スケジュールが新たに追加されました。これにより、それぞれのモデルの引退日、廃止日の詳細と、推奨される代替モデルへのリンクが提供されています。この更新により、ユーザーはモデルの引退に関する最新情報を認識し、適切な代替案を選ぶことが容易になります。全体として、これはドキュメントの有用性を向上させるための小規模な更新です。

## articles/ai-studio/how-to/configure-managed-network.md{#item-dc9c50}

<details>
<summary>Diff</summary>
````diff
@@ -1,23 +1,26 @@
 ---
-title: How to configure a managed network for Azure AI Foundry hubs
+title: How to configure a managed network
 titleSuffix: Azure AI Foundry
-description: Learn how to configure a managed network for Azure AI Foundry hubs.
+description: Learn how to configure a managed network for Azure AI Foundry hubs. A managed network secures your computing resources.
 manager: scottpolly
 ms.service: azure-ai-foundry
 ms.custom: ignite-2023, build-2024, devx-track-azurecli, ignite-2024
 ms.topic: how-to
-ms.date: 11/19/2024
+ms.date: 02/24/2025
 ms.reviewer: meerakurup
 ms.author: larryfr
 author: Blackmist
 zone_pivot_groups: azure-ai-studio-sdk-cli
+
+#Customer intent: As an administrator, I want to configure a managed network for Azure AI Foundry hubs so that my computing resources are protected.
+
 ---
 
 # How to configure a managed network for Azure AI Foundry hubs
 
 We have two network isolation aspects. One is the network isolation to access an [Azure AI Foundry](https://ai.azure.com) hub. Another is the network isolation of computing resources for both your hub and project (such as compute instance, serverless and managed online endpoint.) This document explains the latter highlighted in the diagram. You can use hub built-in network isolation to protect your computing resources.
 
-:::image type="content" source="../media/how-to/network/azure-ai-network-outbound.svg" alt-text="Diagram of hub network isolation." lightbox="../media/how-to/network/azure-ai-network-outbound.png":::
+:::image type="content" source="../media/how-to/network/azure-ai-network-outbound.svg" alt-text="Diagram of hub network isolation configuration with Azure AI Foundry." lightbox="../media/how-to/network/azure-ai-network-outbound.png":::
 
 You need to configure following network isolation configurations.
 
@@ -54,10 +57,13 @@ The following diagram shows a managed virtual network configured to __allow inte
 The following diagram shows a managed virtual network configured to __allow only approved outbound__:
 
 > [!NOTE]
-> In this configuration, the storage, key vault, and container registry used by the hub are flagged as private. Since they are flagged as private, a private endpoint is used to communicate with them.
+> In this configuration, the storage, key vault, and container registry used by the hub are flagged as private. Since they're flagged as private, a private endpoint is used to communicate with them.
 
 :::image type="content" source="../media/how-to/network/only-approved-outbound.svg" alt-text="Diagram of managed virtual network isolation configured for allow only approved outbound." lightbox="../media/how-to/network/only-approved-outbound.png":::
 
+> [!NOTE]
+> When you're accessing a private storage account from a public AI Foundry hub, you must access AI Foundry from within the virtual network of your storage account. Accessing AI Foundry from within the virtual network ensures that you can call actions such as upload files to the private storage account. The private storage account is independent of your AI Foundry hub's networking settings. For more on setting your private storage accounts virtual network, see [Configure Azure Storage firewalls and virtual networks](/azure/storage/common/storage-network-security).
+
 ## Prerequisites
 
 Before following the steps in this article, make sure you have the following prerequisites:
@@ -135,7 +141,7 @@ Before following the steps in this article, make sure you have the following pre
 
 ## Limitations
 
-* Azure AI Foundry supports managed virtual network isolation for securing your compute resources. Azure AI Foundry does not support bring your own virtual network for securing compute resources. Please note bring your own virtual network for securing computes is different than your Azure virtual network that is required to access Azure AI Foundry from your on-premises network. 
+* Azure AI Foundry supports managed virtual network isolation for securing your compute resources. Azure AI Foundry doesn't support bring your own virtual network for securing compute resources. Note that bringing your own virtual network for securing computes is different than your Azure virtual network that is required to access Azure AI Foundry from your on-premises network. 
 * Once you enable managed virtual network isolation of your Azure AI, you can't disable it.
 * Managed virtual network uses private endpoint connection to access your private resources. You can't have a private endpoint and a service endpoint at the same time for your Azure resources, such as a storage account. We recommend using private endpoints in all scenarios.
 * The managed virtual network is deleted when the Azure AI is deleted. 
@@ -149,14 +155,14 @@ Before following the steps in this article, make sure you have the following pre
 ## Configure a managed virtual network to allow internet outbound
 
 > [!TIP]
-> The creation of the managed VNet is deferred until a compute resource is created or provisioning is manually started. When allowing automatic creation, it can take around __30 minutes__ to create the first compute resource as it is also provisioning the network.
+> The creation of the managed virtual network is deferred until a compute resource is created or provisioning is manually started. When allowing automatic creation, it can take around __30 minutes__ to create the first compute resource as it is also provisioning the network.
 
 # [Azure portal](#tab/portal)
 
 * __Create a new hub__:
 
     1. Sign in to the [Azure portal](https://portal.azure.com), and choose Azure AI Foundry from Create a resource menu.
-    1. Select **+ New Azure AI**.
+    1. Select __+ New Azure AI__.
     1. Provide the required information on the __Basics__ tab.
     1. From the __Networking__ tab, select __Private with Internet Outbound__.
     1. To add an _outbound rule_, select __Add user-defined outbound rules__ from the __Networking__ tab. From the __Outbound rules__ sidebar, provide the following information:
@@ -332,14 +338,14 @@ To configure a managed virtual network that allows internet outbound communicati
 ## Configure a managed virtual network to allow only approved outbound
 
 > [!TIP]
-> The managed VNet is automatically provisioned when you create a compute resource. When allowing automatic creation, it can take around __30 minutes__ to create the first compute resource as it is also provisioning the network. If you configured FQDN outbound rules, the first FQDN rule adds around __10 minutes__ to the provisioning time.
+> The managed virtual network is automatically provisioned when you create a compute resource. When allowing automatic creation, it can take around __30 minutes__ to create the first compute resource as it is also provisioning the network. If you configured FQDN outbound rules, the first FQDN rule adds around __10 minutes__ to the provisioning time.
 
 # [Azure portal](#tab/portal)
 
 * __Create a new hub__:
 
     1. Sign in to the [Azure portal](https://portal.azure.com), and choose Azure AI Foundry from Create a resource menu.
-    1. Select **+ New Azure AI**.
+    1. Select __+ New Azure AI__.
     1. Provide the required information on the __Basics__ tab.
     1. From the __Networking__ tab, select __Private with Approved Outbound__.
 
@@ -624,7 +630,7 @@ To reduce the wait time and avoid potential timeout errors, we recommend manuall
 Alternatively, you can use the `provision_network_now` flag to provision the managed network as part of hub creation. This flag is in preview.
 
 > [!NOTE]
-> To create an online deployment, you must manually provision the managed network, or create a compute instance first which will automatically provision it. 
+> To create an online deployment, you must manually provision the managed network, or create a compute instance first. Creating a compute instance automatically provision it. 
 
 # [Azure portal](#tab/portal)
 
@@ -644,7 +650,7 @@ The following example shows how to provision a managed virtual network.
 az ml workspace provision-network -g my_resource_group -n my_ai_hub_name
 ```
 
-To verify that the provisioning has completed, use the following command:
+To verify that the provisioning completed, use the following command:
 
 ```azurecli
 az ml workspace show -n my_ai_hub_name -g my_resource_group --query managed_network
@@ -667,7 +673,7 @@ ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group,
 provision_network_result = ml_client.workspaces.begin_provision_network(workspace_name=ai_hub_name).result()
 ```
 
-To verify that the AI Hub has been provisioned, use `ml_client.workspaces.get()` to get the AI Hub information. The `managed_network` property contains the status of the managed network.
+To verify the AI provisioning, use `ml_client.workspaces.get()` to get the AI Hub information. The `managed_network` property contains the status of the managed network.
 
 ```python
 ws = ml_client.workspaces.get()
@@ -761,7 +767,7 @@ __Inbound__ service tag rules:
 To allow installation of __Python packages for training and deployment__, add outbound _FQDN_ rules to allow traffic to the following host names:
 
 > [!NOTE]
-> This is not a complete list of the hosts required for all Python resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario.
+> This isn't a complete list of the hosts required for all Python resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario.
 
 | __Host name__ | __Purpose__ |
 | ---- | ---- |
@@ -779,7 +785,7 @@ Visual Studio Code relies on specific hosts and ports to establish a remote conn
 The hosts in this section are used to install Visual Studio Code packages to establish a remote connection between Visual Studio Code and the compute instances for your project.
 
 > [!NOTE]
-> This is not a complete list of the hosts required for all Visual Studio Code resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario. For a complete list of host names, see [Network Connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network).
+> This isn't a complete list of the hosts required for all Visual Studio Code resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario. For a complete list of host names, see [Network Connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network).
 
 | __Host name__ | __Purpose__ |
 | ---- | ---- |
@@ -847,7 +853,7 @@ When you create a private endpoint for hub dependency resources, such as Azure S
 A private endpoint is automatically created for a connection if the target resource is an Azure resource listed previously. A valid target ID is expected for the private endpoint. A valid target ID for the connection can be the Azure Resource Manager ID of a parent resource. The target ID is also expected in the target of the connection or in `metadata.resourceid`. For more on connections, see [How to add a new connection in Azure AI Foundry portal](connections-add.md).
 
 > [!IMPORTANT]
-> As of March 31st 2025, the Azure AI Enterprise Network Connection Approver role must be assigned to the Azure AI Foundry hub's managed identity to approve private endpoints to securely access your Azure resources from the managed virtual network. This does not impact existing resources with approved private endpoints as the role is correctly assigned by the service. For new resources, please ensure the role is assigned to the hub's managed identity. For Azure Data Factory, Azure Databricks, and Azure Function Apps, the Contributor role should instead be assigned to your hub's managed identity. This role assignment is applicable to both User-assigned identity and System-assigned identity workspaces. 
+> As of March 31st 2025, the Azure AI Enterprise Network Connection Approver role must be assigned to the Azure AI Foundry hub's managed identity to approve private endpoints to securely access your Azure resources from the managed virtual network. This doesn't impact existing resources with approved private endpoints as the role is correctly assigned by the service. For new resources, please ensure the role is assigned to the hub's managed identity. For Azure Data Factory, Azure Databricks, and Azure Function Apps, the Contributor role should instead be assigned to your hub's managed identity. This role assignment is applicable to both User-assigned identity and System-assigned identity workspaces. 
 
 ## Select an Azure Firewall version for allowed only approved outbound (Preview)
 
@@ -899,7 +905,7 @@ The hub managed virtual network feature is free. However, you're charged for the
 * FQDN outbound rules - FQDN outbound rules are implemented using Azure Firewall. If you use outbound FQDN rules, charges for Azure Firewall are included in your billing. A standard version of Azure Firewall is used by default. For information on selecting the basic version, see [Select an Azure Firewall version](#select-an-azure-firewall-version-for-allowed-only-approved-outbound-preview). Azure Firewall is provisioned per hub.
 
     > [!IMPORTANT]
-    > The firewall isn't created until you add an outbound FQDN rule. If you don't use FQDN rules, you will not be charged for Azure Firewall. For more information on pricing, see [Azure Firewall pricing](https://azure.microsoft.com/pricing/details/azure-firewall/).
+    > The firewall isn't created until you add an outbound FQDN rule. If you don't use FQDN rules, you won't be charged for Azure Firewall. For more information on pricing, see [Azure Firewall pricing](https://azure.microsoft.com/pricing/details/azure-firewall/).
 
 ## Related content
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "管理されたネットワークの構成ガイドの修正"
}
```

### Explanation
この変更は、Azure AI Foundryのハブに対する管理されたネットワークの構成に関するドキュメントを更新したものです。主な改訂点には、文書のタイトルと説明が簡素化され、より具体的な内容が追加されたことが含まれています。また、図の説明が明確になり、関連する注意書きとヒントが整理されました。特に、プライベートストレージアカウントにアクセスするための要件や、管理されたネットワークのプロビジョニングに関する詳細が強調されています。これにより、ユーザーはネットワーク設定をより適切に行うことができるようになり、全体的な内容の理解が向上しています。

## articles/ai-studio/how-to/fine-tune-serverless.md{#item-ce4817}

<details>
<summary>Diff</summary>
````diff
@@ -154,6 +154,32 @@ The supported file type is JSON Lines. Files are uploaded to the default datasto
 
 Once your model is fine-tuned, you can deploy it and use it in your own application, in the playground, or in prompt flow. For more information on how to use deployed models, see [How to use Mistral premium chat models](./deploy-models-mistral.md).
 
+---
+## Supported enterprise scenarios for finetuning
+
+Several enterprise scenarios are supported for MaaS finetuning. The table below outlines the supported configurations for user storage networking and authentication to ensure smooth operation within enterprise scenarios:
+
+>[!Note]  
+>- Data connections auth can be changed via AI Studio by clicking on the datastore connection which your dataset is stored in, and navigating to the **Access details** > **Authentication Method** setting.  
+>- Storage auth can be changed in Azure Storage > **Settings** > **Configurations** page > **Allow storage account key access**.  
+>- Storage networking can be changed in Azure Storage > **Networking** page.
+
+| **Storage Networking**                                       |  **Storage Auth**               | **Data Connection Auth**               | **Support**           |
+| ------------------------------------------------------------ | ------------------------------ | --------------------------------- | ----------------------- |
+| Public Network Access = Enabled                               | Account key enabled            | SAS/Account Key                  | Yes, UX and SDK         |
+| Public Network Access = Enabled                               | Account key disabled           | Entra-Based Auth (Credentialless) | Yes, UX and SDK <br><br> *Note:* for UX, you may need to add Storage Blob Data Reader or Storage Blob Data Contributor for your user ID on the storage account, or change the connection's authentication to use Account key/SAS token |                               |                                   |                         |
+| Enabled from selected virtual networks and IP addresses      | Account key enabled            | Account key                      | Yes, UX and SDK <br><br> *Note:*: for UX, the IP of the compute running the browser must be in the selected list        |
+| Enabled from selected virtual networks and IP addresses      | Account key enabled            | SAS                               | Yes, UX and SDK  <br><br> *Note:*: for UX, the IP of the compute running the browser must be in the selected list       |
+| Enabled from selected virtual networks and IP addresses      | Account key disabled           | Entra-Based Auth (Credentialless) | Yes, UX and SDK. <br><br>*Note:* for UX, you may need to add Storage Blob Data Reader or Storage Blob Data Contributor for your user ID on the storage account, or change the connection's authentication to use Account key/SAS token. Also ensure the IP of the compute running the browser must be in the selected list |                               |                                   |                         |
+| Public Network Access = Disabled                              | Account key enabled            | SAS/Account Key                  | Yes, UX and SDK. <br><br> *Note:*  for UX data upload and submission to work, the workspace _needs to be accessed from within the Vnet_ that has appropriate access to the storage           |
+| Public Network Access = Disabled                              | Account key disabled           | Entra-Based Auth (Credentialless) | Yes, UX and SDK. <br><br> *Note:* for UX data upload and submission to work, the workspace _needs to be accessed from within the Vnet_ that has appropriate access to the storage                |
+
+
+The scenarios above should work in a Managed Vnet workspace as well. See setup of Managed Vnet AI Studio hub here: [How to configure a managed network for Azure AI Foundry hubs](./configure-managed-network.md)
+
+Customer-Managed Keys (CMKs) is **not** a supported enterprise scenario with MaaS finetuning.
+
+Issues finetuning with unique network setups on the workspace and storage usually points to a networking setup issue.
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ファインチューニングに関するエンタープライズシナリオの追加"
}
```

### Explanation
この変更は、サーバーレス環境でのモデルファインチューニングに関するドキュメントに新しいセクションを追加したものです。追加された内容には、MaaS（Model as a Service）ファインチューニングに対応するいくつかのエンタープライズシナリオが含まれており、各シナリオにはストレージネットワーキングや認証に関する詳細が示されています。具体的には、パブリックネットワークアクセスやストレージ認証方法についての設定オプションが表形式で説明されています。また、特に注意が必要な点や、データ接続の認証方法を変更する手順についても記載されています。この更新により、ユーザーはエンタープライズ環境におけるファインチューニングの設定とその制約を理解しやすくなります。さらに、Customer-Managed Keys（CMKs）はサポートされていないことも明記されています。これによって、ネットワーク設定に起因する問題の診断が容易になることが期待されます。

## articles/ai-studio/includes/install-cli.md{#item-868060}

<details>
<summary>Diff</summary>
````diff
@@ -13,6 +13,7 @@ ms.custom: include, ignite-2024
 You install the Azure CLI and sign in from your local development environment, so that you can use your user credentials to call the Azure OpenAI service.
 
 In most cases you can install the Azure CLI from your terminal using the following command: 
+
 # [Windows](#tab/windows)
 
 ```powershell 
@@ -36,9 +37,11 @@ brew update && brew install azure-cli
 You can follow instructions [How to install the Azure CLI](/cli/azure/install-azure-cli) if these commands don't work for your particular operating system or setup.
 
 After you install the Azure CLI, sign in using the ``az login`` command and sign-in using the browser:
+
 ```
 az login
 ```
+
 Alternatively, you can log in manually via the browser with a device code.
 ```
 az login --use-device-code
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure CLI インストールガイドの更新"
}
```

### Explanation
この変更は、Azure CLIのインストールに関するドキュメントを微修正したものです。具体的には、利用可能なログイン方法を明示するために、Windows用のタブを追加し、CLIのインストール後に実行する``az login``コマンドの具体的な記述が強調されています。さらに、デバイスコードを使用した手動ログイン方法の説明も加わりました。この更新により、ユーザーは自分の環境に適した手順をより明確に理解し、Azure OpenAIサービスにアクセスできるようになります。全体として、この変更はCLIのインストールとログインプロセスをより簡便にすることを目的としています。

## articles/ai-studio/quickstarts/get-started-code.md{#item-8a5082}

<details>
<summary>Diff</summary>
````diff
@@ -22,12 +22,10 @@ In this quickstart, we walk you through setting up your local development enviro
 
 * Before you can follow this quickstart, complete the [Azure AI Foundry playground quickstart](../quickstarts/get-started-playground.md) to deploy a **gpt-4o-mini** model into a project.
 
-## Install the Azure CLI and sign in 
-
-[!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
-
 ## Create a new Python environment
 
+In the IDE of your choice, create a new folder for your project.  Open a terminal window in that folder.
+
 [!INCLUDE [Install Python](../includes/install-python.md)]
 
 ## Install packages
@@ -38,6 +36,12 @@ Install `azure-ai-projects`(preview), `azure-ai-inference` (preview), and azure-
 pip install azure-ai-projects azure-ai-inference azure-identity 
 ```
 
+## Install the Azure CLI and sign in 
+
+[!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
+
+Keep this terminal window open to run your python scripts from here as well, now that you've signed in.
+
 ## Build your chat app
 
 Create a file named **chat.py**.  Copy and paste the following code into it.
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
この変更は、Azure AI Studioのクイックスタートガイドに関する文書を更新したもので、手順の順序や具体的な内容を変更しています。特に、Azure CLIのインストールとサインインに関するセクションが、プログラムの実行環境を整えるプロセスの最後に移動され、これによりユーザーはPythonスクリプトを実行する際のターミナルを開いたままにしておくことができるようになりました。

また、プロジェクトの設定手順がより明確になっており、ローカル開発環境の準備がスムーズになるように調整されています。この更新によって、ユーザーが必要なツールを適切なタイミングでインストールし、設定を行うことができるため、全体の体験が改善されます。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -384,7 +384,9 @@ items:
     items:
     - name: Fine-tuning in Azure AI Foundry
       href: concepts/fine-tuning-overview.md
-    - name: Fine-tune with a managed compute
+    - name: Fine-tune models deployed via serverless API
+      href: how-to/fine-tune-serverless.md
+    - name: Fine-tune models deployed via managed compute
       href: how-to/fine-tune-managed-compute.md
     - name: Fine-tune Azure OpenAI models
       href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次の内容更新"
}
```

### Explanation
この変更は、Azure AI Studioの目次ファイル（toc.yml）に対して行われたもので、ファインチューニングに関連する項目の名称とリンクを更新しています。具体的には、「管理されたコンピュートでのファインチューニング」という項目の名称が、「サーバーレスAPI経由でデプロイしたモデルのファインチューニング」に変更され、新たにこの手法に関するリンクが追加されました。

さらに、管理されたコンピュートを使用したファインチューニングに関する項目も残されており、ユーザーがそれぞれの方法について詳細な情報を得られるようになっています。この更新により、情報の整理が進み、ユーザーが必要なリソースにアクセスしやすくなることが期待されます。

## articles/ai-studio/tutorials/copilot-sdk-create-resources.md{#item-552960}

<details>
<summary>Diff</summary>
````diff
@@ -110,12 +110,11 @@ In the Azure AI Foundry portal, check for an Azure AI Search connected resource.
 
 1. Select **Add connection**.  
 
-## <a name="installs"></a> Install the Azure CLI and sign in 
-
-[!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
 
 ## Create a new Python environment
 
+In the IDE of your choice, create a new folder for your project.  Open a terminal window in that folder.
+
 [!INCLUDE [Install Python](../includes/install-python.md)]
 
 ## Install packages
@@ -145,6 +144,12 @@ Create a folder for your work. Create a file called **config.py** in this folder
 
 [!INCLUDE [create-env-file](../includes/create-env-file-tutorial.md)]
 
+## <a name="installs"></a> Install the Azure CLI and sign in 
+
+[!INCLUDE [Install the Azure CLI](../includes/install-cli.md)]
+
+Keep this terminal window open to run your python scripts from here as well, now that you've signed in.
+
 ## Clean up resources
 
 To avoid incurring unnecessary Azure costs, you should delete the resources you created in this tutorial if they're no longer needed. To manage resources, you can use the [Azure portal](https://portal.azure.com?azure-portal=true).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チュートリアルの手順更新"
}
```

### Explanation
この変更は、Azure AI StudioにおけるコパイロットSDKを使用してリソースを作成するためのチュートリアルに関する文書の手順を更新したものです。主な変更点は、Azure CLIのインストールおよびサインインに関連するセクションの位置が変更されたことです。具体的には、新しいプロジェクト用のフォルダを作成し、ターミナルをそのフォルダ内で開く手順が追加されています。

また、Python環境を作成する手順の後にAzure CLIのインストールを行うように順序が調整され、ユーザーがスクリプトを実行するためのターミナルを開いたままで作業できる旨が強調されています。この改善により、チュートリアルがより直感的になり、利用者が指定された手順を効率的に進められるようになっています。


