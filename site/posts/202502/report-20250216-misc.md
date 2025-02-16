---
date: '2025-02-16'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f
summary: このコードの変更には、新しい機能の追加や目次の更新、セキュリティに関する改善が含まれています。特に、`toc.yml`ファイルの更新により、ナビゲーションが改善され、ユーザーが新しいコンテンツにアクセスしやすくなりました。新たにAzure
  AI Foundryに関する記事が追加され、プロジェクト管理や生成AIアプリケーションの情報が強化されています。一方で、目次の大幅な更新に伴い、リンクの変更が発生する可能性があるため、ユーザーは注意が必要です。また、セキュリティ情報が統一され、地域情報や入力ガイダンスが更新されました。全体として、これらの変更はユーザーの利便性とセキュリティの向上を目指しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:b07793e...MicrosoftDocs:1cff62f){target="_blank"}

# Highlights

このコードの変更には、新しい機能の追加や目次の大幅な更新、セキュリティに関する記述の改善、および地域情報や入力ガイダンスの更新が含まれています。特に、`toc.yml`ファイルの更新は、既存のコンテンツの再構成や新しいセクションの追加により、ナビゲーションが大きく改善されました。

## New features

- 2025年1月のAzure AI Foundryに関する新しい記事の追加。これには、プロジェクトの監視と管理、生成AIアプリケーションに関する新しい記事などが含まれます。

## Breaking changes

- `toc.yml`ファイルの大幅な更新は、目次構造の変更を伴い、リンクが変わる可能性があるため、ユーザー遷移に影響を及ぼす可能性があります。

## Other updates

- セキュリティに関する注意事項が統一的な形式で更新されました（例えば、各SDKごとにAzure Key Vaultに関する説明がインクルードファイルで提供されるようになりました）。
- 入力ガイダンスの更新により、文書インテリジェンスのサポート形式に関する情報が充実しました。
- リソース地域に関する情報が簡潔化され、文書の焦点が絞られました。
- ドキュメントの日付の更新により、情報の鮮度が保持されています。

# Insights

今回の変更は、ユーザーの利便性とセキュリティの向上を図るために設計されました。特に、セキュリティ情報の標準化は、開発者がより安全な方法でAzureサービスを利用できるようにするための重要なステップです。Azure Key Vaultに関する情報を共通のインクルードファイルから参照することで、従来の警告文をより効果的に置き換え、情報にすばやくアクセスしやすくしています。

`toc.yml`の大幅な更新は、Azure AI Foundryの最新情報をユーザーに提供しやすくするためです。この結果、ユーザーは新しい機能やチュートリアルにすぐにアクセスできると同時に、ナビゲーションの効率も向上します。しかし、リンクの変更に伴う潜在的な問題については注意が必要で、適切な情報提供が求められます。

