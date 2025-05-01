---
date: '2025-05-01'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8a8182...MicrosoftDocs:0ff32a6
summary: |-
  この報告の要約は以下の通りです。

  主な変更点としては、新しい機能は追加されていないものの、`migrate-from-luis.md`ファイルがLUISからCLUへの移行手順を大幅に見直し、詳細を更新しました。また、ドキュメントの最終更新日が多くのファイルで「2025年4月29日」に変更され、「NodeJS」の表記が「Node.js」に修正されました。さらに、`prompt-flow.md`ファイルでは不要な情報が削除され、より簡潔な内容になっています。これらの変更は、ドキュメントの整合性やユーザーエクスペリエンスを向上させることを目的としています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b8a8182...MicrosoftDocs:0ff32a6){target="_blank"}

<format>
# 変更点の概要

## 新しい機能
特に新しい機能は追加されていません。

## 破壊的変更
- `migrate-from-luis.md` ファイルでは、LUISからCLUへの移行手順が大幅に見直され、詳細に更新されました。これには新しい機能の紹介や制約の説明などが含まれます。

## その他の更新
- 各ファイルの最終更新日が、多くの場合「2025年4月29日」に更新されました。
- 「NodeJS」という誤表記が「Node.js」に修正され、標準的な表記に統一されました。
- `prompt-flow.md`ファイルでは、不必要な情報が削除され、チュートリアルの簡潔さが向上しました。

# 詳細な説明

この更新においては、全般的にドキュメントの最新性を保つために最終更新日を変更し、また技術用語の標準的な表記に統一することで情報の一貫性と正確性を向上させることが目標とされています。

特に注目すべきは、`migrate-from-luis.md`の内容更新です。ここでは、LUISからCLUへの移行が避けて通れないシナリオのため、詳細な移行手順が加わり、ユーザーがこれに伴う新しい機能や制約についても理解できるように配慮されています。例えば、CLUでは廃止された機能についても明確に示されています。この更新はLUISからCLUへのスムーズな移行を支援するための重要な変更です。

一方、他の更新データの日付変更や「Node.js」という表記の統一は、表面的には些細な変更のように思えますが、文書全体の整合性を保ち、ユーザーにとっての情報の見通しを良くするために重要です。専門用語が一貫していることで、利用者はコンテンツを容易に理解でき、実際の開発作業の際に誤解を生まないようにすることができます。

また、`prompt-flow.md`では、不要な情報の削除により、ユーザーが重要な情報に集中し、スムーズに作業を進められるようになっており、これもまたユーザーエクスペリエンスを向上させるための重要な手段となっています。

