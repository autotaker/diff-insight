---
date: '2026-01-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8434102...MicrosoftDocs:8d79be2
summary: 今回のコード変更では、主に既存のドキュメントの更新と新しいコンテンツの追加が行われました。特に、Microsoft Foundryの新機能紹介やクイックスタートガイドのマイナーアップデートが含まれています。また、リンクや文言の改善も実施され、ユーザーがAIソリューションをより直感的に活用できるようにサポートされています。全体として、ユーザーエクスペリエンスが向上し、開発者が新しい環境でより効果的にアプリケーションを開発できるようになっています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:8434102...MicrosoftDocs:8d79be2){target="_blank"}

<format>
# Highlights
今回のコード変更で主なハイライトは、既存のドキュメントの更新と新しいコンテンツの追加です。特に注目すべき点は、Microsoft Foundryの紹介を含む新機能の追加、元々のクイックスタートガイドの更新、リンクや文言の改善です。

## New features
- Microsoft Foundryに関する新しい紹介ドキュメントの追加
- Language Playgroundのレイアウトの説明追加
- Microsoft Foundryを利用する際の新しい前提条件ドキュメントの追加

## Breaking changes
- 特に破壊的な変更は行われていませんが、いくつかのテキストやリンクの更新が行われ、古いリンクを使用する箇所では情報の確認が必要です。

## Other updates
- 複数のクイックスタートガイド（C#, Python, Node.js, .NET, Java）のマイナーアップデート
- Markdown形式の調整、文言修正、リンク更新
- 不要な空白行の削除とドキュメントの構造改善

# Insights
今回のコード変更では、Microsoft Foundryの新しい機能を多くのドキュメントで説明し、具体的な利用方法と前提条件を明確にすることで、AIソリューションの開発者がこのプラットフォームを迅速かつ効果的に利用できるようにしています。

また、新しく追加されたドキュメントや更新されたリンクは、ユーザーがAIソリューションをより直感的に構築、管理、および展開できるようにサポートしています。特に新しい紹介文書では、Microsoft Foundryの概念と利用方法を詳しく説明し、ユーザーがこちらの環境を容易に試せるように設計されています。

さらに、クイックスタートガイドの更新により、利用者は最新のSDKとサービスへ迅速に移行できるようになり、コードサンプルや手順の読みやすさも向上しています。文書が整理され、内容が最新情報であることから、開発者は更新されたドキュメントを用いて、より精確にアプリケーションを開発できるようになりました。