また、新たに追加されたAzure AI Foundryの記事は、ユーザーがプロジェクト管理やAIモデルの活用において最新のベストプラクティスを学び、実装できるよう支援しています。こうした情報更新は、プロダクトの利用価値を高め、ユーザーエクスペリエンスを向上させる上で不可欠です。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [retrieval-augmented-generation.md](#item-c42dcc) | minor update | リソース地域情報の更新 | modified | 0 | 1 | 1 | 
| [layout.md](#item-f7c4c8) | minor update | 入力ガイダンスの更新 | modified | 28 | 1 | 29 | 
| [csharp-sdk.md](#item-ee69c7) | minor update | Azure Key Vaultに関する重要事項の更新 | modified | 1 | 2 | 3 | 
| [java-sdk.md](#item-166b2e) | minor update | Azure Key Vaultに関する注意事項の更新 | modified | 1 | 2 | 3 | 
| [javascript-sdk.md](#item-615fcd) | minor update | Azure Key Vaultに関する注意事項の更新 | modified | 1 | 2 | 3 | 
| [python-sdk.md](#item-83c83f) | minor update | Azure Key Vaultに関する注意事項の更新 | modified | 1 | 2 | 3 | 
| [sdk-overview-v2-1.md](#item-c5f5c7) | minor update | Azure Key Vaultのインクルードファイルの変更 | modified | 1 | 1 | 2 | 
| [create-manage-compute-session.md](#item-6ed743) | minor update | ドキュメントの日付の更新 | modified | 1 | 1 | 2 | 
| [vscode.md](#item-24bd97) | minor update | VS Codeに関する手順の修正と日付の更新 | modified | 4 | 3 | 7 | 
| [toc.yml](#item-2745cd) | breaking change | 目次ファイルの大幅な更新 | modified | 222 | 321 | 543 | 
| [whats-new-ai-foundry.md](#item-769cf0) | new feature | Azure AI Foundryの1月2025年度新機能に関する記事の追加 | added | 32 | 0 | 32 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/retrieval-augmented-generation.md{#item-c42dcc}

<details>
<summary>Diff</summary>
````diff
@@ -119,7 +119,6 @@ If you're looking for a specific section in a document, you can use semantic chu
 
 ```python
 
-# Using SDK targeting 2024-11-30 (GA), make sure your resource is in one of these regions: East US, West US2, West Europe
 # pip install azure-ai-documentintelligence==1.0.0b1
 # pip install langchain langchain-community azure-ai-documentintelligence
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "リソース地域情報の更新"
}
```

### Explanation
この変更は、文書の特定のセクションにアクセスするための方法を示すコード例の一部を修正したものです。具体的には、使用するSDKの対象バージョンに関するコメントから、利用可能なリソース地域の情報が削除されました。削除された部分は、「2024-11-30 (GA)をターゲットとしたSDKを使用する場合、リソースが次の地域のいずれかにあることを確認してください: East US, West US2, West Europe」という内容でした。この変更により、情報が簡潔になり、コードのインストール手順に焦点が当てられました。

## articles/ai-services/document-intelligence/prebuilt/layout.md{#item-f7c4c8}

<details>
<summary>Diff</summary>
````diff
@@ -610,7 +610,34 @@ Document Intelligence v2.1 supports the following tools, applications, and libra
 
 ## Input guidance
 
-[!INCLUDE [input requirements](./../includes/input-requirements.md)]
+Supported file formats:
+
+|Model | PDF |Image: </br>`JPEG/JPG`, `PNG`, `BMP`, `TIFF`, `HEIF` | Microsoft Office: </br> Word (`DOCX`), Excel (`XLSX`), PowerPoint (`PPTX`), HTML|
+|--------|:----:|:-----:|:---------------:|
+|Read            | ✔    | ✔    | ✔  |
+|Layout          | ✔  | ✔ |   |
+|General&nbsp;Document| ✔  | ✔ |   |
+|Prebuilt        |  ✔  | ✔ |   |
+|Custom extraction |  ✔  | ✔ |   |
+|Custom classification  |  ✔  | ✔ | ✔  |
+
+* For best results, provide one clear photo or high-quality scan per document.
+
+* For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).
+
+* The file size for analyzing documents is 500 MB for paid (S0) tier and `4` MB for free (F0) tier.
+
+* Image dimensions must be between 50 pixels x 50 pixels and 10,000 pixels x 10,000 pixels.
+
+* If your PDFs are password-locked, you must remove the lock before submission.
+
+* The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about `8` point text at 150 dots per inch (DPI).
+
+* For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.
+
+  * For custom extraction model training, the total size of training data is 50 MB for template model and `1` GB for the neural model.
+
+  * For custom classification model training, the total size of training data is `1` GB  with a maximum of 10,000 pages. For 2024-11-30 (GA), the total size of training data is `2` GB with a maximum of 10,000 pages.
 
 :::moniker-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "入力ガイダンスの更新"
}
```

### Explanation
この変更では、文書インテリジェンスの入力ガイダンスが大幅に更新されました。具体的には、対応するファイル形式とそれぞれの処理能力に関する詳細な表が追加されました。この表には、PDFや画像（JPEG、PNGなど）、Microsoft Officeのファイル形式に対するサポート状況が含まれています。また、各フォーマットの処理条件、推奨されるファイルサイズやページ数の制限、さらにカスタムモデルのトレーニングに関する要件が詳述されています。

変更前の内容は、入力要件を示す包括的なサンプルを参照する形でしたが、今回の更新により、ユーザーは具体的な入力形式や制約を一目で確認することができるようになりました。これにより、ユーザーは必要な情報を迅速に取得し、文書解析に向けた準備を整えることが容易になります。

## articles/ai-services/document-intelligence/quickstarts/includes/csharp-sdk.md{#item-ee69c7}

<details>
<summary>Diff</summary>
````diff
@@ -170,8 +170,7 @@ To interact with the Form Recognizer service, you need to create an instance of
 
     * [**Prebuilt model**](#prebuilt-model)
 
-> [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../../../ai-services/security-features.md).
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 <!-- ### [.NET Command-line interface (CLI)](#tab/cli)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultに関する重要事項の更新"
}
```

### Explanation
この変更では、C# SDKを使用してForm Recognizerサービスと対話する際のセキュリティに関する重要な注意事項が更新されました。具体的には、以前は直接的な警告文が記載されていた部分が、Azure Key Vaultに関する共通のインクルードファイルを参照する形に変更されました。この参照により、ユーザーは暗号キーや資格情報を安全に保管し、アクセスするためのより効果的な方法を簡単に探すことができます。

結果として、この更新はセキュリティのベストプラクティスを強調し、開発者がコード内のキーを誤って公開しないようにするための指針を明確化しています。また、関連リンクを含むことで、ユーザーが追加情報にすぐにアクセスできる利便性も向上しています。

## articles/ai-services/document-intelligence/quickstarts/includes/java-sdk.md{#item-166b2e}

<details>
<summary>Diff</summary>
````diff
@@ -246,8 +246,7 @@ To interact with the Document Intelligence service, you need to create an instan
 
 :::moniker-end
 
-> [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../../../ai-services/security-features.md).
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 ## Layout model
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultに関する注意事項の更新"
}
```

### Explanation
この変更では、Java SDKを使用してDocument Intelligenceサービスと対話する際のセキュリティに関する注意事項が更新されました。具体的には、以前は「重要」な注意点として直接的な警告文が記載されていましたが、現在ではAzure Key Vaultに関する共通のインクルードファイルを参照する形式に変更されています。この更新により、ユーザーは資格情報を安全に保管し、アクセスするためのより効果的な指針を得られるようになっています。

この措置は、開発者がコード内のキーを安全に管理し、間違って公開しないよう促すものであり、セキュリティのベストプラクティスを強調する全体的な文脈の一部です。また、追加情報へのリンクを含むことで、ユーザーが関連するセキュリティ機能について迅速に学ぶことができる利点も提供されています。

## articles/ai-services/document-intelligence/quickstarts/includes/javascript-sdk.md{#item-615fcd}

<details>
<summary>Diff</summary>
````diff
@@ -129,8 +129,7 @@ Recognizer `endpoint`.
 
     * [**Prebuilt Invoice**](#prebuilt-model)
 
-> [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../../../ai-services/security-features.md).
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 <!-- markdownlint-disable MD036 -->
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultに関する注意事項の更新"
}
```

### Explanation
この変更では、JavaScript SDKを用いてRecognizerエンドポイントと対話する際のセキュリティに関する注意事項が更新されました。変更前は、ユーザーに対してキーをコードから削除し、公開しないように警告する文が直接記載されていましたが、変更後はAzure Key Vaultへのリンクを含む共通のインクルードファイルを参照する形式へと更新されました。

この改訂は、資格情報の安全な保管とアクセス方法についてのベストプラクティスを強調し、ユーザーが適切な情報を迅速に得られるようにしています。このアプローチにより、開発者は自分のコード内の機密情報をより安全に管理することができ、セキュリティの重要性を再確認することが促されています。

## articles/ai-services/document-intelligence/quickstarts/includes/python-sdk.md{#item-83c83f}

<details>
<summary>Diff</summary>
````diff
@@ -109,8 +109,7 @@ To interact with the Document Intelligence service, you need to create an instan
 
 :::moniker-end
 
-> [!IMPORTANT]
-> Remember to remove the key from your code when you're done, and never post it publicly. For production, use a secure way of storing and accessing your credentials like [Azure Key Vault](/azure/key-vault/general/overview). For more information, *see* Azure AI services [security](../../../../ai-services/security-features.md).
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 <!-- markdownlint-disable MD036 -->
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultに関する注意事項の更新"
}
```

### Explanation
この変更では、Python SDKを使用してDocument Intelligenceサービスと対話する際のセキュリティに関する注意事項が更新されました。以前は、ユーザーに対してキーをコードから削除し、公開しないように警告する具体的な文が記載されていましたが、現在はAzure Key Vaultに関連する共通のインクルードファイルを参照する形式に改訂されました。

このアップデートにより、ユーザーは資格情報を安全に管理し、効果的にアクセスする方法についての指針を得ることができます。特に、セキュリティのベストプラクティスを強調することで、開発者が自分のコード内の機密情報を適切に扱う重要性を再認識できるようになっています。この変更は、文書全体のセキュリティ強化に寄与するものです。

## articles/ai-services/document-intelligence/v21/sdk-overview-v2-1.md{#item-c5f5c7}

<details>
<summary>Diff</summary>
````diff
@@ -144,7 +144,7 @@ Here's where to find your Document Intelligence API key in the Azure portal:
 
 :::image type="content" source="../media/containers/keys-and-endpoint.png" alt-text="Screenshot of the keys and endpoint location in the Azure portal.":::
 
-[!INCLUDE [Microsoft Entra ID or AKV](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv.md)]
+[!INCLUDE [Azure key vault](~/reusable-content/ce-skilling/azure/includes/ai-services/security/microsoft-entra-id-akv-expanded.md)]
 
 ### [C#/.NET](#tab/csharp)
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure Key Vaultのインクルードファイルの変更"
}
```

### Explanation
この変更では、Azure AIサービスのDocument Intelligence APIキーの見つけ方に関するセクションが更新されました。具体的には、クイックスタートガイド内で使用されるインクルードファイルが更新され、Microsoft Entra IDまたはAzure Key Vaultのリンクが新しいインクルードファイルに置き換えられました。

変更前は、Microsoft Entra IDまたはAzure Key Vaultの情報を参照していましたが、現行の文書ではAzure Key Vaultに関する詳しい説明が含まれる新しいファイルを指し示すようになっています。この更新により、利用者はAzure Key Vaultのセキュリティ機能についての情報をより深く理解しやすくなります。また、更新内容は、ユーザーのセキュリティ意識を高めるのに寄与することが期待されます。

## articles/ai-studio/how-to/create-manage-compute-session.md{#item-6ed743}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 02/12/2025
+ms.date: 02/14/2025
 ms.reviewer: lochen
 ms.author: sgilley
 author: sdgilley
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
この変更では、ドキュメントの最終更新日が変更されています。具体的には、元の更新日である2025年2月12日から2025年2月14日に調整されました。この変更は、文書の内容が更新されたことを反映し、ユーザーが最新の情報を把握できるようにするためのものです。

日付の更新は、文書の正確性を保つために重要であり、使用される情報の信頼性を向上させる役割を果たします。このような小さな修正でも、技術文書における透明性やユーザーへの信頼感は高まるため、定期的な見直しが推奨されます。

## articles/ai-studio/how-to/develop/vscode.md{#item-24bd97}

<details>
<summary>Diff</summary>
````diff
@@ -9,7 +9,7 @@ ms.custom:
   - build-2024
   - ignite-2024
 ms.topic: how-to
-ms.date: 10/30/2024
+ms.date: 02/14/2025
 ms.reviewer: lebaro
 ms.author: sgilley
 author: sdgilley
@@ -31,7 +31,8 @@ Azure AI Foundry supports developing in VS Code - Desktop and Web. In each scena
 1. For **Compute**, select an existing compute instance or create a new one.
     * Select a compute instance to use. If it's stopped, select **Start compute** and wait for it to switch to **Running**. You'll see a **Ready** status when the compute is ready for use.
     * If you don't have a compute instance, select **Create compute**.  Then enter a name, compute details, and select **Create compute**. Wait until the compute instance is ready.
-1. For **VS Code container**, select **Set up container** once the button enables. This configures the container on the compute for you. The container setup might take a few minutes to complete. Once you set up the container for the first time, you can directly launch subsequent times. You might need to authenticate your compute when prompted. When setup is complete, you'll see **Ready**.
+1. If prompted, select **Authenticate** to authenticate your compute instance.
+1. For **VS Code container**, select **Set up container** once the button enables. This configures the container on the compute for you. The container setup might take a few minutes to complete. Once you set up the container for the first time, you can directly launch subsequent times. When setup is complete, you'll see **Ready**.
 
     > [!WARNING]
      > Even if you [enable idle shutdown on your compute instance](../create-manage-compute.md#configure-idle-shutdown), idle shutdown will not occur for any compute that is set up with this custom VS Code container. This is to ensure the compute doesn't shut down unexpectedly while you're working within a container.
@@ -59,7 +60,7 @@ This table summarizes the folder structure:
 | `shared` | Use for working with a project's shared files and assets such as prompt flows.<br/><br/>For example, `shared\Users\{user-name}\promptflow` is where you find the project's prompt flows. |
 
 > [!IMPORTANT]
-> It's recommended that you work within this project directory. Files, folders, and repos you include in your project directory persist on your host machine (your compute instance). Files stored in the code and data folders will persist even when the compute instance is stopped or restarted, but will be lost if the compute is deleted. However, the shared files are saved in your hub's storage account, and therefore aren't lost if the compute instance is deleted.
+> It's recommended that you work within this project directory. Files, folders, and repos you include in your project directory persist on your host machine (your compute instance). Files stored in the code and data folders persist even when the compute instance is stopped or restarted, but are lost if the compute is deleted. However, the shared files are saved in your hub's storage account, and therefore aren't lost if the compute instance is deleted.
 
 ## Working with prompt flows
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "VS Codeに関する手順の修正と日付の更新"
}
```

### Explanation
この変更では、VS Codeを使用した開発に関する手順が修正され、日付が更新されました。具体的には、ドキュメント内の手順が一部再構成され、特に認証プロセスに関する説明が強調されています。

新しい手順では、「認証を求められた場合は、**Authenticate**を選択」と明記され、ユーザーに対して必要なアクションが示されています。また、VS Codeのコンテナを設定する際の手順も引き続き記載されていますが、手順番号が調整され、流れがよりクリアになっています。

さらに、ドキュメントの最終更新日が2024年10月30日から2025年2月14日に変更されており、情報が最新であることを反映しています。このような小さな修正や日付の更新は、ユーザーが適切で信頼性のある情報にアクセスできるようにするための重要な一手です。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -3,34 +3,54 @@ items:
   href: index.yml
 - name: What is Azure AI Foundry?
   href: what-is-ai-studio.md
+- name: What's new in Azure AI Foundry?
+  href: whats-new-ai-foundry.md
 - name: Get started
+- name: Overview
   expanded: true
   items:
-  - name: Quickstarts
-    items:
-    - name: Use the chat playground
-      href: quickstarts/get-started-playground.md
-    - name: Build app in Python with Azure AI Foundry SDK
-      href: quickstarts/get-started-code.md
-    - name: Get started with Azure AI Foundry SDK
-      href: how-to/develop/sdk-overview.md
-  - name: Tutorials
+  - name: What is Azure AI Foundry?
+    href: what-is-ai-studio.md
+  - name: Azure AI Foundry architecture
+    href: concepts/architecture.md
+  - name: Azure OpenAI in Azure AI Foundry
+    href: azure-openai-in-ai-studio.md
+  - name: Management center
+    href: concepts/management-center.md
+  - name: Azure AI Foundry SDK
+    href: how-to/develop/sdk-overview.md
+    displayName: code, sdk
+  - name: Region support
+    href: reference/region-support.md
+  - name: Azure AI FAQ
+    href: faq.yml
+  - name: Which studio should I choose?
+    href: /ai/ai-studio-experiences-overview?context=/azure/ai-studio/context/context
+- name: Quickstarts
+  items:
+  - name: Use the chat playground
+    href: quickstarts/get-started-playground.md
+  - name: Build a chat app using the Azure AI SDK
+    href: quickstarts/get-started-code.md
+    displayName: code
+  - name: Get started using Azure OpenAI Assistants
+    href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
+- name: Tutorials
+  items:
+  - name: Deploy an enterprise chat web app
+    href: tutorials/deploy-chat-web-app.md
+  - name: Build a custom chat app with the Azure AI Foundry SDK
     items:
-    - name: Build a custom chat app with Azure AI Foundry SDK
-      items:
-        - name: "Part 1: Set up project and install SDK"
-          href: tutorials/copilot-sdk-create-resources.md
-        - name: "Part 2: Build with data retrieval"
-          href: tutorials/copilot-sdk-build-rag.md
-          displayName: code,sdk
-        - name: "Part 3: Evaluate the chat app"
-          href: tutorials/copilot-sdk-evaluate.md
-          displayName: code,sdk
-    - name: Deploy an enterprise chat web app
-      href: tutorials/deploy-chat-web-app.md
-    - name: Build a RAG solution using Azure AI Search
-      href: /azure/search/tutorial-rag-build-solution?context=/azure/ai-studio/context/context
-- name: Explore AI model capabilities
+      - name: "Part 1: Set up project and install SDK"
+        href: tutorials/copilot-sdk-create-resources.md
+      - name: "Part 2: Build with data retrieval"
+        href: tutorials/copilot-sdk-build-rag.md
+        displayName: code,sdk
+      - name: "Part 3: Evaluate the chat app"
+        href: tutorials/copilot-sdk-evaluate.md
+        displayName: code,sdk
+- name: How-to
+  expanded: true
   items:
   - name: Azure OpenAI and AI services
     items:
@@ -53,8 +73,6 @@ items:
         href: ../ai-services/openai/assistants-quickstart.md?context=/azure/ai-studio/context/context
       - name: Use GPT-4o in the real-time audio playground
         href: ../ai-services/openai/realtime-audio-quickstart.md?context=/azure/ai-studio/context/context
-      - name: Analyze images and video with GPT-4 for Vision in the playground
-        href: quickstarts/multimodal-vision.md
     - name: Azure AI Speech
       items:
       - name: Real-time speech to text
@@ -92,6 +110,34 @@ items:
     - name: Distillation
       href: concepts/concept-model-distillation.md
     - name: Azure OpenAI models
+      items:
+      - name: Deploy Azure OpenAI models
+        href: how-to/deploy-models-openai.md
+      - name: Fine-tune Azure OpenAI models
+        href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
+    - name: Healthcare AI models
+      items:
+        - name: Foundational AI models for healthcare
+          href: how-to/healthcare-ai/healthcare-ai-models.md
+        - name: MedImageInsight - embedding model
+          href: how-to/healthcare-ai/deploy-medimageinsight.md
+        - name: CXRReportGen - text generation model
+          href: how-to/healthcare-ai/deploy-cxrreportgen.md
+        - name: MedImageParse - prompted segmentation model
+          href: how-to/healthcare-ai/deploy-medimageparse.md
+    - name: Microsoft Phi family models
+      items:
+        - name: Phi-3 chat models
+          href: how-to/deploy-models-phi-3.md
+        - name: Phi-3 chat model with vision
+          href: how-to/deploy-models-phi-3-vision.md
+        - name: Phi-3.5 chat model with vision
+          href: how-to/deploy-models-phi-3-5-vision.md
+        - name: Phi-4 chat models
+          href: how-to/deploy-models-phi-4.md
+        - name: Fine-tune Phi-3 chat models
+          href: how-to/fine-tune-phi-3.md
+    - name: Cohere models
       items:
       - name: Cohere Command models
         href: how-to/deploy-models-cohere-command.md
@@ -101,119 +147,55 @@ items:
         href: how-to/deploy-models-cohere-rerank.md
     - name: DeepSeek-R1 reasoning models
       href: how-to/deploy-models-deepseek.md
-    - name: Gretel Navigator model
-      href: how-to/deploy-models-gretel-navigator.md
-    - name: Healthcare AI models
-      items:
-      - name: Foundational AI models for healthcare
-        href: how-to/healthcare-ai/healthcare-ai-models.md
-      - name: MedImageInsight - embedding model
-        href: how-to/healthcare-ai/deploy-medimageinsight.md
-      - name: CXRReportGen - text generation model
-        href: how-to/healthcare-ai/deploy-cxrreportgen.md
-      - name: MedImageParse - prompted segmentation model
-        href: how-to/healthcare-ai/deploy-medimageparse.md
-    - name: JAIS model
-      href: how-to/deploy-models-jais.md
     - name: Meta Llama models
       items:
       - name: Meta Llama family models
         href: how-to/deploy-models-llama.md
       - name: Fine-tune Meta Llama family models
         href: how-to/fine-tune-model-llama.md
-    - name: Microsoft Phi family models
-      items:
-      - name: Phi-3 chat models
-        href: how-to/deploy-models-phi-3.md
-      - name: Phi-3 chat model with vision
-        href: how-to/deploy-models-phi-3-vision.md
-      - name: Phi-3.5 chat model with vision
-        href: how-to/deploy-models-phi-3-5-vision.md
-      - name: Phi-4 chat models
-        href: how-to/deploy-models-phi-4.md
-      - name: Fine-tune Phi-3 chat models
-        href: how-to/fine-tune-phi-3.md
     - name: Mistral family models
       items:
-      - name: Mistral premium models
-        href: how-to/deploy-models-mistral.md
-      - name: Codestral model
-        href: how-to/deploy-models-mistral-codestral.md
-      - name: Mistral Nemo model
-        href: how-to/deploy-models-mistral-nemo.md
-      - name: Mistral-7B and Mixtral models
-        href: how-to/deploy-models-mistral-open.md
+        - name: Mistral premium models
+          href: how-to/deploy-models-mistral.md
+        - name: Codestral model
+          href: how-to/deploy-models-mistral-codestral.md
+        - name: Mistral Nemo model
+          href: how-to/deploy-models-mistral-nemo.md
+        - name: Mistral-7B and Mixtral models
+          href: how-to/deploy-models-mistral-open.md
       displayName: maas
-    - name: NTTDATA tsuzumi model
-      items:
-        - name: NTTDATA tsuzumi model
-          href: how-to/deploy-models-tsuzumi.md
-        - name: Fine-tune tsuzumi model
-          href: how-to/fine-tune-models-tsuzumi.md
+    - name: Gretel Navigator model
+      href: how-to/deploy-models-gretel-navigator.md
+    - name: JAIS model
+      href: how-to/deploy-models-jais.md
+    - name: AI21 Jamba models
+      href: how-to/deploy-models-jamba.md
     - name: TimeGEN-1 model
       href: how-to/deploy-models-timegen-1.md
-  - name: Azure OpenAI and AI services
+    - name: NTTDATA tsuzumi model
+      href: how-to/deploy-models-tsuzumi.md
+    - name: Fine-tune tsuzumi model
+      href: how-to/fine-tune-models-tsuzumi.md
+  - name: Deploy AI models
     items:
-    - name: Use Azure OpenAI Service in Azure AI Foundry portal
-      href: ai-services/how-to/connect-azure-openai.md
-    - name: Use Azure AI services in Azure AI Foundry portal
-      href: ai-services/how-to/connect-ai-services.md
-      displayName: cognitive,task
-    - name: What are Azure AI services?
-      href: concepts/what-are-ai-services.md
-    - name: Azure OpenAI
-      items:
-      - name: Deploy Azure OpenAI models
-        items: 
-        - name: Azure OpenAI in Azure AI Foundry
-          href: azure-openai-in-ai-studio.md
-        - name: Model region availability
-          href:  ../ai-services/openai/concepts/models.md?context=/azure/ai-studio/context/context
-          displayName: OpenAI, gpt-4o, gpt-4o-mini, whisper
-        - name: Deployment types
-          href: ../ai-services/openai/how-to/deployment-types.md?context=/azure/ai-studio/context/context
-          displayName: provisioned, global standard, datazone, data zone, global data zone, batch, globalbatch
-        - name: Model deployment
-          href: how-to/deploy-models-openai.md
-      - name: Generate text
-        items:
-        - name: Batch
-          href: ../ai-services/openai/how-to/batch.md?context=/azure/ai-studio/context/context
-          displayName: OpenAI, global batch, globalbatch, chat, chat completions
-        - name: Reasoning models
-          href: ../ai-services/openai/how-to/reasoning.md?context=/azure/ai-studio/context/context
-          displayName: OpenAI, o1, o1-mini, o3-mini, reasoning effort
-        - name: Function calling
-          href: ../ai-services/openai/how-to/function-calling.md?context=/azure/ai-studio/context/context
-          displayName: OpenAI 
-        - name: Predicted outputs
-          href: ../ai-services/openai/how-to/predicted-outputs.md?context=/azure/ai-studio/context/context 
-        - name: Prompt caching
-          href: ../ai-services/openai/how-to/prompt-caching.md?context=/azure/ai-studio/context/context 
-        - name: Structured outputs
-          href: ../ai-services/openai/how-to/structured-outputs.md?context=/azure/ai-studio/context/context 
-        - name: Use vision-enabled chat
-          href:  ../ai-services/openai/gpt-v-quickstart.md?context=/azure/ai-studio/context/context
-      - name: Generate images
-        href: ../ai-services/openai/dall-e-quickstart.md?context=/azure/ai-studio/context/context
-        displayName: OpenAI, DALLE, dall-e, DALL-E
-      - name: Audio
+      - name: Deployments overview
+        href: concepts/deployments-overview.md
+        displayName: endpoint
+      - name: Azure AI model inference
         items:
-          - name: Use GPT-4o in the real-time audio playground
-            href: ../ai-services/openai/realtime-audio-quickstart.md?context=/azure/ai-studio/context/context
-            displayName: OpenAI, realtime, real-time
-          - name: Audio generation
-            href: ../ai-services/openai/audio-completions-quickstart.md?context=/azure/ai-studio/context/context 
-      - name: Distillation (stored completions)
-        href: ../ai-services/openai/how-to/stored-completions.md?context=/azure/ai-studio/context/context
-        displayName: OpenAI, Azure OpenAI, stored completions, model distillation
-      - name: Embeddings
-        href: ../ai-services/openai/tutorials/embeddings.md?context=/azure/ai-studio/context/context
-        displayName: text-embedding-ada-002, text-embedding-3-large, text-embedding-3-small
-      - name: Evaluation
-        href: ../ai-services/openai/how-to/evaluations.md?context=/azure/ai-studio/context/context
-        displayName: OpenAI
-      - name: Fine-tuning
+        - name: What is the Azure AI model inference service?
+          href: ../ai-foundry/model-inference/overview.md?context=/azure/ai-studio/context/context
+        - name: Upgrade from GitHub Models
+          href: ../ai-foundry/model-inference/how-to/quickstart-github-models.md?context=/azure/ai-studio/context/context
+        - name: Add and configure models
+          href: ../ai-foundry/model-inference/how-to/create-model-deployments.md?context=/azure/ai-studio/context/context
+        - name: Deployment types
+          href: ../ai-foundry/model-inference/concepts/deployment-types.md?context=/azure/ai-studio/context/context
+        - name: Use the inference endpoint
+          href: ../ai-foundry/model-inference/concepts/endpoints.md?context=/azure/ai-studio/context/context
+        - name: Quotas and limits
+          href: ../ai-foundry/model-inference/quotas-limits.md?context=/azure/ai-studio/context/context
+      - name: Serverless API
         items:
         - name: Deploy models as serverless API
           href: how-to/deploy-models-serverless.md
@@ -240,116 +222,103 @@ items:
       href: how-to/develop/create-hub-project-sdk.md
     - name: Create a hub with custom security
       items:
-      - name: Azure Image Analysis
-        items:
-        - name: What is Image Analysis?
-          href: /azure/ai-services/computer-vision/overview-image-analysis?context=/azure/ai-studio/context/context
-        - name: Quickstart
-          href: /azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40?context=/azure/ai-studio/context/context
-        - name: Optical Character Recognition concepts
-          href: /azure/ai-services/computer-vision/concept-ocr?context=/azure/ai-studio/context/context
-        - name: Image captioning concepts
-          href: /azure/ai-services/computer-vision/concept-describe-images-40?context=/azure/ai-studio/context/context
-      - name: Azure AI Face
-        items:
-        - name: What is Azure AI Face service?
-          href: /azure/ai-services/computer-vision/overview-identity?context=/azure/ai-studio/context/context
-        - name: Quickstart 
-          href: /azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library?context=/azure/ai-studio/context/context
-        - name: Face detection concepts
-          href: /azure/ai-services/computer-vision/concept-face-detection?context=/azure/ai-studio/context/context
-        - name: Face recognition concepts
-          href: /azure/ai-services/computer-vision/concept-face-recognition?context=/azure/ai-studio/context/context
-        - name: Liveness detection tutorial
-          href: /azure/ai-services/computer-vision/tutorials/liveness?context=/azure/ai-studio/context/context
-- name: Solutions
-  items:
-  - name: Agents
+      - name: Create a hub in the Azure portal
+        href: how-to/create-secure-ai-hub.md
+      - name: Create a hub from template
+        href: how-to/create-azure-ai-hub-template.md
+        displayName: code
+      - name: Create a hub using Terraform
+        href: how-to/create-hub-terraform.md
+
+    - name: Create and manage compute
+      href: how-to/create-manage-compute.md
+  - name: Connections
     items:
-    - name: What is Azure AI Agent Service
-      href: ../ai-services/agents/overview.md?context=/azure/ai-studio/context/context
-    - name: "Quickstart: Create a new agent"
-      href: ../ai-services/agents/quickstart.md?context=/azure/ai-studio/context/context
-  - name: Azure AI Search for RAG
+    - name: Connections overview
+      href: concepts/connections.md
+    - name: Create a connection
+      href: how-to/connections-add.md
+    - name: Create a connection using the Azure Machine Learning SDK
+      href: how-to/develop/connections-add-sdk.md
+      displayName: code
+  - name: Data for your generative AI app
     items:
-    - name: Retrieval Augmented Generation (RAG) overview
+    - name: Overview of retrieval augmented generation (RAG)
       href: concepts/retrieval-augmented-generation.md
-    - name: Use Azure AI Search
-      href: /azure/search/search-what-is-azure-search?context=/azure/ai-studio/context/context
-    - name: Build and consume vector indexes (Portal)
+      displayName: RAG
+    - name: Add data to your project
+      href: how-to/data-add.md
+      displayName: index
+    - name: Build and consume vector indexes
       href: how-to/index-add.md
-    - name: Build and consume vector indexes (Code)
+    - name: Build and consume indexes using code
       href: how-to/develop/index-build-consume-sdk.md
-    - name: Build a RAG solution using Azure AI Search
-      href: /azure/search/tutorial-rag-build-solution?context=/azure/ai-studio/context/context
-  - name: Develop with code
-    items:
-    - name: Work with projects in VS Code
-      href: how-to/develop/vscode.md
-    - name: Start with an AI template
-      href: how-to/develop/ai-template-get-started.md
-    - name: Develop with LangChain
-      href: how-to/develop/langchain.md
-    - name: Develop with LlamaIndex
-      href: how-to/develop/llama-index.md
-      displayName: code,sdk
-    - name: Develop with Semantic Kernel
-      href: how-to/develop/semantic-kernel.md
-  - name: Model inference
-    items:
-    - name: What is Azure AI model inference?
-      href: ../ai-foundry/model-inference/overview.md?context=/azure/ai-studio/context/context
-    - name: Upgrade from GitHub Models
-      href: ../ai-foundry/model-inference/how-to/quickstart-github-models.md?context=/azure/ai-studio/context/context
-    - name: Add and configure models
-      href: ../ai-foundry/model-inference/how-to/create-model-deployments.md?context=/azure/ai-studio/context/context
-    - name: Use the inference endpoint
-      href: ../ai-foundry/model-inference/concepts/endpoints.md?context=/azure/ai-studio/context/context
-  - name: Deployments
-    items:
-    - name: Deploying models in Azure AI Foundry
-      href: concepts/deployments-overview.md
-    - name: Deploy models as serverless API
-      href: how-to/deploy-models-serverless.md
-    - name: Deploy models via managed compute
-      href: how-to/deploy-models-managed.md
-    - name: Consume serverless API models from a different project or hub
-      href: how-to/deploy-models-serverless-connect.md
-      displayName: maas, paygo, models-as-a-service
-    - name: Model and region availability for Serverless API deployments
-      href: how-to/deploy-models-serverless-availability.md
-    - name: Quotas and limits
-      href: ai-services/concepts/quotas-limits.md
-    - name: Troubleshoot deployments and monitoring
-      href: how-to/troubleshoot-deploy-and-monitor.md
-- name: Optimizations
-  items:
-  - name: Prompt engineering
-    items:
-    - name: Prompt engineering techniques
-      href: ../ai-services/openai/concepts/prompt-engineering.md?context=/azure/ai-studio/context/context
-    - name: Image prompt engineering
-      href: ../ai-services/openai/concepts/gpt-4-v-prompt-engineering.md?context=/azure/ai-studio/context/context
     - name: Synthetic Data Generation
       href: concepts/concept-synthetic-data.md
-  - name: Fine-tuning
-    items:
-    - name: Fine-tuning in Azure AI Foundry
-      href: concepts/fine-tuning-overview.md
-    - name: Fine-tune with a managed compute
-      href: how-to/fine-tune-managed-compute.md
-    - name: Fine-tune Azure OpenAI models
-      href: ../ai-services/openai/how-to/fine-tuning.md?context=/azure/ai-studio/context/context
-    - name: Distillation
-      href: concepts/concept-model-distillation.md
-  - name: Tracing
+      displayName: code,sdk
+  - name: Develop generative AI apps
     items:
-    - name: Tracing in Azure AI Foundry
-      href: concepts/trace.md
-    - name: Trace your application with Azure AI Inference SDK
-      href: how-to/develop/trace-local-sdk.md
-    - name: Visualize your traces
-      href: how-to/develop/visualize-traces.md
+    - name: Develop in Azure AI Foundry portal
+      items:
+      - name: Build apps with prompt flow
+        items:
+        - name: Prompt flow overview
+          href: how-to/prompt-flow.md
+        - name: Develop flows
+          items:
+          - name: Create and manage compute session
+            href: how-to/create-manage-compute-session.md
+          - name: Create a flow
+            href: how-to/flow-develop.md
+          - name: Tune prompts using variants
+            href: how-to/flow-tune-prompts-using-variants.md
+          - name: Process images in a flow
+            href: how-to/flow-process-image.md
+          - name: Use prompt flow tools
+            items:
+            - name: Prompt flow tools overview
+              href: how-to/prompt-flow-tools/prompt-flow-tools-overview.md
+            - name: LLM tool
+              href: how-to/prompt-flow-tools/llm-tool.md
+            - name: Prompt tool
+              href: how-to/prompt-flow-tools/prompt-tool.md
+            - name: Python tool
+              href: how-to/prompt-flow-tools/python-tool.md
+            - name: Azure OpenAI GPT-4 Turbo with Vision tool
+              href: how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md
+            - name: Index Lookup tool
+              href: how-to/prompt-flow-tools/index-lookup-tool.md
+            - name: Rerank tool
+              href: how-to/prompt-flow-tools/rerank-tool.md
+            - name: Content Safety tool
+              href: how-to/prompt-flow-tools/content-safety-tool.md
+            - name: Embedding tool
+              href: how-to/prompt-flow-tools/embedding-tool.md
+            - name: Serp API tool
+              href: how-to/prompt-flow-tools/serp-api-tool.md
+        - name: Troubleshoot prompt flow
+          href: how-to/prompt-flow-troubleshoot.md
+    - name: Develop with code
+      items:
+      - name: Work with projects in VS Code
+        href: how-to/develop/vscode.md
+      - name: Start with an AI template
+        href: how-to/develop/ai-template-get-started.md
+      - name: Develop with LangChain
+        href: how-to/develop/langchain.md
+      - name: Develop with LlamaIndex
+        href: how-to/develop/llama-index.md
+        displayName: code,sdk
+      - name: Develop with Semantic Kernel 
+        href: how-to/develop/semantic-kernel.md
+    - name: Trace generative AI apps
+      items:
+       - name: Tracing overview
+         href: concepts/trace.md 
+       - name: Trace your application with Azure AI Inference SDK
+         href: how-to/develop/trace-local-sdk.md
+       - name: Visualize your traces
+         href: how-to/develop/visualize-traces.md
   - name: Evaluate generative AI apps
     items:
     - name: Evaluations concepts
@@ -378,96 +347,24 @@ items:
           href: how-to/flow-bulk-test-evaluation.md
         - name: Develop an evaluation flow in Prompt flow
           href: how-to/flow-develop-evaluation.md
-    - name: A/B experimentation
+    - name: A/B experimentation 
       href: concepts/a-b-experimentation.md
-  - name: Build apps with prompt flow
-    items:
-    - name: Prompt flow overview
-      href: how-to/prompt-flow.md
-    - name: Develop flows
-      items:
-      - name: Create and manage compute session
-        href: how-to/create-manage-compute-session.md
-      - name: Create a flow
-        href: how-to/flow-develop.md
-      - name: Tune prompts using variants
-        href: how-to/flow-tune-prompts-using-variants.md
-      - name: Process images in a flow
-        href: how-to/flow-process-image.md
-      - name: Use prompt flow tools
-        items:
-        - name: Prompt flow tools overview
-          href: how-to/prompt-flow-tools/prompt-flow-tools-overview.md
-        - name: LLM tool
-          href: how-to/prompt-flow-tools/llm-tool.md
-        - name: Prompt tool
-          href: how-to/prompt-flow-tools/prompt-tool.md
-        - name: Python tool
-          href: how-to/prompt-flow-tools/python-tool.md
-        - name: Azure OpenAI GPT-4 Turbo with Vision tool
-          href: how-to/prompt-flow-tools/azure-open-ai-gpt-4v-tool.md
-        - name: Index Lookup tool
-          href: how-to/prompt-flow-tools/index-lookup-tool.md
-        - name: Rerank tool
-          href: how-to/prompt-flow-tools/rerank-tool.md
-        - name: Content Safety tool
-          href: how-to/prompt-flow-tools/content-safety-tool.md
-        - name: Embedding tool
-          href: how-to/prompt-flow-tools/embedding-tool.md
-        - name: Serp API tool
-          href: how-to/prompt-flow-tools/serp-api-tool.md
-    - name: Deploy and monitor generative AI apps
-      items:
-      - name: Continuously monitor your applications
-        href: how-to/monitor-applications.md
-      - name: Deploy and monitor flows
-        items:
-        - name: Deploy a flow for real-time inference
-          href: how-to/flow-deploy.md
-          displayName: endpoint
-        - name: Enable tracing and collect feedback for a flow deployment
-          href: how-to/develop/trace-production-sdk.md
-          displayName: code
-        - name: Monitor prompt flow deployments
-          href: how-to/monitor-quality-safety.md
-        - name: Troubleshoot prompt flow
-          href: how-to/prompt-flow-troubleshoot.md
-- name: Management center
-  items:
-  - name: Management center overview
-    href: concepts/management-center.md
-  - name: Manage projects and hubs
+  - name: Deploy and monitor generative AI apps
     items:
-    - name: Create a project
-      href: how-to/create-projects.md
-    - name: Hubs and projects overview
-      href: concepts/ai-resources.md
-    - name: Create your first hub
-      href: how-to/create-azure-ai-resource.md
-    - name: Create a hub using the Azure Machine Learning SDK and CLI
-      href: how-to/develop/create-hub-project-sdk.md
-    - name: Create a hub with custom security
+    - name: Continuously monitor your applications
+      href: how-to/monitor-applications.md
+    - name: Deploy and monitor flows
       items:
-      - name: Create a hub in the Azure portal
-        href: how-to/create-secure-ai-hub.md
-      - name: Create a hub from template
-        href: how-to/create-azure-ai-hub-template.md
+      - name: Deploy a flow for real-time inference
+        href: how-to/flow-deploy.md
+        displayName: endpoint
+      - name: Enable tracing and collect feedback for a flow deployment
+        href: how-to/develop/trace-production-sdk.md
         displayName: code
-      - name: Create a hub using Terraform
-        href: how-to/create-hub-terraform.md
-  - name: Create and manage compute
-    href: how-to/create-manage-compute.md
-  - name: Connections
-    items:
-    - name: Connections overview
-      href: concepts/connections.md
-    - name: Create a connection
-      href: how-to/connections-add.md
-    - name: Create a connection using the Azure Machine Learning SDK
-      href: how-to/develop/connections-add-sdk.md
-      displayName: code
-  - name: Add and manage data in Azure AI Foundry
-    href: how-to/data-add.md
+      - name: Monitor prompt flow deployments
+        href: how-to/monitor-quality-safety.md
+      - name: Troubleshoot deployments and monitoring
+        href: how-to/troubleshoot-deploy-and-monitor.md
   - name: Costs and quotas
     items:
     - name: Plan and manage costs
@@ -522,7 +419,7 @@ items:
   items:
   - name: Responsible AI overview
     href: responsible-use-of-ai-overview.md
-  - name: Azure AI Content Safety in AI Foundry portal overview
+  - name: What is Azure AI Content Safety?
     href: ai-services/content-safety-overview.md
   - name: Content safety for models deployed with serverless APIs
     href: concepts/model-catalog-content-safety.md
@@ -554,19 +451,15 @@ items:
   - name: Azure AI services REST APIs
     displayName: swagger http
     href: ../ai-services/reference/rest-api-resources.md?context=/azure/ai-studio/context/context
+  - name: Prompt flow Python SDK
+    href: https://microsoft.github.io/promptflow/reference/index.html#
   - name: Azure AI Model Inference API
     href: ../ai-foundry/model-inference/reference/reference-model-inference-api.md
   - name: Azure Policy built-ins
     displayName: samples, policies, definitions
     href: ../ai-services/policy-reference.md?context=/azure/ai-studio/context/context
-  - name: Region support
-    href: reference/region-support.md
 - name: Resources
   items:
-  - name: Azure AI FAQ
-    href: faq.yml
-  - name: Azure AI Foundry architecture
-    href: concepts/architecture.md
   - name: Support & help options
     href: ../ai-services/cognitive-services-support-options.md?context=/azure/ai-studio/context/context
   - name: Use Azure AI Foundry with a screen reader
@@ -583,3 +476,11 @@ items:
     href: https://azure.microsoft.com/support/legal/sla/cognitive-services/v1_1/
   - name: Azure Government
     href: /azure/azure-government/compare-azure-government-global-azure
+  - name: Videos
+    href: https://azure.microsoft.com/resources/videos/index/?services=cognitive-services
+  - name: Azure Blog
+    href: https://azure.microsoft.com/blog/
+  - name: Artificial Intelligence and Machine Learning Blog
+    href: https://techcommunity.microsoft.com/t5/artificial-intelligence-and/ct-p/AI
+  - name: LLMOps with Prompt Flow
+    href: https://github.com/microsoft/llmops-promptflow-template
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "目次ファイルの大幅な更新"
}
```

### Explanation
この変更では、`toc.yml`ファイルが大幅に修正され、新しいセクションが追加され、既存のコンテンツが削除または reorganized されました。追加および削除されたライン数からも分かるように、構造が大きく変わっています。

特に、Azure AI Foundryに関連する新しい項目やチュートリアルが追加され、ユーザーが追加機能や手順にアクセスしやすくなっています。例えば、「What's new in Azure AI Foundry?」という新しいトピックが追加され、その後のセクションには、各種のチュートリアルや手順に関するリンクが強調されています。また、以前の内容の整理や統合も行われ、ユーザーが情報を見つけやすくなっています。

このような大規模な変更は、ドキュメントのナビゲーションや全体的な体験を改善するために重要です。しかし、内容が大幅に変わったため、既存のリンクが正しく機能しない可能性があり、ユーザーにとっては混乱を招く可能性もあります。そのため、変更が実施された場合は、ユーザーに適切な注意喚起を行うことが推奨されます。

## articles/ai-studio/whats-new-ai-foundry.md{#item-769cf0}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,32 @@
+---
+title: "Azure AI Foundry docs: What's new for January 2025"
+description: "What's new in the Azure AI Foundry docs for January 2025."
+ms.author: smcdowell
+author: skpmcdowell
+ms.topic: whats-new
+ms.subject: ai-studio
+ms.custom: January-2025
+ms.date: 02/14/2025
+---
+
+# Azure AI Foundry docs: What's new for January 2025
+
+Welcome to what's new in the Azure AI Foundry docs for January 2025. This article lists some of the major changes to docs during this period.
+
+
+## Azure AI Foundry
+
+### New articles
+
+- [Audit and manage Azure AI Foundry hubs and projects](../ai-studio/how-to/azure-policy.md)
+- [Continuously monitor your generative AI applications](../ai-studio/how-to/monitor-applications.md)
+- [How to use Codestral chat model](../ai-studio/how-to/deploy-models-mistral-codestral.md)
+- [How to use DeepSeek-R1 reasoning model](../ai-studio/how-to/deploy-models-deepseek.md)
+- [How to use Gretel Navigator chat model](../ai-studio/how-to/deploy-models-gretel-navigator.md)
+
+### Updated articles
+
+- [How to use Phi-4 family chat models](../ai-studio/how-to/deploy-models-phi-4.md)
+
+
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "Azure AI Foundryの1月2025年度新機能に関する記事の追加"
}
```

### Explanation
この変更では、Azure AI Foundryに関する新しい機能と更新情報をまとめた文書が追加されました。この文書は、2025年1月の主要な変更点を明記しており、ユーザーが新しい情報にアクセスしやすくなるよう設計されています。

具体的には、文書は以下の内容を含んでいます：
- 新たに追加された記事として、「Azure AI Foundryハブとプロジェクトの監査と管理」、「生成AIアプリケーションの継続的な監視」、「Codestralチャットモデルの使用方法」、「DeepSeek-R1推論モデルの使用方法」、「Gretel Navigatorチャットモデルの使用方法」などがリストされています。
- また、「Phi-4ファミリーのチャットモデルの使用方法」に関する既存の記事も更新されたことが示されています。

このような形で新情報が整理されることで、ユーザーはAzure AI Foundryの最新情報を簡単に把握し、必要なリソースへ迅速にアクセスできるようになります。新しい機能や更新が明確に提示されることで、プロダクトの利用価値が高まります。


