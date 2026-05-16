---
date: '2026-05-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca3a955...MicrosoftDocs:6fafdc8
summary: この更新では、Azureリソースやプロジェクトの設定における役割名を「Azure AIアカウントオーナー」から「Foundryアカウントオーナー」に変更しました。この変更により、役割名が統一され、ユーザーがアクセス権の要件をより理解しやすくなります。また、CQA関連ドキュメントでは必要なリソースについての指摘が強調されています。この変更は、運用効率を向上させ、ユーザーエクスペリエンスの改善を目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:ca3a955...MicrosoftDocs:6fafdc8){target="_blank"}

<format>
# ハイライト
この更新は、さまざまなAzureリソースやプロジェクトの設定において必要となる役割名を「Azure AIアカウントオーナー」から「Foundryアカウントオーナー」に変更するものです。これにより、役割の名称が統一され、ユーザーがアクセス権の要件をより理解しやすくなります。また、注記が追加され、変更点を明確にしています。

## 新機能
特に新機能が追加されたわけではなく、主に既存の役割名の更新が行われました。

## 破壊的変更
破壊的変更はありませんが、役割名の変更により、ユーザーはドキュメントの内容を確認し、設定を再確認する必要があります。

## その他の更新
追加で、CQA（Conversational Question Answering）関連のドキュメントには必要なリソースについての指摘が強調されています。「Microsoft Foundryリソース」や「Azure AI Searchリソース」が要件として明記されました。

# 洞察
今回の変更は、主に役割名を「Azure AIアカウントオーナー」から「Foundryアカウントオーナー」に変更することで、ドキュメントの一貫性を高め、ユーザーが必要なアクセス権限をより直感的に理解できるようにすることを目的としています。この種の名称変更は、ユーザーが最新のシステムやアクセス要件について混乱しないように保つために重要です。特に、企業が提供する異なるサービスやプラットフォーム間で役割や権限管理の整合性を保つことは、運用効率を向上させます。

また、CQA関連のドキュメントで追加されたリソースの明記は、ユーザーが何を準備する必要があるかを具体的に示し、よりスムーズなプロジェクト設定を助けるためのものです。これにより、実践的な運用フェーズでの問題を未然に防ぎ、システムの導入を円滑に進めることが期待されます。