このように本更新は、見た目以上にドキュメントの品質向上に寄与する内容が揃っており、多くのユーザーにとって有用かつ直感的に理解しやすい形式へと改善されています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [use-sdk-rest-api.md](#item-25a870) | minor update | SDKのノード名の修正 | modified | 3 | 3 | 6 | 
| [get-started-sdks-rest-api.md](#item-ed53bc) | minor update | SDKのノード名の修正 | modified | 2 | 2 | 4 | 
| [configure-containers.md](#item-6f87ab) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [multi-region-deployment.md](#item-a7351d) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [data-limits.md](#item-48b8af) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [regional-support.md](#item-5becd3) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [migrate-from-luis.md](#item-fdb6bf) | breaking change | LUISからCLUへの移行手順の刷新 | modified | 49 | 49 | 98 | 
| [train-model.md](#item-f5b164) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [use-containers.md](#item-77ab95) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-b67686) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [overview.md](#item-89c74f) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-29d53a) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-79ac7d) | minor update | 表記の修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-a6bafe) | minor update | 表記の修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-636553) | minor update | 表記の修正 | modified | 1 | 1 | 2 | 
| [ga-preview-mapping.md](#item-bed282) | minor update | 日付の修正 | modified | 1 | 1 | 2 | 
| [named-entity-categories.md](#item-a4a7f1) | minor update | 日付の修正 | modified | 1 | 1 | 2 | 
| [skill-parameters.md](#item-e29e05) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-c084f9) | minor update | Node.jsの表記修正と日付更新 | modified | 2 | 2 | 4 | 
| [use-containers.md](#item-8c61d4) | minor update | 文章内容の明確化と日付の更新 | modified | 6 | 6 | 12 | 
| [quickstart.md](#item-94affd) | minor update | Node.jsの表記修正と日付更新 | modified | 2 | 2 | 4 | 
| [call-api.md](#item-c2ddb6) | minor update | ドキュメントの日付更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-8c5758) | minor update | Node.jsの表記修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-bff856) | minor update | Node.jsの表記修正 | modified | 1 | 1 | 2 | 
| [fhir.md](#item-7ef75f) | minor update | 日付の更新 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-9b06f2) | minor update | Node.jsの表記修正 | modified | 1 | 1 | 2 | 
| [prompt-flow.md](#item-22c24b) | bug fix | 不要な情報の削除 | modified | 0 | 4 | 4 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/use-sdk-rest-api.md{#item-25a870}

<details>
<summary>Diff</summary>
````diff
@@ -94,12 +94,12 @@ Choose from the following Document Intelligence models and analyze and extract d
 ::: zone pivot="programming-language-javascript"
 
 ::: moniker range="doc-intel-4.0.0"
-[!INCLUDE [NodeJS SDK quickstart](includes/v4-0/javascript-sdk.md)]
+[!INCLUDE [Node.js SDK quickstart](includes/v4-0/javascript-sdk.md)]
 ::: moniker-end
 
 ::: moniker range="doc-intel-3.1.0 || doc-intel-3.0.0"
 
-[!INCLUDE [NodeJS SDK quickstart](includes/v3-0/javascript-sdk.md)]
+[!INCLUDE [Node.js SDK quickstart](includes/v3-0/javascript-sdk.md)]
 ::: moniker-end
 
 ::: zone-end
@@ -176,7 +176,7 @@ You use the following APIs to extract structured data from forms and documents:
 ::: zone pivot="programming-language-javascript"
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [NodeJS SDK quickstart](includes/v2-1/javascript-sdk.md)]
+[!INCLUDE [Node.js SDK quickstart](includes/v2-1/javascript-sdk.md)]
 ::: moniker-end
 
 ::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKのノード名の修正"
}
```

### Explanation
この変更では、ドキュメントの中で「NodeJS SDK」という表記が「Node.js SDK」に修正されました。具体的には、`use-sdk-rest-api.md`というファイル内で、ユーザーが利用できるDocument Intelligenceモデルに関連するメッセージにおいて、SDKの名称が一貫性を持たせるために変更されたものです。このマイナーアップデートは、文書の明確さを向上させ、読み手に対して正確な情報を提供することを目的としています。変更の具体的な地点は、異なるモニカー（バージョン）に渡って、SDKの呼称を統一したもので、合計で3か所の追加と削除が行われています。この修正により、ユーザーがSDKをより明確に識別できるようになります。

## articles/ai-services/document-intelligence/quickstarts/get-started-sdks-rest-api.md{#item-ed53bc}

<details>
<summary>Diff</summary>
````diff
@@ -76,7 +76,7 @@ To learn more about the API features and development options, visit our [Overvie
 ::: zone pivot="programming-language-javascript"
 
 ::: moniker range="doc-intel-4.0.0 || doc-intel-3.1.0 || doc-intel-3.0.0"
-[!INCLUDE [NodeJS SDK](includes/javascript-sdk.md)]
+[!INCLUDE [Node.js SDK](includes/javascript-sdk.md)]
 ::: moniker-end
 
 ::: zone-end
@@ -150,7 +150,7 @@ To learn more about Document Intelligence features and development options, visi
 ::: zone pivot="programming-language-javascript"
 
 ::: moniker range="doc-intel-2.1.0"
-[!INCLUDE [NodeJS SDK](includes/v2-1/javascript.md)]
+[!INCLUDE [Node.js SDK](includes/v2-1/javascript.md)]
 ::: moniker-end
 
 ::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "SDKのノード名の修正"
}
```

### Explanation
この変更では、「NodeJS SDK」という表記が「Node.js SDK」に修正されています。具体的には、`get-started-sdks-rest-api.md`というファイル内で、API機能と開発オプションに関連する説明において、この表記が変更されたものです。これにより、SDKの名称が文書全体で統一され、利用者への情報提供が向上します。この修正は、異なるモニカー（バージョン）について行われ、合計で2か所の追加と削除が発生しています。これにより、ユーザーはSDKをより明確に認識できるようになり、ドキュメントの品質が向上します。

## articles/ai-services/language-service/concepts/configure-containers.md{#item-6f87ab}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - ignite-2024
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/04/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`configure-containers.md`というファイル内の更新日が「2024年11月4日」から「2025年4月29日」に変更されました。このマイナーアップデートは、文書の最新性を保つために行われており、参考となる情報の正確性を向上させることを目的としています。この変更により、ユーザーは最新の情報を得ることができ、ドキュメントの信頼性が向上します。その他のメタデータは変更されていません。

## articles/ai-services/language-service/concepts/custom-features/multi-region-deployment.md{#item-a7351d}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/04/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-clu, ignite-2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`multi-region-deployment.md`というファイル内にある更新日が「2024年11月4日」から「2025年4月29日」に変更されました。このマイナーアップデートは、文書の情報が最新であることを保証するために行われ、ユーザーが最新のコンテンツを参照できるようにしています。この更新により、ドキュメントの精度と信頼性が向上します。他のメタ情報には特に変更はありません。

## articles/ai-services/language-service/concepts/data-limits.md{#item-48b8af}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`data-limits.md`というファイルの更新日が「2024年10月21日」から「2025年4月29日」に変更されました。このマイナーアップデートは、文書の最新性を保つために行われており、ユーザーに対して信頼性の高い情報を提供することを目的としています。このように更新することで、ユーザーが常に最新の情報を得られるようになり、ドキュメントの品質が向上します。他のメタデータはそのまま維持されています。

## articles/ai-services/language-service/concepts/regional-support.md{#item-5becd3}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: references_regions 
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`regional-support.md`というファイル内の更新日が「2024年10月21日」から「2025年4月29日」に変更されました。このマイナーアップデートは、文書の情報を最新の状態に保つために行われ、ユーザーが常に正確で信頼できる情報を得られることを目指しています。文書全体の整合性を保つために、このような小さな変更が重要です。他のメタ情報は引き続き同じままとなっています。

## articles/ai-services/language-service/conversational-language-understanding/how-to/migrate-from-luis.md{#item-fdb6bf}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-clu
 ---
@@ -17,7 +17,7 @@ ms.custom: language-service-clu
 
 CLU offers the following advantages over LUIS: 
 
-- Improved accuracy with state-of-the-art machine learning models for better intent classification and entity extraction. LUIS required more examples to generalize certain concepts in intents and entities, while CLU's more advanced machine learning reduces the burden on customers by requiring significantly less data.  
+- Improved accuracy with state-of-the-art machine learning models for better intent classification and entity extraction. LUIS required more examples to generalize certain concepts in intents and entities, while CLU's more advanced machine learning reduces the burden on customers by requiring less data.  
 - Multilingual support for model learning and training. Train projects in one language and immediately predict intents and entities across 96 languages.
 - Ease of integration with different CLU and [custom question answering](../../question-answering/overview.md) projects using [orchestration workflow](../../orchestration-workflow/overview.md). 
 - The ability to add testing data within the experience using Language Studio and APIs for model performance evaluation prior to deployment. 
@@ -30,23 +30,23 @@ The following table presents a side-by-side comparison between the features of L
 
 |LUIS features | CLU features | Post migration |
 |:------------:|:----------------------------------------------:|:--------------:|
-|Machine-learned and Structured ML entities| Learned [entity components](#how-are-entities-different-in-clu) |Machine-learned entities without subentities will be transferred as CLU entities. Structured ML entities will only transfer leaf nodes (lowest level subentities that do not have their own subentities) as entities in CLU. The name of the entity in CLU will be the name of the subentity concatenated with the parent. For example, _Order.Size_|
-|List, regex, and prebuilt entities| List, regex, and prebuilt [entity components](#how-are-entities-different-in-clu) | List, regex, and prebuilt entities will be transferred as entities in CLU with a populated entity component based on the entity type.|
-|`Pattern.Any` entities| Not currently available | `Pattern.Any` entities will be removed.|
-|Single culture for each application|[Multilingual models](#how-is-conversational-language-understanding-multilingual) enable multiple languages for each project. |The primary language of your project will be set as your LUIS application culture. Your project can be trained to extend to different languages.|
-|Entity roles  |[Roles](#how-are-entity-roles-transferred-to-clu) are no longer needed. | Entity roles will be transferred as entities.|
-|Settings for: normalize punctuation, normalize diacritics, normalize word form, use all training data  |[Settings](#how-is-the-accuracy-of-clu-better-than-luis) are no longer needed. |Settings will not be transferred.  |
-|Patterns and phrase list features|[Patterns and Phrase list features](#how-is-the-accuracy-of-clu-better-than-luis) are no longer needed. |Patterns and phrase list features will not be transferred.  |
-|Entity features| Entity components| List or prebuilt entities added as features to an entity will be transferred as added components to that entity. [Entity features](#how-do-entity-features-get-transferred-in-clu) will not be transferred for intents. |
-|Intents and utterances| Intents and utterances |All intents and utterances will be transferred. Utterances will be labeled with their transferred entities. |
-|Application GUIDs |Project names| A project will be created for each migrating application with the application name. Any special characters in the application names will be removed in CLU.|
-|Versioning| Every time you train, a model is created and acts as a version of your [project](#how-do-i-manage-versions-in-clu). | A project will be created for the selected application version. |
-|Evaluation using batch testing |Evaluation using testing sets | [Adding your testing dataset](../how-to/tag-utterances.md#how-to-label-your-utterances) will be required.|  
+|Machine-learned and Structured ML entities| Learned [entity components](#how-are-entities-different-in-clu) |Machine-learned entities without subentities are transferred as CLU entities. Structured ML entities only transfer leaf nodes (lowest level subentities that don't have their own subentities) as entities in CLU. The name of the entity in CLU is the name of the subentity concatenated with the parent. For example, _Order.Size_|
+|List, regex, and prebuilt entities| List, regex, and prebuilt [entity components](#how-are-entities-different-in-clu) | List, regex, and prebuilt entities are transferred as entities in CLU with a populated entity component based on the entity type.|
+|`Pattern.Any` entities| Not currently available | `Pattern.Any` entities are removed.|
+|Single culture for each application|[Multilingual models](#how-is-conversational-language-understanding-multilingual) enable multiple languages for each project. |The primary language of your project are set as your LUIS application culture. Your project can be trained to extend to different languages.|
+|Entity roles  |[Roles](#how-are-entity-roles-transferred-to-clu) are no longer needed. | Entity roles are transferred as entities.|
+|Settings for: normalize punctuation, normalize diacritics, normalize word form, use all training data  |[Settings](#how-is-the-accuracy-of-clu-better-than-luis) are no longer needed. |Settings aren't transferred.  |
+|Patterns and phrase list features|[Patterns and Phrase list features](#how-is-the-accuracy-of-clu-better-than-luis) are no longer needed. |Patterns and phrase list features aren't transferred.  |
+|Entity features| Entity components| List or prebuilt entities added as features to an entity are transferred as added components to that entity. [Entity features](#how-do-entity-features-get-transferred-in-clu) aren't transferred for intents. |
+|Intents and utterances| Intents and utterances |All intents and utterances are transferred. Utterances are labeled with their transferred entities. |
+|Application GUIDs |Project names| A project is created for each migrating application with the application name. Any special characters in the application names are removed in CLU.|
+|Versioning| Every time you train, a model is created and acts as a version of your [project](#how-do-i-manage-versions-in-clu). | A project is created for the selected application version. |
+|Evaluation using batch testing |Evaluation using testing sets | [Adding your testing dataset](../how-to/tag-utterances.md#how-to-label-your-utterances) is required.|  
 |Role-Based Access Control (RBAC) for LUIS resources |Role-Based Access Control (RBAC) available for Language resources |Language resource RBAC must be [manually added after migration](../../concepts/role-based-access-control.md). |
-|Single training mode| Standard and advanced [training modes](#how-are-the-training-times-different-in-clu-how-is-standard-training-different-from-advanced-training) | Training will be required after application migration. |
-|Two publishing slots and version publishing |Ten deployment slots with custom naming | Deployment will be required after the application’s migration and training. |
-|LUIS authoring APIs and SDK support in .NET, Python, Java, and Node.js |[CLU Authoring REST APIs](https://aka.ms/clu-authoring-apis). | For more information, see the [quickstart article](../quickstart.md?pivots=rest-api) for information on the CLU authoring APIs. [Refactoring](#do-i-have-to-refactor-my-code-if-i-migrate-my-applications-from-luis-to-clu) will be necessary to use the CLU authoring APIs. |
-|LUIS Runtime APIs and SDK support in .NET, Python, Java, and Node.js |[CLU Runtime APIs](https://aka.ms/clu-runtime-api). CLU Runtime SDK support for [.NET](/dotnet/api/overview/azure/ai.language.conversations-readme) and [Python](/python/api/overview/azure/ai-language-conversations-readme?view=azure-python-preview&preserve-view=true). | See [how to call the API](../how-to/call-api.md#use-the-client-libraries-azure-sdk) for more information. [Refactoring](#do-i-have-to-refactor-my-code-if-i-migrate-my-applications-from-luis-to-clu) will be necessary to use the CLU runtime API response. |
+|Single training mode| Standard and advanced [training modes](#how-are-the-training-times-different-in-clu-how-is-standard-training-different-from-advanced-training) | Training is required after application migration. |
+|Two publishing slots and version publishing |Ten deployment slots with custom naming | Deployment is required after the application’s migration and training. |
+|LUIS authoring APIs and SDK support in .NET, Python, Java, and Node.js |[CLU Authoring REST APIs](https://aka.ms/clu-authoring-apis). | For more information, see the [quickstart article](../quickstart.md?pivots=rest-api) for information on the CLU authoring APIs. [Refactoring](#do-i-have-to-refactor-my-code-if-i-migrate-my-applications-from-luis-to-clu) is necessary to use the CLU authoring APIs. |
+|LUIS Runtime APIs and SDK support in .NET, Python, Java, and Node.js |[CLU Runtime APIs](https://aka.ms/clu-runtime-api). CLU Runtime SDK support for [.NET](/dotnet/api/overview/azure/ai.language.conversations-readme) and [Python](/python/api/overview/azure/ai-language-conversations-readme?view=azure-python-preview&preserve-view=true). | See [how to call the API](../how-to/call-api.md#use-the-client-libraries-azure-sdk) for more information. [Refactoring](#do-i-have-to-refactor-my-code-if-i-migrate-my-applications-from-luis-to-clu) is necessary to use the CLU runtime API response. |
 
 ## Migrate your LUIS applications
 
@@ -58,7 +58,7 @@ Use the following steps to migrate your LUIS application using either the LUIS p
 
 Follow these steps to begin migration using the [LUIS Portal](https://www.luis.ai/): 
 
-1. After logging into the LUIS portal, click the button on the banner at the top of the screen to launch the migration wizard. The migration will only copy your selected LUIS applications to CLU. 
+1. After logging into the LUIS portal, click the button on the banner at the top of the screen to launch the migration wizard. The migration copies your selected LUIS applications to CLU. 
 
     :::image type="content" source="../media/backwards-compatibility/banner.svg" alt-text="A screenshot showing the migration banner in the LUIS portal." lightbox="../media/backwards-compatibility/banner.svg":::
 
@@ -71,15 +71,15 @@ Follow these steps to begin migration using the [LUIS Portal](https://www.luis.a
 
     :::image type="content" source="../media/backwards-compatibility/select-resource.svg" alt-text="A screenshot showing the resource selection window." lightbox="../media/backwards-compatibility/select-resource.svg":::
 
-1. Select all your LUIS applications that you want to migrate, and specify each of their versions. Select **Next**. After selecting your application and version, you will be prompted with a message informing you of any features that won't be carried over from your LUIS application. 
+1. Select all your LUIS applications that you want to migrate, and specify each of their versions. Select **Next**. After selecting your application and version, you're prompted with a message informing you of any features that won't be carried over from your LUIS application. 
 
     > [!NOTE] 
-    > Special characters are not supported by conversational language understanding. Any special characters in your selected LUIS application names will be removed in your new migrated applications. 
+    > Special characters aren't supported by conversational language understanding. Any special characters in your selected LUIS application names are removed in your new migrated applications. 
     :::image type="content" source="../media/backwards-compatibility/select-applications.svg" alt-text="A screenshot showing the application selection window." lightbox="../media/backwards-compatibility/select-applications.svg":::
 
 1. Review your Language resource and LUIS applications selections. Select **Finish** to migrate your applications.  
 
-1. A popup window will let you track the migration status of your applications. Applications that have not started migrating will have a status of **Not started**. Applications that have begun migrating will have a status of **In progress**, and once they have finished migrating their status will be **Succeeded**. A **Failed** application means that you must repeat the migration process. Once the migration has completed for all applications, select **Done**.
+1. A popup window lets you track the migration status of your applications. Applications that haven't started migrating have a status of **Not started**. Applications that have begun migrating have a status of **In progress**, and once they have finished migrating their status is **Succeeded**. A **Failed** application means that you must repeat the migration process. Once the migration has completed for all applications, select **Done**.
 
     :::image type="content" source="../media/backwards-compatibility/migration-progress.svg" alt-text="A screenshot showing the application migration progress window." lightbox="../media/backwards-compatibility/migration-progress.svg":::
 
@@ -97,7 +97,7 @@ Follow these steps to begin migration programmatically using the CLU Authoring R
 
 1. Export your LUIS application in JSON format. You can use the [LUIS Portal](https://www.luis.ai/) to export your applications, or the [LUIS programmatic APIs](https://westus.dev.cognitive.microsoft.com/docs/services/luis-programmatic-apis-v3-0-preview/operations/5890b47c39e2bb052c5b9c40).  
 
-1. Submit a POST request using the following URL, headers, and JSON body to import LUIS application into your CLU project. CLU does not support names with special characters so remove any special characters from the project name.
+1. Submit a POST request using the following URL, headers, and JSON body to import LUIS application into your CLU project. CLU doesn't support names with special characters so remove any special characters from the project name.
     
     ### Request URL
     ```rest
@@ -108,7 +108,7 @@ Follow these steps to begin migration programmatically using the CLU Authoring R
     |---------|---------|---------|
     |`{ENDPOINT}`     | The endpoint for authenticating your API request.   | `https://<your-custom-subdomain>.cognitiveservices.azure.com` |
     |`{PROJECT-NAME}`     | The name for your project. This value is case sensitive.   | `myProject` |
-    |`{API-VERSION}`     | The [version](../../concepts/model-lifecycle.md#api-versions) of the API you are calling. | `2023-04-01` |
+    |`{API-VERSION}`     | The [version](../../concepts/model-lifecycle.md#api-versions) of the API you're calling. | `2023-04-01` |
       
     ### Headers
 
@@ -144,9 +144,9 @@ In CLU, a single entity can have multiple entity components, which are different
 - Prebuilt: Prebuilt components allow you to define an entity with the prebuilt extractors for common types available in both LUIS and CLU.
 - Regex: Regex components use regular expressions to capture custom defined patterns, exactly like regex entities in LUIS.
 
-Entities in LUIS will be transferred over as entities of the same name in CLU with the equivalent components transferred.
+Entities in LUIS are transferred over as entities of the same name in CLU with the equivalent components transferred.
 
-After migrating, your structured machine-learned leaf nodes and bottom-level subentities will be transferred to the new CLU model while all the parent entities and higher-level entities will be ignored. The name of the entity will be the bottom-level entity’s name concatenated with its parent entity. 
+After migrating, your structured machine-learned leaf nodes and bottom-level subentities are transferred to the new CLU model while all the parent entities and higher-level entities are ignored. The name of the entity is the bottom-level entity’s name concatenated with its parent entity. 
 
 #### Example: 
 
@@ -161,21 +161,21 @@ Migrated LUIS entity in CLU:
 * Pizza Order.Topping 
 * Pizza Order.Size 
  
-You also cannot label 2 different entities in CLU for the same span of characters. Learned components in CLU are mutually exclusive and do not provide overlapping predictions for learned components only. When migrating your LUIS application, entity labels that overlapped preserved the longest label and ignored any others.  
+You also can't label 2 different entities in CLU for the same span of characters. Learned components in CLU are mutually exclusive and don't provide overlapping predictions for learned components only. When migrating your LUIS application, entity labels that overlapped preserved the longest label and ignored any others.  
 
 For more information on entity components, see [Entity components](../concepts/entity-components.md).
 
 ### How are entity roles transferred to CLU? 
 
-Your roles will be transferred as distinct entities along with their labeled utterances. Each role’s entity type will determine which entity component will be populated. For example, a list entity role will be transferred as an entity with the same name as the role, with a populated list component. 
+Your roles are transferred as distinct entities along with their labeled utterances. Each role’s entity type determines which entity component is populated. For example, a list entity role is transferred as an entity with the same name as the role, with a populated list component. 
 
 ### How do entity features get transferred in CLU? 
 
-Entities used as features for intents will not be transferred. Entities used as features for other entities will populate the relevant component of the entity. For example, if a list entity named _SizeList_ was used as a feature to a machine-learned entity named _Size_, then the _Size_ entity will be transferred to CLU with the list values from _SizeList_ added to its list component. The same is applied for prebuilt and regex entities.
+Entities used as features for intents aren't transferred. Entities used as features for other entities populate the relevant component of the entity. For example, if a list entity named _SizeList_ was used as a feature to a machine-learned entity named _Size_, then the _Size_ entity is transferred to CLU with the list values from _SizeList_ added to its list component. The same is applied for prebuilt and regex entities.
 
 ### How are entity confidence scores different in CLU? 
 
-Any extracted entity has a 100% confidence score and therefore entity confidence scores should not be used to make decisions between entities.  
+Any extracted entity has a 100% confidence score and therefore entity confidence scores shouldn't be used to make decisions between entities.  
 
 ### How is conversational language understanding multilingual? 
 
@@ -197,21 +197,21 @@ CLU uses state-of-the-art models to enhance machine learning performance of diff
 
 These models are insensitive to minor variations, removing the need for the following settings: _Normalize punctuation_, _normalize diacritics_, _normalize word form_, and _use all training data_.  
 
-Additionally, the new models do not support phrase list features as they no longer require supplementary information from the user to provide semantically similar words for better accuracy. Patterns were also used to provide improved intent classification using rule-based matching techniques that are not necessary in the new model paradigm. The question below explains this in more detail. 
+Additionally, the new models don't support phrase list features as they no longer require supplementary information from the user to provide semantically similar words for better accuracy. Patterns were also used to provide improved intent classification using rule-based matching techniques that aren't necessary in the new model paradigm. The question below explains this in more detail. 
 
-### What do I do if the features I am using in LUIS are no longer present?
+### What do I do if the features I'm using in LUIS are no longer present?
 
-There are several features that were present in LUIS that will no longer be available in CLU. This includes the ability to do feature engineering, having patterns and pattern.any entities, and structured entities. If you had dependencies on these features in LUIS, use the following guidance:
+There are several features that were present in LUIS that are no longer available in CLU. This includes the ability to do feature engineering, having patterns and pattern.any entities, and structured entities. If you had dependencies on these features in LUIS, use the following guidance:
 
-- **Patterns**: Patterns were added in LUIS to assist the intent classification through defining regular expression template utterances. This included the ability to define Pattern only intents (without utterance examples). CLU is capable of generalizing by leveraging the state-of-the-art models. You can provide a few utterances to that matched a specific pattern to the intent in CLU, and it will likely classify the different patterns as the top intent without the need of the pattern template utterance. This simplifies the requirement to formulate these patterns, which was limited in LUIS, and provides a better intent classification experience. 
+- **Patterns**: Patterns were added in LUIS to assist the intent classification through defining regular expression template utterances. This included the ability to define Pattern only intents (without utterance examples). CLU is capable of generalizing by using the state-of-the-art models. You can provide a few utterances to that matched a specific pattern to the intent in CLU, and it likely classifies the different patterns as the top intent without the need of the pattern template utterance. This simplifies the requirement to formulate these patterns, which was limited in LUIS, and provides a better intent classification experience. 
 
-- **Phrase list features**: The ability to associate features mainly occurred to assist the classification of intents by highlighting the key elements/features to use. This is no longer required since the deep models used in CLU already possess the ability to identify the elements that are inherent in the language. In turn removing these features will have no effect on the classification ability of the model.
+- **Phrase list features**: The ability to associate features mainly occurred to assist the classification of intents by highlighting the key elements/features to use. This is no longer required since the deep models used in CLU already possess the ability to identify the elements that are inherent in the language. In turn removing these features has no effect on the classification ability of the model.
 
-- **Structured entities**: The ability to define structured entities was mainly to enable multilevel parsing of utterances. With the different possibilities of the sub-entities, LUIS needed all the different combinations of entities to be defined and presented to the model as examples. In CLU, these structured entities are no longer supported, since overlapping learned components are not supported. There are a few possible approaches to handling these structured extractions:
+- **Structured entities**: The ability to define structured entities was mainly to enable multilevel parsing of utterances. With the different possibilities of the subentities, LUIS needed all the different combinations of entities to be defined and presented to the model as examples. In CLU, these structured entities are no longer supported, since overlapping learned components aren't supported. There are a few possible approaches to handling these structured extractions:
     - **Non-ambiguous extractions**: In most cases the detection of the leaf entities is enough to understand the required items within a full span. For example, structured entity such as _Trip_ that fully spanned a source and destination (_London to New York_ or _Home to work_) can be identified with the individual spans predicted for source and destination. Their presence as individual predictions would inform you of the _Trip_ entity.
-    - **Ambiguous extractions**: When the boundaries of different sub-entities are not very clear. To illustrate, take the example “I want to order a pepperoni pizza and an extra cheese vegetarian pizza”. While the different pizza types as well as the topping modifications can be extracted, having them extracted without context would have a degree of ambiguity of where the extra cheese is added. In this case the extent of the span is context based and would require ML to determine this. For ambiguous extractions you can use one of the following approaches:
+    - **Ambiguous extractions**: When the boundaries of different subentities aren't clear. To illustrate, take the example "I want to order a pepperoni pizza and an extra cheese vegetarian pizza". While the different pizza types and the topping modifications can be extracted, having them extracted without context would have a degree of ambiguity of where the extra cheese is added. In this case, the extent of the span is context based and would require ML to determine this. For ambiguous extractions you can use one of the following approaches:
 
-1. Combine sub-entities into different entity components within the same entity.
+1. Combine subentities into different entity components within the same entity.
 
 #### Example: 
 
@@ -243,15 +243,15 @@ You can export your CLU projects using [Language Studio](https://language.cognit
 
 ### Why is CLU classification different from LUIS? How does None classification work? 
 
-CLU presents a different approach to training models by using multi-classification as opposed to binary classification. As a result, the interpretation of scores is different and also differs across training options. While you are likely to achieve better results, you have to observe the difference in scores and determine a new threshold for accepting intent predictions. You can easily add a confidence score threshold for the [None intent](../concepts/none-intent.md) in your project settings. This will return *None* as the top intent if the top intent did not exceed the confidence score threshold provided. 
+CLU presents a different approach to training models by using multi-classification as opposed to binary classification. As a result, the interpretation of scores is different and also differs across training options. While you're likely to achieve better results, you have to observe the difference in scores and determine a new threshold for accepting intent predictions. You can easily add a confidence score threshold for the [None intent](../concepts/none-intent.md) in your project settings. This returns *None* as the top intent if the top intent didn't exceed the confidence score threshold provided. 
 
 ### Do I need more data for CLU models than LUIS? 
 
 The new CLU models have better semantic understanding of language than in LUIS, and in turn help make models generalize with a significant reduction of data. While you shouldn’t aim to reduce the amount of data that you have, you should expect better performance and resilience to variations and synonyms in CLU compared to LUIS. 
 
-### If I don’t migrate my LUIS apps, will they be deleted? 
+### If I don’t migrate my LUIS apps, are they deleted? 
 
-Your existing LUIS applications will be available until October 1, 2025. After that time you will no longer be able to use those applications, the service endpoints will no longer function, and the applications will be permanently deleted. 
+Your existing LUIS applications are available until October 1, 2025. After that time you'll no longer be able to use those applications, the service endpoints will no longer function, and the applications will be permanently deleted. 
 
 ### Are .LU files supported on CLU? 
 
@@ -263,19 +263,19 @@ See the [service limits](../service-limits.md) article for more information.
 
 ### Do I have to refactor my code if I migrate my applications from LUIS to CLU? 
 
-The API objects of CLU applications are different from LUIS and therefore code refactoring will be necessary.  
+The API objects of CLU applications are different from LUIS and therefore code refactoring is necessary.  
 
-If you are using the LUIS [programmatic](https://westus.dev.cognitive.microsoft.com/docs/services/luis-programmatic-apis-v3-0-preview/operations/5890b47c39e2bb052c5b9c40) and [runtime](https://westus.dev.cognitive.microsoft.com/docs/services/luis-endpoint-api-v3-0/operations/5cb0a9459a1fe8fa44c28dd8) APIs, you can replace them with their equivalent APIs. 
+If you're using the LUIS [programmatic](https://westus.dev.cognitive.microsoft.com/docs/services/luis-programmatic-apis-v3-0-preview/operations/5890b47c39e2bb052c5b9c40) and [runtime](https://westus.dev.cognitive.microsoft.com/docs/services/luis-endpoint-api-v3-0/operations/5cb0a9459a1fe8fa44c28dd8) APIs, you can replace them with their equivalent APIs. 
 
 [CLU authoring APIs](https://aka.ms/clu-authoring-apis): Instead of LUIS's specific CRUD APIs for individual actions such as _add utterance_, _delete entity_, and _rename intent_, CLU offers an [import API](/rest/api/language/2023-04-01/conversational-analysis-authoring/import) that replaces the full content of a project using the same name. If your service used LUIS programmatic APIs to provide a platform for other customers, you must consider this new design paradigm. All other APIs such as: _listing projects_, _training_, _deploying_, and _deleting_ are available. APIs for actions such as _importing_ and _deploying_ are asynchronous operations instead of synchronous as they were in LUIS. 
 
 [CLU runtime APIs](https://aka.ms/clu-runtime-api): The new API request and response includes many of the same parameters such as: _query_, _prediction_, _top intent_, _intents_, _entities_, and their values. The CLU response object offers a more straightforward approach. Entity predictions are provided as they are within the utterance text, and any additional information such as resolution or list keys are provided in extra parameters called `extraInformation` and `resolution`.
 
-You can use the [.NET](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.Language.Conversations_1.0.0-beta.3/sdk/cognitivelanguage/Azure.AI.Language.Conversations/samples/) or [Python](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-language-conversations_1.1.0b1/sdk/cognitivelanguage/azure-ai-language-conversations/samples/README.md) CLU runtime SDK to replace the LUIS runtime SDK. There is currently no authoring SDK available for CLU. 
+You can use the [.NET](https://github.com/Azure/azure-sdk-for-net/tree/Azure.AI.Language.Conversations_1.0.0-beta.3/sdk/cognitivelanguage/Azure.AI.Language.Conversations/samples/) or [Python](https://github.com/Azure/azure-sdk-for-python/blob/azure-ai-language-conversations_1.1.0b1/sdk/cognitivelanguage/azure-ai-language-conversations/samples/README.md) CLU runtime SDK to replace the LUIS runtime SDK. There's currently no authoring SDK available for CLU. 
 
 ### How are the training times different in CLU? How is standard training different from advanced training?
 
-CLU offers standard training, which trains and learns in English and is comparable to the training time of LUIS. It also offers advanced training, which takes a considerably longer duration as it extends the training to all other [supported languages](../language-support.md). The train API will continue to be an asynchronous process, and you will need to assess the change in the DevOps process you employ for your solution. 
+CLU offers standard training, which trains and learns in English and is comparable to the training time of LUIS. It also offers advanced training, which takes a considerably longer duration as it extends the training to all other [supported languages](../language-support.md). The train API continues to be an asynchronous process, and you need to assess the change in the DevOps process you employ for your solution. 
 
 ### How has the experience changed in CLU compared to LUIS? How is the development lifecycle different?
 
@@ -288,15 +288,15 @@ In LUIS you would Build-Train-Test-Publish, whereas in CLU you Build-Train-Evalu
 
 This process is in contrast to LUIS, where the application ID was attached to everything, and you deployed a version of the application in either the staging or production slots.
 
-This will influence the DevOps processes you use.
+This influences the DevOps processes you use.
 
 ### Does CLU have container support?
 
-No, you cannot export CLU to containers.
+No, you can't export CLU to containers.
 
-### How will my LUIS applications be named in CLU after migration?
+### How are my LUIS applications be named in CLU after migration?
 
-Any special characters in the LUIS application name will be removed. If the cleared name length is greater than 50 characters, the extra characters will be removed. If the name after removing special characters is empty (for example, if the LUIS application name was `@@`), the new name will be _untitled_. If there is already a conversational language understanding project with the same name, the migrated LUIS application will be appended with `_1` for the first duplicate and increase by 1 for each additional duplicate. In case the new name’s length is 50 characters and it needs to be renamed, the last 1 or 2 characters will be removed to be able to concatenate the number and still be within the 50 characters limit. 
+Any special characters in the LUIS application name are removed. If the cleared name length is greater than 50 characters, the extra characters are removed. If the name after removing special characters is empty (for example, if the LUIS application name was `@@`), the new name is _untitled_. If there's already a conversational language understanding project with the same name, the migrated LUIS application is appended with `_1` for the first duplicate and increase by 1 for each subsequent duplicate. In case the new name’s length is 50 characters and it needs to be renamed, the last 1 or 2 characters are removed to be able to concatenate the number and still be within the 50 characters limit. 
 
 ## Migration from LUIS Q&A
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "LUISからCLUへの移行手順の刷新"
}
```

### Explanation
この変更では、`migrate-from-luis.md`ファイルが大幅に改訂され、LUISからCLU（Conversational Language Understanding）への移行手順が詳細に更新されました。具体的には、単純な日付変更から始まり、文の構造的な変更、文言の精緻化、情報の整理まで多岐にわたります。

変更点は主に以下の通りです：
- 更新日が「2024年10月21日」から「2025年4月29日」に変更されました。
- LUISからCLUへの移行方法についての説明が改善され、適用される操作や手順が詳細に記述されています。
- 移行中にユーザーが認識すべき新しい機能や制約が明確にされています。
- 各種機能に関する扱いが変更され、特定の機能（例えば、パターンや構造化エンティティなど）がCLUでは廃止されたことが強調されています。

この変更は、LUISからCLUに移行する際に必要な情報を提供し、サポートを強化することで、ユーザーにとっての使いやすさを向上させることを目的としています。移行に伴う新しい技術や手続きに関する明確なガイダンスを伴うため、ユーザーは新システムへの遷移をスムーズに行うことができます。

## articles/ai-services/language-service/conversational-language-understanding/how-to/train-model.md{#item-f5b164}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-clu
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、`train-model.md`というファイルの更新日が「2024年10月21日」から「2025年4月29日」に変更されたものです。このマイナーアップデートは、文書の最新情報を保つために必要なもので、ユーザーが常に正確で最新の情報にアクセスできるようにすることを目的としています。内容の他の部分は影響を受けておらず、全体の整合性が保たれた形で日付のみが更新されました。

## articles/ai-services/language-service/conversational-language-understanding/how-to/use-containers.md{#item-77ab95}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-language
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 10/07/2024
+ms.date: 04/29/2025
 ms.author: jboback
 keywords: on-premises, Docker, container
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`use-containers.md`ファイルの更新日が「2024年10月7日」から「2025年4月29日」に変更されました。このマイナーアップデートは、ドキュメントが最新の情報を提供するために必要です。これにより、利用者は常に正確な日付を参照でき、情報の信頼性が向上します。他のコンテンツや文の変更はなく、日付のみの更新となっています。

## articles/ai-services/language-service/conversational-language-understanding/quickstart.md{#item-b67686}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-clu, mode-other
 zone_pivot_groups: usage-custom-language-features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
このコードの変更では、`quickstart.md`ファイルの更新日が「2024年10月21日」から「2025年4月29日」に変更されました。このマイナーアップデートは、ドキュメントの時効性を保つために重要です。一貫した情報提供を維持し、ユーザーが最新のデータに基づいて操作できるようにしています。変更は日付のみであり、他の内容には影響を与えていません。

## articles/ai-services/language-service/custom-named-entity-recognition/overview.md{#item-89c74f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: overview
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-custom-ner
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更では、`overview.md`ファイルの更新日が「2024年10月21日」から「2025年4月29日」に更新されました。このマイナーアップデートは、文書の正確性を保つために重要です。ユーザーは、常に最新の日付情報に基づいてコンテンツを利用でき、その信頼性が向上します。変更は日付のみで、他の情報には影響を与えていません。

## articles/ai-services/language-service/custom-text-classification/quickstart.md{#item-29d53a}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-custom-classification, mode-other
 zone_pivot_groups: usage-custom-language-features
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
このコード変更では、`quickstart.md`ファイルの更新日が「2024年10月21日」から「2025年4月29日」に変更されました。このマイナーアップデートは、ドキュメントの最新性を保つために重要であり、ユーザーが最も新しい情報に基づいて作業できるようにします。変更内容は日付の更新のみであり、他の情報には影響を与えていません。

## articles/ai-services/language-service/entity-linking/quickstart.md{#item-79ac7d}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ zone_pivot_groups: programming-languages-entity-linking
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "表記の修正"
}
```

### Explanation
この変更では、`quickstart.md`ファイル内の「NodeJS」という表記が「Node.js」に修正されました。このマイナーアップデートは、正確な表記を使用することで文書の一貫性を高め、読み手にとってより理解しやすくします。変更は表記の修正のみであり、内容の意味や他の情報には影響を与えていません。

## articles/ai-services/language-service/key-phrase-extraction/quickstart.md{#item-a6bafe}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "表記の修正"
}
```

### Explanation
この変更は、`quickstart.md`ファイル内の「NodeJS」という表記を「Node.js」に修正しています。この修正は文書の整合性と正確性を向上させ、利用者にとっての理解を深めることを目的としています。変更内容は表記の変更のみであり、他の情報や機能には影響しないため、ドキュメントの内容全体を通じて一貫性が保たれています。

## articles/ai-services/language-service/language-detection/quickstart.md{#item-636553}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "表記の修正"
}
```

### Explanation
この変更では、`quickstart.md`ファイル内の表記を修正しています。「NodeJS」の記述が「Node.js」に変更され、より正確で一般的な表現が使用されています。このマイナーアップデートにより、文書内の整合性が向上し、利用者が内容をより理解しやすくなります。変更は表記のみに関連しており、ドキュメントの他の部分や機能に影響を与えるものではありません。

## articles/ai-services/language-service/named-entity-recognition/concepts/ga-preview-mapping.md{#item-bed282}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/04/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-ner, ignite-2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の修正"
}
```

### Explanation
この変更は、`ga-preview-mapping.md`ファイル内の最終更新日を修正しています。元の日時「11/04/2024」が「04/29/2025」に変更されており、最新の情報を反映させることを目的としています。このマイナーアップデートは文書の整合性を保つために重要であり、利用者に正確な情報を提供する役割を果たしています。変更自体は日付の更新に限られているため、他の内容や機能には影響を与えていません。

## articles/ai-services/language-service/named-entity-recognition/concepts/named-entity-categories.md{#item-a4a7f1}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-ner
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の修正"
}
```

### Explanation
この変更は、`named-entity-categories.md`ファイル内の最終更新日を更新しています。以前の更新日「10/21/2024」が「04/29/2025」に変更されており、ドキュメントの最新性を確保しています。このマイナーアップデートにより、利用者に正確な情報が提供され、文書の整合性が保たれます。変更は日付に関するものであり、他の内容や機能には影響を与えるものではありません。

## articles/ai-services/language-service/named-entity-recognition/how-to/skill-parameters.md{#item-e29e05}

<details>
<summary>Diff</summary>
````diff
@@ -8,7 +8,7 @@ ms.service: azure-ai-language
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 11/04/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、`skill-parameters.md`ファイルの最終更新日を修正しています。元の更新日「11/04/2024」が「04/29/2025」に変更されており、文書の最新性を確保するためのものです。このマイナーアップデートにより、利用者はより正確な情報を得ることができ、文書全体の整合性が向上します。変更は日付の更新に限定されているため、他の内容や機能には影響を及ぼしません。

## articles/ai-services/language-service/named-entity-recognition/quickstart.md{#item-c084f9}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -31,7 +31,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsの表記修正と日付更新"
}
```

### Explanation
この変更では、`quickstart.md`ファイルが更新され、以下の2つの主な修正が行われました。まず、最終更新日が「10/21/2024」から「04/29/2025」に変更され、文書の最新性が確保されました。次に、Node.jsの表記が「NodeJS」から「Node.js」に修正され、より標準的な表記が使用されています。このマイナー更新により、ドキュメントの整合性と可読性が向上することを目的としています。その他の内容や機能には影響を与えない変更です。

## articles/ai-services/language-service/personally-identifiable-information/how-to/use-containers.md{#item-8c61d4}

<details>
<summary>Diff</summary>
````diff
@@ -7,15 +7,15 @@ manager: nitinme
 ms.service: azure-ai-language
 ms.custom:
 ms.topic: how-to
-ms.date: 10/07/2024
+ms.date: 04/29/2025
 ms.author: jboback
 keywords: on-premises, Docker, container
 ---
 
 # Install and run Personally Identifiable Information (PII) Detection containers
 
 > [!NOTE]
-> The data limits in a single synchronous API call for the PII container are 5120 characters per document and up to 10 documents per call.
+> The data limits in a single synchronous API call for the PII container are 5,120 characters per document and up to 10 documents per call.
 
 Containers enable you to host the PII detection API on your own infrastructure. If you have security or data governance requirements that can't be fulfilled by calling PII detection remotely, then containers might be a good option.
 
@@ -39,11 +39,11 @@ You must meet the following prerequisites before using PII detection containers.
 
 The following table describes the minimum and recommended specifications for the available container. Each CPU core must be at least 2.6 gigahertz (GHz) or faster.
 
-It is recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
+It's recommended to have a CPU with AVX-512 instruction set, for the best experience (performance and accuracy).
 
 |                     | Minimum host specs     | Recommended host specs |
 |---------------------|------------------------|------------------------|
-| **PII detection**   | 1 core, 2GB memory     | 4 cores, 8GB memory    |
+| **PII detection**   | 1 core, 2 GB memory     | 4 cores, 8 GB memory    |
 
 CPU core and memory correspond to the `--cpus` and `--memory` settings, which are used as part of the `docker run` command.
 
@@ -63,7 +63,7 @@ docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/pii:latest
 
 ## Run the container with `docker run`
 
-Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container will continue to run until you stop it. Replace the placeholders below with your own values:
+Once the container is on the host computer, use the [docker run](https://docs.docker.com/engine/reference/commandline/run/) command to run the containers. The container continues to run until you stop it. Replace the placeholders below with your own values:
 
 
 > [!IMPORTANT]
@@ -139,7 +139,7 @@ In this article, you learned concepts and workflow for downloading, installing,
 * You must specify billing information when instantiating a container.
 
 > [!IMPORTANT]
-> Azure AI containers are not licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers do not send customer data (e.g. text that is being analyzed) to Microsoft.
+> Azure AI containers aren't licensed to run without being connected to Azure for metering. Customers need to enable the containers to communicate billing information with the metering service at all times. Azure AI containers don't send customer data (for example, text that is being analyzed) to Microsoft.
 
 ## Next steps
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "文章内容の明確化と日付の更新"
}
```

### Explanation
この変更は、`use-containers.md`ファイルに対して行われたもので、主に3つのポイントが修正されています。最初に、ファイルの最終更新日が「10/07/2024」から「04/29/2025」に変更され、情報の最新性が反映されています。次に、一部の数値表記がより明確に修正され、例えば「5120」が「5,120」と記述されるようになりました。同様に、メモリの表記も「2GB」から「2 GB」に変更されています。最後に、文の表現が微調整され、「container will continue to run until you stop it」が「container continues to run until you stop it」に変更されています。このような修正は、文書の明確さと整合性を高めることを目的としています。

## articles/ai-services/language-service/personally-identifiable-information/quickstart.md{#item-94affd}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.devlang: csharp
 # ms.devlang: csharp, java, javascript, python
@@ -33,7 +33,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsの表記修正と日付更新"
}
```

### Explanation
この変更は、`quickstart.md`ファイルに対して行われたもので、主に二つの重要な修正が含まれています。最初に、最終更新日が「10/21/2024」から「04/29/2025」に変更され、ドキュメントの最新性が保たれています。次に、Node.jsに関する表記が「NodeJS」から「Node.js」に修正され、業界標準の表記が使用されています。これにより、ドキュメントの明確さとプロフェッショナルさが向上し、読者にとっての理解が容易になることを目指しています。この更新は、機能には影響を与えず、主に表記の一貫性と正確性を高めることが目的とされています。

## articles/ai-services/language-service/sentiment-opinion-mining/how-to/call-api.md{#item-c2ddb6}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: how-to
-ms.date: 10/21/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-sentiment-opinion-mining
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントの日付更新"
}
```

### Explanation
この変更は、`call-api.md`ファイルに対して行われたもので、主に最終更新日が「10/21/2024」から「04/29/2025」に変更されています。この修正により、ドキュメントが最新の情報を反映するようになり、ユーザーにとっての有用性が向上します。変更内容は非常に簡潔であり、文書の内容自体には影響を与えず、主に情報の正確性と現代性を確保することを目的としています。

## articles/ai-services/language-service/sentiment-opinion-mining/quickstart.md{#item-8c5758}

<details>
<summary>Diff</summary>
````diff
@@ -31,7 +31,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsの表記修正"
}
```

### Explanation
この変更は、`quickstart.md`ファイルに対して行われたもので、Node.jsに関する表記が「NodeJS」から「Node.js」に修正されています。この修正は、業界標準に従った表記の使用を促進し、ドキュメントの一貫性と正確性を向上させることを目的としています。この変更は説明的な内容に影響を与えるものではなく、あくまで表記の調整に留まっています。そのため、既存の機能や手順には変更がないことを確認しています。

## articles/ai-services/language-service/summarization/quickstart.md{#item-bff856}

<details>
<summary>Diff</summary>
````diff
@@ -32,7 +32,7 @@ zone_pivot_groups: programming-languages-text-analytics
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsの表記修正"
}
```

### Explanation
この変更は、`quickstart.md`ファイルに対して行われたもので、Node.jsに関する表記が「NodeJS」から「Node.js」に修正されています。この修正により、公式な表記に合わせた内容となり、文書の整合性が向上します。この変更は、技術文書における用語の一貫性を高めることを目的としており、他のコンテンツや情報には影響を及ぼさないため、ユーザーに対する具体的な機能や手順の変更はありません。

## articles/ai-services/language-service/text-analytics-for-health/concepts/fhir.md{#item-7ef75f}

<details>
<summary>Diff</summary>
````diff
@@ -6,7 +6,7 @@ author: jboback
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: conceptual
-ms.date: 11/04/2024
+ms.date: 04/29/2025
 ms.author: jboback
 ms.custom: language-service-health, ignite-2024
 ---
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "日付の更新"
}
```

### Explanation
この変更は、`fhir.md`ファイルの最終更新日を「2024年11月4日」から「2025年4月29日」に変更するものです。この日付の更新は、ドキュメントが最新の情報を反映するために必要です。具体的には、内容が改訂されたことを示しており、ユーザーにとっての情報の新鮮さと信頼性を向上させるためのものです。この修正自体は実質的なコンテンツの変更を伴わないため、元の内容や手順に影響を与えるものではありません。

## articles/ai-services/language-service/text-analytics-for-health/quickstart.md{#item-9b06f2}

<details>
<summary>Diff</summary>
````diff
@@ -35,7 +35,7 @@ This article contains Text Analytics for health quickstarts that help with using
 
 ::: zone pivot="programming-language-javascript"
 
-[!INCLUDE [NodeJS quickstart](includes/quickstarts/nodejs-sdk.md)]
+[!INCLUDE [Node.js quickstart](includes/quickstarts/nodejs-sdk.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.jsの表記修正"
}
```

### Explanation
この変更は、`quickstart.md`ファイルにおいて、「NodeJS」という表記を「Node.js」に修正することを目的としています。この修正により、Node.jsの公式な表記に合わせた形となり、文書の一貫性が向上します。具体的には、プログラミング言語に関連するリソースの記載内容が整えられ、読者にとってよりわかりやすい内容となることを目指しています。この変更は、機能や手順に影響を与えるものではなく、主に表記に関する修正です。

## articles/ai-services/language-service/tutorials/prompt-flow.md{#item-22c24b}

<details>
<summary>Diff</summary>
````diff
@@ -21,10 +21,6 @@ This tutorial teaches you how to use Language in prompt flow utilizing [Azure AI
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 
-- You need an Azure AI Foundry hub or permissions to create one. Your user role must be **Azure AI Developer**, **Contributor**, or **Owner** on the hub. For more information, see [hubs](../../../ai-foundry/concepts/ai-resources.md) and [Azure AI roles](../../../ai-foundry/concepts/rbac-azure-ai-foundry.md).
-     - If your role is **Contributor** or **Owner**, you can [create a hub in this tutorial](#create-a-project-in-azure-ai-foundry-portal). 
-     - If your role is **Azure AI Developer**, the hub must already be created. 
-
 - Your subscription needs to be below your [quota limit](../../../ai-foundry/how-to/quota.md) to deploy a new flow in this tutorial.
 
 ## Create a project in Azure AI Foundry portal
````
</details>

### Summary

```json
{
    "modification_type": "bug fix",
    "modification_title": "不要な情報の削除"
}
```

### Explanation
この変更は、`prompt-flow.md`ファイルにおいて、チュートリアルの手順に関連する不要な情報を削除することを目的としています。具体的には、Azure AI Foundryのハブの作成に関する説明が簡略化され、役割に応じた要件が明確化されています。削除された内容には、役割に基づくハブの作成や権限に関する情報が含まれており、これによりドキュメントがスッキリし、ユーザーが必要な情報に集中できるようになっています。この変更は内容の実質的な意味合いを損なうことなく、文書の読みやすさと明確さを向上させる方向に寄与しています。