このように今回の更新で多くの改善が施され、ユーザーエクスペリエンスが向上しています。特に、Microsoft Foundryを含むAzureのAIサービスの利用を促進し、スムーズかつ確実な導入と展開を支援する構成となっています。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [csharp-sdk.md](#item-50a434) | minor update | C# SDK クイックスタートの更新 | modified | 4 | 8 | 12 | 
| [introduction.md](#item-16c9eb) | new feature | Microsoft Foundry の紹介文書の追加 | added | 18 | 0 | 18 | 
| [playground-layout.md](#item-02346b) | new feature | Language Playground レイアウトの説明追加 | added | 22 | 0 | 22 | 
| [prerequisites-with-storage.md](#item-fd8f82) | new feature | ストレージを用いた前提条件の追加 | added | 19 | 0 | 19 | 
| [prerequisites.md](#item-e85bb5) | new feature | Microsoft Foundryの前提条件の追加 | added | 18 | 0 | 18 | 
| [tip-you-can-use-foundry.md](#item-f67565) | minor update | Microsoft Foundryのヒントドキュメントの名称変更 | renamed | 1 | 1 | 2 | 
| [python-sdk.md](#item-df8e49) | minor update | Python SDKの言語検出クイックスタートの更新 | modified | 7 | 19 | 26 | 
| [csharp-sdk.md](#item-1105f3) | minor update | .NET用名前付きエンティティ認識クイックスタートの更新 | modified | 4 | 13 | 17 | 
| [quickstart.md](#item-bee292) | minor update | オーケストレーションワークフローのクイックスタートの更新 | modified | 4 | 2 | 6 | 
| [csharp-sdk.md](#item-67858f) | minor update | 個人を特定できる情報検出クイックスタートの更新 | modified | 3 | 7 | 10 | 
| [java-sdk.md](#item-1f313c) | minor update | 個人を特定できる情報検出クイックスタートのJava SDKの更新 | modified | 3 | 6 | 9 | 
| [nodejs-sdk.md](#item-e367fd) | minor update | Node.js SDKを使用した個人を特定できる情報検出クイックスタートの更新 | modified | 12 | 15 | 27 | 
| [use-microsoft-foundry.md](#item-fc17a0) | minor update | Microsoft Foundryの使用に関する文言の修正 | modified | 2 | 1 | 3 | 
| [nodejs-sdk.md](#item-8bd4c1) | minor update | Node.js SDKを使用したテキスト要約アプリケーションのクイックスタートの更新 | modified | 3 | 6 | 9 | 
| [use-microsoft-foundry.md](#item-4c70b1) | minor update | Microsoft Foundryを使用した要約機能に関する文言の修正 | modified | 1 | 1 | 2 | 
| [quickstart.md](#item-9b06f2) | minor update | ヘルスケア向けテキスト分析クイックスタートのリンク修正 | modified | 2 | 3 | 5 | 


# Modified Contents
## articles/ai-services/language-service/entity-linking/includes/quickstarts/csharp-sdk.md{#item-50a434}

<details>
<summary>Diff</summary>
````diff
@@ -4,14 +4,14 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 12/11/2025
+ms.date: 01/07/2026
 ms.author: lajanuar
 ---
 [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet) | [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics)
 
 Use this quickstart to create an entity linking application with the client library for .NET. In the following example, you create a C# application that can identify and disambiguate entities found in text.
 
-[!INCLUDE [Use Microsoft Foundry](../../../includes/use-microsoft-foundry.md)]
+[!INCLUDE [Use Microsoft Foundry](../../../includes/microsoft-foundry/tip-you-can-use-foundry.md)]
 
 ## Prerequisites
 
@@ -33,12 +33,10 @@ Use this quickstart to create an entity linking application with the client libr
 
 ### Create a new .NET Core application
 
-Using the Visual Studio IDE, create a new .NET Core console app. This will create a "Hello World" project with a single C# source file: *program.cs*.
+Using the Visual Studio IDE, create a new .NET Core console app. This step creates a "Hello World" project with a single C# source file: *program.cs*.
 
 Install the client library by right-clicking the solution in the **Solution Explorer** and selecting **Manage NuGet Packages**. In the package manager that opens select **Browse** and search for `Azure.AI.TextAnalytics`. Select version `5.2.0`, and then **Install**. You can also use the [Package Manager Console](/nuget/consume-packages/install-use-packages-powershell#find-and-install-a-package).
 
-
-
 ## Code example
 
 Copy the following code into your *program.cs* file and run the code. 
@@ -141,11 +139,9 @@ Linked Entities:
 
 [!INCLUDE [clean up resources](../../../includes/clean-up-resources.md)]
 
-
-
 ## Next steps
 
 * [Entity linking language support](../../language-support.md)
 * [How to call the entity linking API](../../how-to/call-api.md)  
 * [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet)
-* [Additional samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples)
+* [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "C# SDK クイックスタートの更新"
}
```

### Explanation
本修正では、C# SDK クイックスタートのドキュメントが変更されました。具体的には、文書における数か所のテキストの修正や、リンクの更新が行われています。主な変更点は以下の通りです：

1. **日付の更新**: `ms.date`の値が「12/11/2025」から「01/07/2026」に変更され、最新の内容を示しています。
2. **リンクの修正**: 「Microsoft Foundry」の含有文において、使用されるリファレンスが更新され、正確な情報を提供するようになりました。
3. **文言の修正**: ドキュメント内のいくつかの文言が改善され、読者に対してより明確に手順を説明しています。例えば、「このステップは..."」という文が「このステップが…"」に修正されています。
4. **不要な空行の削除**: いくつかの不要な空行が削除され、全体の文書がよりコンパクトに整理されています。

これにより、全体的なドキュメントの質が向上し、ユーザーに対して効果的な情報提供が行われることを目的としています。

## articles/ai-services/language-service/includes/microsoft-foundry/introduction.md{#item-16c9eb}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+ title: include file
+ description: Microsoft foundry introductory paragraph
+ #services: cognitive-services
+ author: laujan
+ ms.service: azure-ai-language
+ ms.topic: include
+ ms.date: 12/18/2025
+ ms.author: lajanuar
+ms.custom: include
+---
+Microsoft Foundry offers a unified platform for building, managing, and deploying AI solutions with a wide array of models and tools. Foundry playgrounds are interactive environments within the Foundry portal designed for exploring, testing, and prototyping with various AI models and tools.
+
+> [!NOTE]
+>
+> * If you already have an Azure Language in Foundry Tools or multi-service resource—whether used on its own or through Language Studio—you can continue to use those existing Language resources within the Microsoft Foundry portal.
+> * For more information, see [How to use Foundry Tools in the Foundry portal](/azure/ai-services/connect-services-ai-foundry-portal).
+> * We highly recommended that you use a Foundry resource in the Foundry; however, you can also follow these instructions using a Language resource.
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Microsoft Foundry の紹介文書の追加"
}
```

### Explanation
本修正では、Microsoft Foundryに関する新しい紹介文書が追加されました。この文書は、AIソリューションの構築、管理、および展開のための統一プラットフォームを提供するMicrosoft Foundryの概要を説明しています。主な内容は以下の通りです：

1. **プラットフォームの機能**: Microsoft FoundryがいかにしてAIソリューションの開発を支援するかを紹介し、さまざまなモデルとツールを活用した開発環境を提供することに触れています。
2. **Foundry Playground**: Interactivityを特徴とするFoundry Playgroundについて説明し、AIモデルやツールを試すための環境としての役割を強調しています。
3. **利用に関する注意事項**: 既存のAzure Languageサービスやマルチサービスリソースの利用者に対して、Microsoft Foundryポータルでのリソースの利用継続についての情報を提供しています。
4. **推奨される利用法**: Foundryリソースを利用することが推奨されている一方で、Languageリソースを使って手順を進めることも可能であるとしています。

この文書の追加により、ユーザーがMicrosoft Foundryの基本的な理解を深め、AIソリューションをより効果的に活用できるようサポートしています。

## articles/ai-services/language-service/includes/microsoft-foundry/playground-layout.md{#item-02346b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,22 @@
+---
+ title: include file
+ description: Language playground layout and page orientation
+ #services: cognitive-services
+ author: laujan
+ ms.service: azure-ai-language
+ ms.topic: include
+ ms.date: 01/07/2026
+ ms.author: lajanuar
+ms.custom: include
+---
+
+## Understanding the Language playground layout
+
+The Language playground consists of four primary sections:
+
+- **Top banner**: Select from the available Language capabilities including language detection, entity recognition, sentiment analysis, Personally Identifiable Information (PII) detection, summarization, and conversational language understanding.
+- **Left pane**: Configure service options such as API version, model version, and capability-specific parameters (language selection, entity types, redaction policies).
+- **Center pane**: Enter or upload text for processing. Results display here after you execute the operation.
+- **Right pane**: View detailed operation results including entity categories, confidence scores, offsets, and JSON-formatted responses.
+
+After processing your text, select **View code** to access multilingual code samples in Python, C#, JavaScript, and other languages for integration into your applications.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Language Playground レイアウトの説明追加"
}
```

### Explanation
本修正では、Language Playgroundのレイアウトに関する新しい文書が追加されました。この文書は、Language Playgroundの構成要素と、それぞれの役割について詳細に説明しています。主な内容は以下の通りです：

1. **セクションの説明**: Language Playgroundは四つの主要なセクションから構成されています。
   - **トップバナー**: 言語検出、エンティティ認識、感情分析、個人識別情報（PII）検出、要約、会話型言語理解などの利用可能な言語機能を選択するための部分です。
   - **左ペイン**: サービスオプションを設定するためのエリアで、APIのバージョン、モデルのバージョン、機能特定のパラメータ（言語選択、エンティティタイプ、削除ポリシーなど）を構成できます。
   - **センターペイン**: 処理するテキストを入力またはアップロードする場所で、操作を実行した後はこの部分に結果が表示されます。
   - **右ペイン**: エンティティカテゴリ、信頼スコア、オフセット、JSON形式のレスポンスなどの詳細な操作結果を見ることができます。

2. **コードサンプルの提供**: テキストを処理した後に「コードを表示」を選択することで、Python、C#、JavaScriptなどの多言語のコードサンプルにアクセスでき、アプリケーションへの統合が容易になります。

この文書の追加により、ユーザーはLanguage Playgroundの使い方や各セクションの機能をより深く理解し、AIソリューションの開発に役立てることができるようになります。

## articles/ai-services/language-service/includes/microsoft-foundry/prerequisites-with-storage.md{#item-fd8f82}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,19 @@
+## Prerequisites
+
+* An **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+
+* The **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control).
+
+*  An [**Language resource with a storage account**](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics). On the **select additional features** page, select the **Custom text classification, Custom named entity recognition, Custom sentiment analysis & Custom Text Analytics for health** box to link a required storage account to this resource:
+
+    :::image type="content" source="../../media/foundry-next/select-additional-features.png" alt-text="Screenshot of the select additional features option in the Foundry.":::
+
+  > [!NOTE]
+  >  * You need to have an **owner** role assigned on the resource group to create a Language resource.
+  >  * If you're connecting a preexisting storage account, you should have an owner role assigned to it.
+  >  * Don't move the storage account to a different resource group or subscription once linked with Azure Language resource.
+
+
+* **A Foundry project created in the Foundry**. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
+
+* **A custom NER dataset uploaded to your storage container**. A custom named entity recognition (NER) dataset is the collection of labeled text documents used to train your custom NER model. You can [download our sample dataset](https://go.microsoft.com/fwlink/?linkid=2175226) for this quickstart. The source language is English.
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "ストレージを用いた前提条件の追加"
}
```

### Explanation
本修正では、Microsoft Foundryを使用する際の前提条件に関する新しい文書が追加されました。この文書は、ユーザーがプロジェクトを正常に構築および実行するために必要な要素を明示しています。主な内容は以下の通りです：

1. **Azureサブスクリプション**: ユーザーはAzureのサブスクリプションを持つ必要があり、持っていない場合は無料で作成する手続きについてのリンクが提供されています。

2. **必要な権限**: アカウントとプロジェクトを設定する者は、Azure AIアカウントオーナーの役割や、貢献者またはCognitive Services貢献者の役割を持っている必要があります。この要件についての詳細は、役割ベースのアクセス制御（RBAC）に関するリンクが参照されています。

3. **Languageリソースとストレージアカウント**: ユーザーは、カスタムテキスト分類やカスタムエンティティ認識などのためのストレージアカウントをリンクすることが求められます。これに関する手順と注意点が画像で示されています。具体的には、リソースグループにオーナー権限が必要であり、ストレージアカウントが他のリソースグループやサブスクリプションに移動されないようにすることが强调されています。

4. **Foundryプロジェクト**: Foundryプロジェクトの作成についての情報が提供され、独自のNERデータセットをストレージコンテナにアップロードする必要性が強調されています。サンプルデータセットのダウンロードリンクも含まれています。

この文書の追加により、ユーザーはFoundryを利用するための具体的な要件を理解し、必要な準備を整えることができるようになります。

## articles/ai-services/language-service/includes/microsoft-foundry/prerequisites.md{#item-e85bb5}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,18 @@
+---
+ title: include file
+ description: Microsoft foundry prerequisites
+ #services: cognitive-services
+ author: laujan
+ ms.service: azure-ai-language
+ ms.topic: include
+ ms.date: 12/18/2025
+ ms.author: lajanuar
+ms.custom: include
+---
+
+## Prerequisites
+
+* **Azure subscription**. If you don't have one, you can [create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
+* **Requisite permissions**. Make sure the person establishing the account and project is assigned as the Azure AI Account Owner role at the subscription level. Alternatively, having either the **Contributor** or **Cognitive Services Contributor** role at the subscription scope also meets this requirement. For more information, *see* [Role based access control (RBAC)](/azure/ai-foundry/openai/how-to/role-based-access-control#cognitive-services-contributor).
+*  [Foundry resource](/azure/ai-services/multi-service-resource). For more information, *see* [Configure a Foundry resource](../../../concepts/configure-azure-resources.md). Alternately, you can use a [Language resource](https://portal.azure.com/?Microsoft_Azure_PIMCommon=true#create/Microsoft.CognitiveServicesTextAnalytics).
+* **A Foundry project created in the Foundry**. For more information, *see* [Create a Foundry project](/azure/ai-foundry/how-to/create-projects).
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Microsoft Foundryの前提条件の追加"
}
```

### Explanation
この修正では、Microsoft Foundryを使用するための前提条件に関する新しい文書が追加されました。この文書は、ユーザーがFoundryを適切に利用するために必要な要素を示しています。主な内容は次の通りです：

1. **Azureサブスクリプション**: ユーザーはAzureのサブスクリプションを持つ必要があり、持っていない場合は無料で作成できるリンクが提供されています。

2. **必要な権限**: プロジェクトの設定を行う者は、Azure AIアカウントオーナーの役割が必要です。また、貢献者またはCognitive Services貢献者の役割も受けられます。これに関する詳細は役割ベースのアクセス制御（RBAC）についてのリンクが参照されています。

3. **Foundryリソース**: ユーザーはFoundryリソースを設定する必要があり、これに関する情報や構成手順へのリンクが含まれています。また、代替としてLanguageリソースの使用も提案されています。

4. **Foundryプロジェクト**: ユーザーはFoundry内にプロジェクトを作成する必要があり、このプロセスについての詳細な情報も提供されています。

この文書の追加により、Foundryを使うための具体的な準備が明示され、ユーザーが円滑にプロジェクトを開始できるようになります。

## articles/ai-services/language-service/includes/microsoft-foundry/tip-you-can-use-foundry.md{#item-f67565}

<details>
<summary>Diff</summary>
````diff
@@ -1,6 +1,6 @@
 ---
  title: include file
- description: include file
+ description: tip
  #services: cognitive-services
  author: laujan
  ms.service: azure-ai-language
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryのヒントドキュメントの名称変更"
}
```

### Explanation
この修正では、Microsoft Foundryに関するドキュメントのファイル名が変更され、説明も更新されました。具体的な変更点は以下の通りです：

1. **ファイル名の変更**: 元のファイル名「use-microsoft-foundry.md」から「tip-you-can-use-foundry.md」へと変更されました。この変更により、ドキュメントの内容がより明確に示されることを目的としています。

2. **説明の更新**: ファイルの説明も「include file」から「tip」に変更されました。この更新により、ドキュメントの目的が短く簡潔に表現され、ユーザーにとって理解しやすくなりました。

この変更により、Microsoft Foundryに関する情報が整理され、ユーザーが必要な情報を効率的に見つけられるようにする意図があります。

## articles/ai-services/language-service/language-detection/includes/quickstarts/python-sdk.md{#item-df8e49}

<details>
<summary>Diff</summary>
````diff
@@ -2,36 +2,26 @@
 author: laujan
 ms.service: azure-ai-language
 ms.topic: include
-ms.date: 11/18/2025
+ms.date: 01/07/2026
 ms.author: lajanuar
 ---
-[Reference documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?preserve-view=true&view=azure-python) | [More samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples) | [Package (PyPi)](https://pypi.org/project/azure-ai-textanalytics/5.2.0/) | [Library source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics)
-
-
-Use this quickstart to create a language detection application with the client library for Python. In the following example, you create a Python application that can identify the language a text sample was written in.
-
-[!INCLUDE [Use Microsoft Foundry](../../../includes/use-microsoft-foundry.md)]
-
+<!-- markdownlint-disable MD041 -->
+[Reference documentation](/python/api/azure-ai-textanalytics/azure.ai.textanalytics?preserve-view=true&view=azure-python) | [More samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics/samples) | [Package (PyPi)](https://pypi.org/project/azure-ai-textanalytics/5.2.0/) | [Library source code](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/textanalytics/azure-ai-textanalytics)Use this quickstart to create a language detection application with the client library for Python. In the following example, you create a Python application that can identify the language a text sample was written in.
+[!INCLUDE [Use Microsoft Foundry](../../../includes/microsoft-foundry/tip-you-can-use-foundry.md)]
 
 ## Prerequisites
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * [Python 3.8 or later](https://www.python.org/)
 
-
 ## Setting up
 
 [!INCLUDE [Create an Azure resource](../../../includes/create-resource.md)]
 
-
-
 [!INCLUDE [Get your key and endpoint](../../../includes/get-key-endpoint.md)]
 
-
-
 [!INCLUDE [Create environment variables](../../../includes/environment-variables.md)]
 
-
 ### Install the client library
 
 After installing Python, you can install the client library with:
@@ -40,10 +30,9 @@ After installing Python, you can install the client library with:
 pip install azure-ai-textanalytics==5.2.0
 ```
 
-
 ## Code example
 
-Create a new Python file and copy the below code. Then run the code.  
+Create a new Python file and copy the below code. Then run the code.
 
 ```python
 # This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"
@@ -53,11 +42,11 @@ language_endpoint = os.environ.get('LANGUAGE_ENDPOINT')
 from azure.ai.textanalytics import TextAnalyticsClient
 from azure.core.credentials import AzureKeyCredential
 
-# Authenticate the client using your key and endpoint 
+# Authenticate the client using your key and endpoint
 def authenticate_client():
     ta_credential = AzureKeyCredential(language_key)
     text_analytics_client = TextAnalyticsClient(
-            endpoint=language_endpoint, 
+            endpoint=language_endpoint,
             credential=ta_credential)
     return text_analytics_client
 
@@ -75,7 +64,6 @@ def language_detection_example(client):
 language_detection_example(client)
 ```
 
-
 ### Output
 
 ```console
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Python SDKの言語検出クイックスタートの更新"
}
```

### Explanation
この修正では、Python SDKを用いた言語検出のクイックスタートに関する文書が更新されました。変更内容は以下の通りです：

1. **日付の更新**: 文書の日付が「11/18/2025」から「01/07/2026」に変更されました。これは新しい情報の提供を示しています。

2. **ドキュメントの内容修正**: 文章の一部が削除され、他の部分ではMarkdownの記述体裁が調整されています。特に、使用するMicrosoft Foundryに関するインクルードファイルのパスが更新され、内容がより正確になっています。

3. **コードサンプルの整形**: コード例の説明文が若干の修正を受け、より読みやすくなりました。また、それに続くコードブロックの末尾にあたる部分も調整されています。

これらの変更により、言語検出のクイックスタートがより利用しやすく、正確な情報を提供することが狙いです。ユーザーは、この更新によって最新の情報をもとにアプリケーションを迅速に開発できるようになります。

## articles/ai-services/language-service/named-entity-recognition/includes/quickstarts/csharp-sdk.md{#item-1105f3}

<details>
<summary>Diff</summary>
````diff
@@ -6,40 +6,32 @@ ms.topic: include
 ms.date: 11/18/2025
 ms.author: lajanuar
 ---
+<!-- markdownlint-disable MD041 -->
 [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet) | [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics) 
 
-Use this quickstart to create a Named Entity Recognition (NER) application with the client library for .NET. In the following example, you will create a C# application that can identify [recognized entities](../../concepts/named-entity-categories.md) in text.
+Use this quickstart to create a Named Entity Recognition (NER) application with the client library for .NET. In the following example, you create a C# application that can identify [recognized entities](../../concepts/named-entity-categories.md) in text.
 
-[!INCLUDE [Use Microsoft Foundry](../../../includes/use-microsoft-foundry.md)]
+[!INCLUDE [Use Microsoft Foundry](../../../includes/microsoft-foundry/tip-you-can-use-foundry.md)]
 
 ## Prerequisites
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * The [Visual Studio IDE](https://visualstudio.microsoft.com/vs/)
 
-
-
 ## Setting up
 
-
 [!INCLUDE [Create an Azure resource](../../../includes/create-resource.md)]
 
-
-
 [!INCLUDE [Get your key and endpoint](../../../includes/get-key-endpoint.md)]
 
-
-
 [!INCLUDE [Create environment variables](../../../includes/environment-variables.md)]
 
-
 ### Create a new .NET Core application
 
-Using the Visual Studio IDE, create a new .NET Core console app. This creates a "Hello World" project with a single C# source file: *program.cs*.
+Using the Visual Studio IDE, create a new .NET Core console app. This step creates a "Hello World" project with a single C# source file: *program.cs*.
 
 Install the client library by right-clicking the solution in the **Solution Explorer** and selecting **Manage NuGet Packages**. In the package manager that opens select **Browse** and search for `Azure.AI.TextAnalytics`. Select version `5.2.0`, and then **Install**. You can also use the [Package Manager Console](/nuget/consume-packages/install-use-packages-powershell#find-and-install-a-package).
 
-
 ## Code example
 
 Copy the following code into your *program.cs* file and run the code.
@@ -85,7 +77,6 @@ namespace Example
 }
 ```
 
-
 ## Output
 
 ```console
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": ".NET用名前付きエンティティ認識クイックスタートの更新"
}
```

### Explanation
この修正は、.NET向けの名前付きエンティティ認識（NER）に関するクイックスタート文書に対する更新です。具体的な変更は以下の通りです：

1. **Markdown形式の調整**: ドキュメントの冒頭にMarkdownLintの無効化コマンドが追加され、Markdownの記述に関する形式統一が行われました。

2. **インクルードファイルのパス変更**: Microsoft Foundryに関するインクルードのパスが更新され、「../../../includes/use-microsoft-foundry.md」から「../../../includes/microsoft-foundry/tip-you-can-use-foundry.md」に変更され、最新の情報へリンクされています。

3. **文言の軽微な修整**: 「In the following example, you will create a C# application」から「In the following example, you create a C# application」へと、文言が修正されました。これにより、読者に対してより直接的な表現となっています。

これらの調整により、クイックスタートガイドはより最新の情報に基づき、および読みやすくなり、ユーザーが.NETを用いた名前付きエンティティ認識アプリケーションを効果的に構築できるようになっています。

## articles/ai-services/language-service/orchestration-workflow/quickstart.md{#item-bee292}

<details>
<summary>Diff</summary>
````diff
@@ -1,15 +1,17 @@
 ---
 title: Quickstart - Orchestration workflow
 titleSuffix: Foundry Tools
-description: Quickly start creating an AI model to connect your Conversational Language Understanding, question answering and LUIS applications.
+description: Quickly start creating an AI model to connect your Conversational Language Understanding, question answering applications.
 author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: quickstart
-ms.date: 11/18/2025
+ms.date: 01/07/2026
 ms.author: lajanuar
 ms.custom: language-service-clu, mode-other
 ---
+<!-- markdownlint-disable MD025 -->
+
 # Quickstart: Orchestration workflow
 
 Use this article to get started with Orchestration workflow projects using the REST API. Follow these steps to try out an example.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "オーケストレーションワークフローのクイックスタートの更新"
}
```

### Explanation
この修正では、オーケストレーションワークフローに関するクイックスタート記事が更新されました。具体的な変更は次の通りです：

1. **説明文の修正**: 記事の説明文が修正され、「Conversational Language Understanding, question answering, and LUIS applications」から「Conversational Language Understanding, question answering applications」に短縮されました。これにより、内容がより明確になり、情報が整理されました。

2. **日付の更新**: ドキュメントの日付が「11/18/2025」から「01/07/2026」に変更され、最新の情報が反映されています。

3. **Markdownの無効化**: MarkdownLintの無効化コマンドが追加され、特定の形式に対するチェックが無効化される設定が行われました。

4. **見出しの追加**: 記事の冒頭に「# Quickstart: Orchestration workflow」という見出しが追加され、文書の構造が明確になっています。これにより、読みやすさとナビゲーションが向上しました。

これらの変更により、クイックスタートガイドはより整理され、情報が最新化されており、ユーザーがオーケストレーションワークフローを容易に始めることができるように設計されています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/csharp-sdk.md{#item-67858f}

<details>
<summary>Diff</summary>
````diff
@@ -10,12 +10,12 @@ ms.custom:
   - ignite-2024
   - build-2025
 ---
+<!-- markdownlint-disable MD041 -->
 [Reference documentation](/dotnet/api/azure.ai.textanalytics?preserve-view=true&view=azure-dotnet) | [More samples](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics/samples) | [Package (NuGet)](https://www.nuget.org/packages/Azure.AI.TextAnalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-net/tree/master/sdk/textanalytics/Azure.AI.TextAnalytics)
 
 Use this quickstart to create a Personally Identifiable Information (PII) detection application with the client library for .NET. In the following example, you create a C# application that can identify [recognized sensitive information](../../concepts/entity-categories.md) in text.
 
-[!INCLUDE [Use Microsoft Foundry](../use-microsoft-foundry.md)]
-
+[!INCLUDE [Tip: use Microsoft Foundry](../use-microsoft-foundry.md)]
 
 ## Prerequisites
 
@@ -29,12 +29,10 @@ Use this quickstart to create a Personally Identifiable Information (PII) detect
 
 ### Create a new .NET Core application
 
-Using the Visual Studio IDE, create a new .NET Core console app. This creates a "Hello World" project with a single C# source file: *program.cs*.
+Using the Visual Studio IDE, create a new .NET Core console app. This step creates a "Hello World" project with a single C# source file: *program.cs*.
 
 Install the client library by right-clicking the solution in the **Solution Explorer** and selecting **Manage NuGet Packages**. In the package manager that opens select **Browse** and search for `Azure.AI.TextAnalytics`. Select version `5.2.0`, and then **Install**. You can also use the [Package Manager Console](/nuget/consume-packages/install-use-packages-powershell#find-and-install-a-package).
 
-
-
 ## Code example
 
 Copy the following code into your *program.cs* file and run the code.
@@ -90,8 +88,6 @@ namespace Example
 }
 ```
 
-
-
 ## Output
 
 ```console
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人を特定できる情報検出クイックスタートの更新"
}
```

### Explanation
この修正は、個人を特定できる情報（PII）検出に関するクイックスタートの記事に対する更新です。以下に具体的な変更点を示します：

1. **Markdown形式の調整**: ドキュメントの先頭にMarkdownLintの無効化コマンドが追加され、Markdownの特定の規則を回避する設定が行われました。

2. **インクルードファイルの文言修正**: 「Use Microsoft Foundry」というインクルードの文言が「Tip: use Microsoft Foundry」へと変更され、より実用的な情報が加わりました。

3. **文言の修整**: 「In the following example, you will create a C# application」という文が「In the following example, you create a C# application」に変更され、読者への直接的な表現に改められています。また、.NET Coreアプリケーションの作成手順も微修正されており、「This creates a "Hello World" project」から「This step creates a "Hello World" project」に改善されています。

4. **余分な行の削除**: 不要な空行が削除され、全体の文書の整合性と読みやすさが向上しています。

これらの変更によって、クイックスタートガイドはより明確で、ユーザーが個人を特定できる情報を検出するアプリケーションを簡単に開始できるようになりました。また、最新の情報を反映する形で改善されています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/java-sdk.md{#item-1f313c}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.custom:
   - ignite-2024
   - build-2025
 ---
+<!-- markdownlint-disable MD041 -->
 [Reference documentation](/java/api/overview/azure/ai-textanalytics-readme?preserve-view=true&view=azure-java-stable) | [More samples](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics/src/samples) | [Package (Maven)](https://mvnrepository.com/artifact/com.azure/azure-ai-textanalytics/5.2.0) | [Library source code](https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/textanalytics/azure-ai-textanalytics)
 
 Use this quickstart to create a Personally Identifiable Information (PII) detection application with the client library for Java. In the following example, you create a Java application that can identify [recognized sensitive information](../../concepts/entity-categories.md) in text.
@@ -40,11 +41,9 @@ Create a Maven project in your preferred IDE or development environment. Then ad
 </dependencies>
 ```
 
-
-
 ## Code example
 
-Create a Java file named `Example.java`. Open the file and copy the below code. Then run the code. 
+Create a Java file named `Example.java`. Open the file and copy the following code. Then run the code.
 
 ```java
 import com.azure.core.credential.AzureKeyCredential;
@@ -70,7 +69,7 @@ public class Example {
                 .buildClient();
     }
 
-    // Example method for detecting sensitive information (PII) from text 
+    // Example method for detecting sensitive information (PII) from text
     static void recognizePiiEntitiesExample(TextAnalyticsClient client)
     {
         // The text that need be analyzed.
@@ -86,8 +85,6 @@ public class Example {
 
 ```
 
-
-
 ## Output
 
 ```console
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "個人を特定できる情報検出クイックスタートのJava SDKの更新"
}
```

### Explanation
この修正は、Java SDKを使用した個人を特定できる情報（PII）検出に関するクイックスタートの記事に対する更新です。具体的な変更点は以下の通りです：

1. **Markdown形式の調整**: ドキュメントの先頭にMarkdownLintの無効化コマンドが追加され、特定のMarkdown規則が無視されるよう設定されています。

2. **リファレンスリンクの更新**: リファレンスドキュメント、追加サンプル、Mavenパッケージ、ライブラリのソースコードのリンクが記載されており、内容が最新のものにアップデートされています。

3. **文言の修整**: 「copy the below code」が「copy the following code」に修正され、より正確な表現に改善されています。

4. **空行の削除**: 不要な空行が削除され、全体の文書構造が整理されています。

5. **コメントの修正**: コード内のコメントが少し修正され、行末の余分なスペースが削除されています。

これらの変更によって、Javaを用いた個人を特定できる情報検出アプリケーションのクイックスタートガイドは、構造が整理されており、内容が最新化されているため、ユーザーがスムーズにアプリケーションを開発できるようになっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/quickstarts/nodejs-sdk.md{#item-e367fd}

<details>
<summary>Diff</summary>
````diff
@@ -2,39 +2,40 @@
 author: laujan
 ms.author: lajanuar
 manager: nitinme
-ms.date: 11/18/2025
+ms.date: 01/07/2026
 ms.service: azure-ai-language
 ms.topic: include
 ms.custom:
   - devx-track-js
   - ignite-2024
   - build-2025
 ---
-[Reference documentation](/javascript/api/overview/azure/ai-language-text-readme) | [More samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-language-text) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text) 
+<!-- markdownlint-disable MD041 -->
+[Reference documentation](/javascript/api/overview/azure/ai-language-text-readme) | [More samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text/samples/v1) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-language-text) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/cognitivelanguage/ai-language-text)
 
 Use this quickstart to create a Personally Identifiable Information (PII) detection application with the client library for Node.js. In the following example, you create a JavaScript application that can identify [recognized sensitive information](../../concepts/entity-categories.md) in text.
 
 ## Prerequisites
 
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * Once you have your Azure subscription, [create a Foundry resource](../../../../../ai-services/multi-service-resource.md?pivots=azportal).
-* [Node.js](https://nodejs.org/) v14 LTS or later
+* [Node.js](https://nodejs.org/) v14 `LTS` or later
 
 ## Setting up
 
 [!INCLUDE [Create environment variables](../../../includes/environment-variables.md)]
 
 ### Create a new Node.js application
 
-In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. 
+In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it.
 
 ```console
-mkdir myapp 
+mkdir myapp
 
 cd myapp
 ```
 
-Run the `npm init` command to create a node application with a `package.json` file. 
+Run the `npm init` command to create a node application with a `package.json` file.
 
 ```console
 npm init
@@ -48,11 +49,9 @@ Install the npm package:
 npm install @azure/ai-text-analytics
 ```
 
-
-
 ## Code example
 
-Open the file and copy the below code. Then run the code.
+Open the file and copy the following sample and run the code.
 
 ```javascript
 "use strict";
@@ -68,13 +67,13 @@ const documents = [ "The employee's phone number is (555) 555-5555." ];
 
 async function main() {
     console.log(`PII recognition sample`);
-  
+
     const client = new TextAnalyticsClient(endpoint, new AzureKeyCredential(key));
-  
+
     const documents = ["My phone number is 555-555-5555"];
-  
+
     const [result] = await client.analyze("PiiEntityRecognition", documents, "en");
-  
+
     if (!result.error) {
       console.log(`Redacted text: "${result.redactedText}"`);
       console.log("Pii Entities: ");
@@ -89,8 +88,6 @@ console.error("The sample encountered an error:", err);
 });
 ```
 
-
-
 ## Output
 
 ```console
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.js SDKを使用した個人を特定できる情報検出クイックスタートの更新"
}
```

### Explanation
この修正は、Node.js SDKを利用した個人を特定できる情報（PII）検出に関するクイックスタートの記事に対する更新です。具体的な変更点は以下の通りです：

1. **日付の更新**: `ms.date`の値が2025年11月18日から2026年1月7日に変更され、文書の日付が最新のものになりました。

2. **Markdown形式の調整**: ドキュメントの先頭にMarkdownLintの無効化コマンドが追加され、Markdownの特定の規則を無視する設定がされています。

3. **文言の修正**: ノードバージョンの表記を「v14 LTS or later」から「v14 `LTS` or later」に変更し、強調を加えています。また、サンプルコードの作成手順に関する説明文が「copy the below code」から「copy the following sample」に改められ、より適切な表現になっています。

4. **インデントと空行の整理**: コードブロック内の空行が管理され、全体的にコードの可読性が向上しています。

5. **追加の修正**: その他の軽微な文言修正と空白の整理が行われており、文書の流れがスムーズになっています。

これらの変更により、Node.jsを用いた個人を特定できる情報検出アプリケーションのクイックスタートガイドがより明確かつ整然とした内容になり、開発者は効果的に学習し、アプリケーションを構築できるようになっています。

## articles/ai-services/language-service/personally-identifiable-information/includes/use-microsoft-foundry.md{#item-fc17a0}

<details>
<summary>Diff</summary>
````diff
@@ -6,5 +6,6 @@ ms.date: 12/11/2025
 ms.author: lajanuar
 ms.custom: include, ignite-2024
 ---
+<!-- markdownlint-disable MD041 -->
 > [!TIP]
-> You can use [**Microsoft Foundry**](https://ai.azure.com/) to try Azure Language features without needing to write code.
+> You can try the [**Microsoft Foundry**](https://ai.azure.com/) platform to perform Azure Language tasks without the need to write code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryの使用に関する文言の修正"
}
```

### Explanation
この修正は、Microsoft Foundryを使用したAzure Language機能に関する文書の更新です。主な変更点は以下の通りです：

1. **Markdown形式の調整**: ドキュメントの先頭にMarkdownLintの無効化コマンドが追加され、特定のMarkdownの規則が無視されるようになっています。

2. **文言の修正**: Microsoft Foundryを使用する案内の文言が変更されました。具体的には、「You can use [**Microsoft Foundry**](https://ai.azure.com/) to try Azure Language features without needing to write code.」という表現から、「You can try the [**Microsoft Foundry**](https://ai.azure.com/) platform to perform Azure Language tasks without the need to write code.」に変更されています。これにより、焦点が「Azure Language機能を試す」から「Azure Language作業を実行する」へと移り、より明確な意図が示されています。

3. **構造の改善**: 文言の変更にともない、情報がよりスムーズに伝わるように整えられています。

これにより、ユーザーはMicrosoft Foundryを使用してAzure Language機能を簡単に体験できることが明確になり、利用の利便性が向上しています。

## articles/ai-services/language-service/summarization/includes/quickstarts/nodejs-sdk.md{#item-8bd4c1}

<details>
<summary>Diff</summary>
````diff
@@ -10,6 +10,7 @@ ms.custom:
   - ignite-2024
   - build-2025
 ---
+<!-- markdownlint-disable MD041 -->
 [Reference documentation](/javascript/api/overview/azure/ai-language-text-readme?view=azure-node-latest&preserve-view=true) | [Additional samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/textanalytics/ai-text-analytics/samples) | [Package (npm)](https://www.npmjs.com/package/@azure/ai-text-analytics/v/5.2.0-beta.1) | [Library source code](https://github.com/Azure/azure-sdk-for-js/tree/master/sdk/textanalytics/ai-text-analytics) 
 
 Use this quickstart to create a text summarization application with the client library for Node.js. In the following example, you create a JavaScript application that can summarize documents.
@@ -21,18 +22,14 @@ Use this quickstart to create a text summarization application with the client l
 * Azure subscription - [Create one for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn)
 * [Node.js](https://nodejs.org/) v16 LTS
 * Once you have your Azure subscription, [create a Foundry resource](../../../../../ai-services/multi-service-resource.md?pivots=azportal).
-    * You need the key and endpoint from the resource you create to connect your application to the API. You paste your key and endpoint into the code below later in the quickstart.
-    * You can use the free pricing tier (`Free F0`) to try the service, and upgrade later to a paid tier for production.
+  * You need the key and endpoint from the resource you create to connect your application to the API. You paste your key and endpoint into the code below later in the quickstart.
+  * You can use the free pricing tier (`Free F0`) to try the service, and upgrade later to a paid tier for production.
 * To use the Analyze feature, you need a Language resource with the standard (S) pricing tier.
 
-
-
 ## Setting up
 
 [!INCLUDE [Create environment variables](../../../includes/environment-variables.md)]
 
-
-
 ### Create a new Node.js application
 
 In a console window (such as cmd, PowerShell, or Bash), create a new directory for your app, and navigate to it. 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Node.js SDKを使用したテキスト要約アプリケーションのクイックスタートの更新"
}
```

### Explanation
この修正は、Node.js SDKを用いてテキスト要約アプリケーションを作成するためのクイックスタートガイドに対する軽微な更新です。主な変更点は以下の通りです：

1. **Markdown形式の調整**: ドキュメントの先頭にMarkdownLintの無効化コマンドが追加され、特定のMarkdownのルールが無視されるようになっています。

2. **文言の整形**: 必要なリソースとその利用方法に関しての文言が再構成されています。特に、キーとエンドポイントに関する指示がリスト形式に変更され、より明確に示されています。

3. **空白の管理**: コード例や手順の間にあった不要な空行が削除され、文書全体を通して流れがスムーズになっています。

これらの変更により、ユーザーはNode.js SDKを使用してテキスト要約アプリケーションを構築する際のインストラクションがより明確になり、理解しやすくなっています。特に、必要なリソースに関する詳しい説明が強調されることで、ユーザーはスムーズにアプリケーションを設定できるようになることが期待されます。

## articles/ai-services/language-service/summarization/includes/use-microsoft-foundry.md{#item-4c70b1}

<details>
<summary>Diff</summary>
````diff
@@ -10,4 +10,4 @@
 ms.custom: include, build-2024, ignite-2024
 ---
 > [!TIP]
-> You can use [**Microsoft Foundry**](https://ai.azure.com/) to try summarization without needing to write code. 
+> You can try the [**Microsoft Foundry**](https://ai.azure.com/) platform to perform summarization tasks without the need to write code.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Microsoft Foundryを使用した要約機能に関する文言の修正"
}
```

### Explanation
この修正は、Microsoft Foundryを使用して要約作業を行う方法に関する文書の軽微な更新です。主な変更点は以下の通りです：

1. **文言の修正**: Microsoft Foundryの利用方法についての表現が変更されました。元の文は「You can use [**Microsoft Foundry**](https://ai.azure.com/) to try summarization without needing to write code.」でしたが、新しい表現では「You can try the [**Microsoft Foundry**](https://ai.azure.com/) platform to perform summarization tasks without the need to write code.」に変更されています。この修正により、「試す」という言葉から「実行する」という表現に焦点が移り、より具体的な指示が与えられています。

2. **構造の改善**: 文言の変更に伴い、情報がより直感的に伝わるように調整されています。この改善により、ユーザーはMicrosoft Foundryを通じて要約するタスクを簡単に理解し、実行できるようになります。

これらの変更により、ユーザーは要約作業の実行方法についてより明確な理解を得られることを目的としています。

## articles/ai-services/language-service/text-analytics-for-health/quickstart.md{#item-9b06f2}

<details>
<summary>Diff</summary>
````diff
@@ -15,11 +15,12 @@ ms.custom: language-service-health, mode-api, devx-track-extended-java, devx-tra
 keywords: text mining, health, text analytics for health
 zone_pivot_groups: programming-languages-text-analytics
 ---
+<!-- markdownlint-disable MD025 -->
 # Quickstart: Using Text Analytics for health client library and REST API
 
 This article contains Text Analytics for health quickstarts that help with using the supported client libraries, C#, Java, NodeJS, and Python and the REST API.
 
-[!INCLUDE [Use Microsoft Foundry](../includes/use-microsoft-foundry.md)]
+[!INCLUDE [Use Microsoft Foundry](../includes/microsoft-foundry/tip-you-can-use-foundry.md)]
 ::: zone pivot="programming-language-csharp"
 
 [!INCLUDE [C# quickstart](includes/quickstarts/csharp-sdk.md)]
@@ -63,8 +64,6 @@ To clean up and remove an Azure AI resource, you can delete either the individua
 * [Azure portal](../../multi-service-resource.md?pivots=azportal#clean-up-resources)
 * [Azure CLI](../../multi-service-resource.md?pivots=azcli#clean-up-resources)
 
-
-
 ## Next steps
 
 * [How to call the hosted API](./how-to/call-api.md)
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ヘルスケア向けテキスト分析クイックスタートのリンク修正"
}
```

### Explanation
この修正は、ヘルスケア向けテキスト分析に関するクイックスタートガイドの軽微な更新です。主な変更点は以下の通りです：

1. **MarkdownLintコマンドの追加**: ドキュメントの先頭に「<!-- markdownlint-disable MD025 -->」というコマンドが追加され、特定のMarkdownのルールが無視されるようになっています。これにより、標準のMarkdownのルールに従わずに内容を調整できるようになります。

2. **リンクの修正**: Microsoft Foundryに関するインクルード文が変更されました。元のリンクは「../includes/use-microsoft-foundry.md」でしたが、新しいリンクは「../includes/microsoft-foundry/tip-you-can-use-foundry.md」に修正されています。これにより、関連情報にアクセスしやすくなっています。

3. **空白行の削除**: 文書内の不要な空白行が削除され、文書のレイアウトが整理されています。これにより、全体的にスムーズな読みやすさが向上しています。

これらの変更によって、ユーザーは最新の情報をより簡単に取得でき、文章の流れも改善されています。特に、Microsoft Foundryに関するリンクの修正により、関連リソースへのアクセスがより直感的になっています。