このようなドキュメントの小規模ながらも重要な更新は、ユーザーエクスペリエンスの向上に寄与し、Azure環境での作業をより容易かつ正確なものにするための戦略的改善策とも言えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [configure-azure-resources.md](#item-f4a2b0) | minor update | Azureリソースの設定に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [build-multi-turn-model.md](#item-dcf352) | minor update | CLVモデルの構築に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [create-project.md](#item-58b2dd) | minor update | プロジェクト作成に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [quickstart-multi-turn-conversations.md](#item-9a3011) | minor update | マルチターン会話のクイックスタートにおける役割名の変更 | modified | 3 | 1 | 4 | 
| [train-model.md](#item-f5b164) | minor update | モデル訓練に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [azure-ai-foundry.md](#item-3076ad) | minor update | Azure AI Foundryにおける役割名の変更 | modified | 3 | 1 | 4 | 
| [azure-ai-foundry.md](#item-86cfba) | minor update | カスタム命名エンティティ認識に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [prerequisites-with-storage.md](#item-fd8f82) | minor update | ストレージを伴う前提条件に関する役割名の変更 | modified | 3 | 1 | 4 | 
| [prerequisites.md](#item-e85bb5) | minor update | 前提条件に関する役割名の更新 | modified | 3 | 1 | 4 | 
| [azure-ai-foundry.md](#item-41c23c) | minor update | 前提条件における役割名の変更 | modified | 3 | 1 | 4 | 
| [azure-ai-foundry.md](#item-ff89fc) | minor update | 前提条件に関する役割名の更新 | modified | 3 | 1 | 4 | 
| [configure-azure-resources.md](#item-a2ea5c) | minor update | 前提条件の役割名変更とリソースの追加 | modified | 3 | 1 | 4 | 
| [create-test-deploy.md](#item-80a22f) | minor update | 前提条件の役割名変更とリソースの追加 | modified | 3 | 1 | 4 | 
| [deploy-agent.md](#item-36ec34) | minor update | 前提条件の役割名変更とリソースの追加 | modified | 3 | 1 | 4 | 
| [azure-ai-foundry.md](#item-bb6666) | minor update | 役割名の変更と前提条件のリソースの追加 | modified | 3 | 1 | 4 | 


# Modified Contents
## articles/ai-services/language-service/concepts/configure-azure-resources.md{#item-f4a2b0}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,9 @@ In addition, we show you how to assign the correct roles and permissions within
 Before you can set up your resources, you need:
 
 * **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../foundry/includes/role-rename-note.md)]
 * A [Foundry resource](/azure/ai-services/multi-service-resource) or an [Azure Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 
 * An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) (optional but required for [option 2](#option-2-configure-azure-language-resource-and-azure-openai-resources))
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azureリソースの設定に関する役割名の変更"
}
```

### Explanation
この変更では、Azureのリソースを設定する際に必要な権限の説明が更新されています。具体的には、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。これは、アカウントおよびプロジェクトを設定する際に求められる役割に関する重要な情報です。また、この変更に加え、役割名変更に関する注記が新たに追加され、ユーザーへの情報提供が強化されています。この更新は、ユーザーが必要なアクセス権を理解しやすくするためのものです。

## articles/ai-services/language-service/conversational-language-understanding/how-to/build-multi-turn-model.md{#item-dcf352}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,9 @@ In this article, learn how to build a CLU model that implements entity slot fill
 
 * **Azure subscription** - If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-* **Required permissions** - Ensure that the person establishing the account and project has the Azure AI Account Owner role at the subscription level. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+* **Required permissions** - Ensure that the person establishing the account and project has the Foundry Account Owner role at the subscription level. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 
 * **Azure Language in Foundry Tools resource** - Create a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics) in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "CLVモデルの構築に関する役割名の変更"
}
```

### Explanation
この変更は、会話型言語理解（CLU）モデルの構築に関するドキュメントの一部であり、必要な権限に関する情報が更新されています。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、アカウントやプロジェクトを設定する際の要件が明確にされています。また、役割名変更に関する注記も新たに追加され、ユーザーへの説明が強化されています。この更新により、ユーザーは必要なアクセス権をより簡単に理解できるようになっています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,9 @@ A Conversational Language Understanding (CLU) fine-tuning task is a workspace pr
 ## Prerequisites
 
 * An **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 *  An [**Foundry resource**](../../../multi-service-resource.md). For more information, *see* [Configure a Foundry resource](configure-azure-resources.md#option-1-configure-a-foundry-resource). Alternately, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project created in the Foundry**. For more information, *see* [Create a Foundry project](../../../../ai-foundry/how-to/create-projects.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プロジェクト作成に関する役割名の変更"
}
```

### Explanation
この変更は、会話型言語理解（CLU）のプロジェクトを作成する際に必要な条件に関するドキュメントの一部で、権限に関する情報が更新されています。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。この変更により、アカウントおよびプロジェクトを設定するために必要な役割の認識が改善されます。また、役割名変更に関する注記が新たに追加され、さらなる情報提供が行われています。この更新は、ユーザーが必要なアクセス権を正確に理解するための助けとなります。

## articles/ai-services/language-service/conversational-language-understanding/how-to/quickstart-multi-turn-conversations.md{#item-9a3011}

<details>
<summary>Diff</summary>
````diff
@@ -30,7 +30,9 @@ If you don't have an Azure subscription, [create a free account](https://azure.m
 
 * **Azure subscription** - If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-* **Required permissions** - Ensure that the person establishing the account and project has the Azure AI Account Owner role at the subscription level. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Language role-based access control](../../concepts/role-based-access-control.md) and [Assign Azure roles](/azure/role-based-access-control/role-assignments-steps).
+* **Required permissions** - Ensure that the person establishing the account and project has the Foundry Account Owner role at the subscription level. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Language role-based access control](../../concepts/role-based-access-control.md) and [Assign Azure roles](/azure/role-based-access-control/role-assignments-steps).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 
 * **Azure Language in Foundry Tools resource** - Create a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics) in the Azure portal.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "マルチターン会話のクイックスタートにおける役割名の変更"
}
```

### Explanation
この変更は、マルチターン会話のクイックスタートガイドにおいて、ユーザーが必要とする権限に関する情報が更新されたものです。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、これによりアカウントやプロジェクトを設定するための要件が明確になりました。また、役割名変更に関する注記が新たに追加され、ユーザーが役割の認識を容易にするための情報が提供されています。この更新により、ユーザーが適切なアクセス権を持つかどうかを確認しやすくなります。

## articles/ai-services/language-service/conversational-language-understanding/how-to/train-model.md{#item-f5b164}

<details>
<summary>Diff</summary>
````diff
@@ -28,7 +28,9 @@ Model evaluation is triggered automatically after training is completed successf
 ## Prerequisites
 
 * **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 * **A project created in the Microsoft Foundry**. For more information, *see* [Create a Foundry project](../../../../ai-foundry/how-to/create-projects.md).
 * [**Your labeled utterances**](tag-utterances.md) tagged for your fine tuning task.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデル訓練に関する役割名の変更"
}
```

### Explanation
この変更は、モデル訓練に関するドキュメントの一部で、必要な権限に関する情報が更新されています。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、これによりアカウントおよびプロジェクトを設定するための要件が明確にされました。また、役割名の変更を説明する注記が新たに追加され、ユーザーが必要とする情報をより理解しやすくしています。この更新は、ユーザーが適切なアクセス権を有しているかどうかの確認を円滑に行えるようにするためのものです。

## articles/ai-services/language-service/conversational-language-understanding/includes/quickstarts/azure-ai-foundry.md{#item-3076ad}

<details>
<summary>Diff</summary>
````diff
@@ -15,7 +15,9 @@ ms.author: lajanuar
 ## Prerequisites
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../../foundry/includes/role-rename-note.md)]
 *  [Foundry resource](/azure/ai-services/multi-service-resource). For more information, *see* [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternately, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project created in the Foundry**. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Foundryにおける役割名の変更"
}
```

### Explanation
この変更は、Azure AI Foundryに関するドキュメントの一部で、必要な権限に関する情報が更新されました。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、これによりアカウントおよびプロジェクトを設定するための要件が明確にされました。また、役割名変更に関する注記が追加され、ユーザーが必要な情報をより理解しやすくしています。この更新は、ユーザーが正しいアクセス権を持っていることを確認しやすくすることを目的としています。

## articles/ai-services/language-service/custom-named-entity-recognition/includes/quickstarts/azure-ai-foundry.md{#item-86cfba}

<details>
<summary>Diff</summary>
````diff
@@ -14,7 +14,9 @@ ms.author: lajanuar
 
 * An **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-* The **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control).
+* The **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control).
+
+  [!INCLUDE [role-rename-note](../../../../../foundry/includes/role-rename-note.md)]
 
 *  An [**Language resource with a storage account**](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics). On the **select additional features** page, select the **Custom text classification, Custom named entity recognition, Custom sentiment analysis & Custom Text Analytics for health** box to link a required storage account to this resource:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタム命名エンティティ認識に関する役割名の変更"
}
```

### Explanation
この変更は、カスタム命名エンティティ認識に関するドキュメントの一部で、必要な権限に関連する情報が更新されています。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、アカウントとプロジェクトの設定に関する要件がより明確になりました。また、役割名の変更を説明する注記が新たに追加され、ユーザーが必要な情報を理解しやすくしています。この更新は、ユーザーが適切な権限を持っていることを確認するうえでの助けとなります。

## articles/ai-services/language-service/includes/microsoft-foundry/prerequisites-with-storage.md{#item-fd8f82}

<details>
<summary>Diff</summary>
````diff
@@ -2,7 +2,9 @@
 
 * An **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
 
-* The **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control).
+* The **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 
 *  An [**Language resource with a storage account**](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics). On the **select additional features** page, select the **Custom text classification, Custom named entity recognition, Custom sentiment analysis & Custom Text Analytics for health** box to link a required storage account to this resource:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ストレージを伴う前提条件に関する役割名の変更"
}
```

### Explanation
この変更は、ストレージを伴う前提条件に関連するドキュメントの一部で、必要な権限に関する記述が更新されました。具体的には、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、アカウントおよびプロジェクトを設定するための要件が明確にされています。また、役割名の変更を説明する注記が追加され、ユーザーが必要な情報をより理解しやすくなっています。この更新は、ユーザーが必要なアクセス権を確認できるようにすることを目的としています。

## articles/ai-services/language-service/includes/microsoft-foundry/prerequisites.md{#item-e85bb5}

<details>
<summary>Diff</summary>
````diff
@@ -11,6 +11,8 @@ ms.custom: include
 ---
 
 * **An Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 * [**A Foundry resource**](/azure/ai-services/multi-service-resource) (recommended). For more information, *see* [Configure a Foundry resource](../../concepts/configure-azure-resources.md). Alternately, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project created in the Foundry**. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件に関する役割名の更新"
}
```

### Explanation
この変更は、前提条件に関するドキュメントの一部で、必要な権限に関する情報が更新されています。「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、アカウントおよびプロジェクトの設定に関する要件がより明確になりました。さらに、役割名の変更を説明する注記が新たに追加されており、ユーザーが必要な情報を理解しやすくなっています。この更新は、ユーザーが必要な権限を確認する手助けをすることを目的としています。

## articles/ai-services/language-service/language-detection/includes/quickstarts/azure-ai-foundry.md{#item-41c23c}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,9 @@ ai-usage: ai-assisted
 ## Prerequisites
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project has the Azure AI Account Owner role at the subscription level assigned. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project has the Foundry Account Owner role at the subscription level assigned. Alternatively, the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../../foundry/includes/role-rename-note.md)]
 * **Foundry resource**. Create a [Foundry resource](../../../../multi-service-resource.md) or see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternatively, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project**. For more information, see [Create a Foundry project](../../../../../ai-foundry/how-to/create-projects.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件における役割名の変更"
}
```

### Explanation
この変更は、言語検出に関するクイックスタートガイドの前提条件セクションに関連しています。必要な権限に関する記述が更新され、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。これにより、アカウントおよびプロジェクトを設定する際の要件がより具体的になっています。また、役割名の変更についての注記も新たに追加され、ユーザーが必要な情報を容易に理解できるよう工夫されています。この変更により、ユーザーの権限の確認が円滑に行えることを目指しています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/azure-ai-foundry.md{#item-ff89fc}

<details>
<summary>Diff</summary>
````diff
@@ -17,7 +17,9 @@ ms.custom: doc-kit-assisted
 > * Consider using a Foundry resource for the best experience. You can also follow these instructions with a Language resource.
 
 * **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, see [Role based access control (RBAC)](../../../../../ai-foundry/openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../../foundry/includes/role-rename-note.md)]
 * **Foundry resource**. Create a [Foundry resource](../../../../multi-service-resource.md) or see [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternatively, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 * **A Foundry project**. For more information, see [Create a Foundry project](../../../../../ai-foundry/how-to/create-projects.md).
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件に関する役割名の更新"
}
```

### Explanation
この変更は、個人を特定できる情報に関するクイックスタートガイドにおける前提条件セクションの更新です。必要な権限に関する記述が更新され、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に改訂されました。これにより、アカウント及びプロジェクトを設定する際の要件が明確化され、ユーザーが遵守するべき情報が整理されました。また、役割名の変更に関する注記が新規に追加され、ユーザーが必要な情報を容易に理解できるよう配慮されています。この変更は、ユーザーが必要な権限を把握しやすくすることを目指しています。

## articles/ai-services/language-service/question-answering/how-to/configure-azure-resources.md{#item-a2ea5c}

<details>
<summary>Diff</summary>
````diff
@@ -19,7 +19,9 @@ In addition, we show you how to assign the correct roles and permissions within
 Before you can set up your resources, you need:
 
 * **An active Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 *   A [Microsoft Foundry resource](../../../multi-service-resource.md) or a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 *   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件の役割名変更とリソースの追加"
}
```

### Explanation
この変更は、Azureリソースの設定に関するガイドの前提条件セクションに関連しています。必要な権限についての記述が更新され、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。また、役割名の変更に関する注記が新たに追加され、ユーザーが必要な情報を理解しやすくする配慮がなされています。さらに、必要なリソースとして、「Microsoft Foundryリソース」や「Azure AI Searchリソース」が新たに明記され、CQA（Conversational Question Answering）へのアクセスに関する要件も強調されています。この変更により、ユーザーがリソースの準備や役割の確認を行いやすくしています。

## articles/ai-services/language-service/question-answering/how-to/create-test-deploy.md{#item-80a22f}

<details>
<summary>Diff</summary>
````diff
@@ -24,7 +24,9 @@ This guide walks you through the essential steps needed to create, test, and dep
 Before you get started, you need the following resources and permissions:
 
 * **An active Azure subscription**. If you don't have one, [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 *   A [Foundry resource](../../../multi-service-resource.md) or a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 *   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA). For more information on how to connect your Azure AI Search resource, *see* [Configure connections in Foundry](../../conversational-language-understanding/how-to/configure-azure-resources.md#step-2-configure-connections-in-ai-foundry)
 * A Foundry project created in the Foundry. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件の役割名変更とリソースの追加"
}
```

### Explanation
この変更は、テストデプロイの作成手順に関するガイドにおける前提条件セクションの更新です。必要な権限の記述が改訂され、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。また、新たに役割名の変更に関する注記が付加され、ユーザーが必要な情報を簡単に理解できるようにしています。さらに、必要なリソースとして「Foundryリソース」や「Azure AI Searchリソース」が追加され、特にCQA（Conversational Question Answering）へのアクセスに必要な要件として強調されています。全体として、この変更はユーザーがリソースの確認と準備を行いやすくすることを意図しています。

## articles/ai-services/language-service/question-answering/how-to/deploy-agent.md{#item-36ec34}

<details>
<summary>Diff</summary>
````diff
@@ -25,7 +25,9 @@ This article gives you clear steps and important tips for building and deploying
 Before you get started, you need the following resources and permissions:
 
 * **An active Azure subscription**. If you don't have one, [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 *   A [Foundry resource](../../../multi-service-resource.md) or a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 *   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA). For more information on how to connect your Azure AI Search resource, *see* [Configure connections in Foundry](../../conversational-language-understanding/how-to/configure-azure-resources.md#step-2-configure-connections-in-ai-foundry)
 * A Foundry project created in the Foundry with a **deployed CQA knowledge base**. For more information, *see* [Create and deploy a CQA project](create-test-deploy.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "前提条件の役割名変更とリソースの追加"
}
```

### Explanation
この変更は、エージェントのデプロイに関するガイドの前提条件セクションを更新しています。必要な権限に関する記述が改訂され、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更されました。また、役割名の変更に伴う注記が新たに追加され、ユーザーがより明確に理解できるように工夫されています。加えて、必要なリソースとして「Foundryリソース」や「Azure AI Searchリソース」が明記され、特にCQA（Conversational Question Answering）にアクセスするための要件が強調されています。最後に、デプロイされたCQAナレッジベースを持つFoundryプロジェクトが必要であることが明記され、ユーザーが準備すべき具体的な要素が示されています。これにより、ユーザーはエージェントを適切にデプロイするために必要なリソースや権限を容易に把握できるようになります。

## articles/ai-services/language-service/question-answering/includes/azure-ai-foundry.md{#item-bb6666}

<details>
<summary>Diff</summary>
````diff
@@ -18,7 +18,9 @@ This quickstart guides you through the essential steps needed to create, test, a
 Before you get started, you need the following resources and permissions:
 
 * **An active Azure subscription**. If you don't have one, [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
-* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Foundry Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](../../../openai/how-to/role-based-access-control.md#cognitive-services-contributor).
+
+  [!INCLUDE [role-rename-note](../../../../foundry/includes/role-rename-note.md)]
 *   A [Foundry resource](../../../multi-service-resource.md) or a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
 *   An [Azure AI Search resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.Search) (required for accessing CQA). For more information on how to connect your Azure AI Search resource, *see* [Configure connections in Foundry](../../conversational-language-understanding/how-to/configure-azure-resources.md#step-2-configure-connections-in-ai-foundry)
 * A Foundry project created in the Foundry. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "役割名の変更と前提条件のリソースの追加"
}
```

### Explanation
この変更は、Azure AI Foundryに関するクイックスタートガイドの前提条件を更新する内容です。具体的には、「Azure AIアカウントオーナー」という役割名が「Foundryアカウントオーナー」に変更され、より正確な情報が提供されています。加えて、役割名の変更に関する注記が新たに追加され、利用者が異なる役割について十分に理解できるよう配慮されています。さらに、必要なリソースとして「Foundryリソース」や「Azure AI Searchリソース」が明記され、特にCQA（Conversational Question Answering）へのアクセスが求められることが強調されています。これにより、ユーザーはエージェントのデプロイに必要な情報を一層明確に把握できるようになります。全体として、修正は具体性を高め、ユーザーが準備を整えるためのガイダンスを改善しています。


