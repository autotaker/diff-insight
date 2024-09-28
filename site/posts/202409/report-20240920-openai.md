---
date: '2024-09-20'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:daa818e
summary: 今回の変更は、ドキュメント `articles/ai-services/openai` に含まれる複数のファイルに対する重要な修正であり、著者情報や日付の更新、手順の明確化、APIエンドポイントの変更、ならびに画像の追加および削除が含まれています。特に、新しいチャットビューやプレイグラウンドの画像が追加され、古い画像が削除されたことにより、視覚的説明が失われる可能性があります。これらの修正はユーザーがAzure
  OpenAIやAIスタジオをより効率的に利用できるように設計されており、技術文書の信頼性と関連性を高めるための取り組みが反映されています。
title: Diff Insight Report - openai

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:e496207...MicrosoftDocs:daa818e){target="_blank"}

# ハイライト
ドキュメント `articles/ai-services/openai` に属する複数のファイルの変更が行われました。主要な変更点としては、著者情報や日付の更新、各ドキュメントのセクションや手順の明確化、APIエンドポイントの変更、ならびに新しい画像の追加や削除が含まれます。

## 新機能
- **`articles/ai-services/openai/media/quickstarts/chat-view-code.png`と`chat-playground.png`**：新しいチャットビューやプレイグラウンドに関する画像が追加されました。

## 破壊的変更
- **`column-options.png`、`assistant-session.png`、`assistants-playground.png`と`assistants-studio.png`**：これらの画像が削除されました。これによって、これまで視覚的に説明されていた内容が失われ、ユーザーの理解が困難になる可能性があります。

## その他の更新
- **著者および日付の更新**：複数のファイルで著者情報やリリース日付が最新の日付に更新されました。
- **手順の明確化**：`quota.md`や`working-with-models.md`などでデプロイメント手順やクォータの項目が明確化されました。
- **APIエンドポイントの変更**：`api-surface.md`では、旧エンドポイント「completions」が「chat/completions」に変更されました。
- **画像の更新**：複数のドキュメントで画像が最新の情報に基づいて修正されました。

# 洞察
今回の大幅なドキュメント変更は、ユーザーがAzure OpenAIとAIスタジオをより効率的に利用するための利便性向上を強く意識したものです。以下に、各主要変更点についてさらに深く掘り下げて説明します。

## 変更の背景
### 著者情報と日付の更新
例えば、`assistants-quickstart.md`の著者が「mrbullwinkle」から「aahill」へと変更されましたが、これはドキュメントの信頼性や関連性を保つための重要な更新です。特に、技術文書は常に最新情報を反映する必要があるため、著者の変更はその情報が最新であることを保証するものです。

## 問題解決とユーザー体験の向上
### デプロイメント手順の明確化
`quota.md`などでデプロイメント手順が明確に記述されることにより、ユーザーはAzure AI Studioのデプロイプロセスをスムーズに行うことができ、混乱を防ぐことができます。具体的には、従来の「Management」セクションではなく「Shared Resources」セクションからデプロイメントを作成するなどの変更が行われました。これにより、ユーザーは操作をより直感的に理解しやすくなっています。

### APIエンドポイントの変更
`api-surface.md`のエンドポイント変更により、従来の「completions」エンドポイントから「chat/completions」に移行しました。これは、Azure OpenAIがチャットベースの解析機能に焦点を当てており、ユーザーがAPIを利用する際に一貫性を保つための重要な変更点です。これにより、ユーザーは特定の機能に対するリクエストをより正確に構成できるようになります。

## ビジュアル更新の意義
### 画像の追加と更新
画像の追加や修正も多数行われました。例えば、`chat-view-code.png`の追加は、ユーザーがコードを視覚的に理解するための支援を強化します。同様に、旧画像が最新情報に基づいて更新されることで、視覚資料を利用した操作が確実に行えるようになります。特に、新規ユーザーにとって視覚的なガイドは非常に有益であり、迅速な理解と操作の習得を助けるものです。

まとめとして、今回の変更は単なる表面的な修正ではなく、実際のユーザーエクスペリエンスを向上させることを目

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [assistants-quickstart.md](#item-eaf614) | minor update | アーティクルの著者情報と日付の更新 | modified | 4 | 10 | 14 | 
| [quota.md](#item-9440c2) | minor update | デプロイメント手順の更新とクォータ項目の明確化 | modified | 5 | 7 | 12 | 
| [working-with-models.md](#item-7ec098) | minor update | デプロイメント手順の項目名の変更 | modified | 1 | 7 | 8 | 
| [api-surface.md](#item-a25fa2) | minor update | APIエンドポイントの更新 | modified | 1 | 1 | 2 | 
| [assistants-ai-studio.md](#item-1632e2) | minor update | Azure AI Studioの使用に関する追加情報 | modified | 3 | 0 | 3 | 
| [chatgpt-javascript.md](#item-cbf09f) | minor update | ChatGPTのJavaScriptおよびTypeScriptサンプルの改善 | modified | 167 | 1 | 168 | 
| [chatgpt-studio.md](#item-ab43f3) | minor update | ChatGPT Studioに関するドキュメントの更新 | modified | 15 | 60 | 75 | 
| [connect-your-data-studio.md](#item-c34da8) | minor update | データソース追加の手順を更新 | modified | 4 | 0 | 4 | 
| [dall-e-studio.md](#item-439729) | minor update | DALL-Eのドキュメント名を更新 | modified | 4 | 4 | 8 | 
| [javascript.md](#item-f4828f) | minor update | JavaScriptおよびTypeScriptのサンプルコードを更新 | modified | 169 | 1 | 170 | 
| [studio.md](#item-eeeaff) | minor update | Azure OpenAI Studioに関するドキュメントの更新 | modified | 7 | 22 | 29 | 
| [deploy-models.png](#item-c9e3a5) | minor update | デプロイモデルに関する画像の更新 | modified | 0 | 0 | 0 | 
| [dynamic-quota.png](#item-eaf5dc) | minor update | ダイナミッククォータに関する画像の更新 | modified | 0 | 0 | 0 | 
| [update-policy.png](#item-ad6800) | minor update | モデルの更新ポリシーに関する画像の更新 | modified | 0 | 0 | 0 | 
| [auto-update.png](#item-4e03a7) | minor update | 自動更新に関する画像の更新 | modified | 0 | 0 | 0 | 
| [column-options.png](#item-768cad) | breaking change | カラムオプションに関する画像の削除 | removed | 0 | 0 | 0 | 
| [deployments.png](#item-7217ff) | minor update | デプロイメントに関する画像の更新 | modified | 0 | 0 | 0 | 
| [assistant-session.png](#item-8cb4f9) | breaking change | アシスタントセッションに関する画像の削除 | removed | 0 | 0 | 0 | 
| [assistants-playground.png](#item-211017) | breaking change | アシスタントプレイグラウンドに関する画像の削除 | removed | 0 | 0 | 0 | 
| [assistants-studio.png](#item-8f1ba9) | breaking change | アシスタントスタジオに関する画像の削除 | removed | 0 | 0 | 0 | 
| [chat-playground.png](#item-cb74b5) | minor update | チャットプレイグラウンドに関する画像の更新 | modified | 0 | 0 | 0 | 
| [chat-view-code.png](#item-74bc20) | new feature | チャットビューコードに関する画像の追加 | added | 0 | 0 | 0 | 
| [chatgpt-playground-load.png](#item-77b058) | minor update | ChatGPTプレイグラウンドの読み込みに関する画像の更新 | modified | 0 | 0 | 0 | 
| [chatgpt-playground.png](#item-ad29b9) | minor update | ChatGPTプレイグラウンドの画像の更新 | modified | 0 | 0 | 0 | 
| [dall-e-studio.png](#item-fe085c) | minor update | DALL·Eスタジオに関する画像の更新 | modified | 0 | 0 | 0 | 
| [playground-load.png](#item-e248f0) | minor update | プレイグラウンドのロード画面に関する画像の更新 | modified | 0 | 0 | 0 | 
| [studio-start.png](#item-a3bf0f) | minor update | スタジオの開始画面に関する画像の更新 | modified | 0 | 0 | 0 | 
| [summarize-text.png](#item-675e86) | minor update | テキスト要約機能に関する画像の更新 | modified | 0 | 0 | 0 | 
| [deployment.png](#item-59cbb2) | minor update | デプロイメントに関する画像の更新 | modified | 0 | 0 | 0 | 
| [quota.png](#item-b7e319) | minor update | クオータに関する画像の更新 | modified | 0 | 0 | 0 | 
| [bring-your-data-card.png](#item-2e0a7f) | minor update | データカードに関する画像の更新 | modified | 0 | 0 | 0 | 
| [chat-playground.png](#item-fd6d6f) | new feature | チャットプレイグラウンドに関する画像の追加 | added | 0 | 0 | 0 | 
| [quickstart.md](#item-7d1656) | minor update | クイックスタートガイドにTypeScriptトラッキングの追加 | modified | 1 | 1 | 2 | 
| [use-your-data-quickstart.md](#item-52c1f4) | minor update | データ利用に関するクイックスタートガイドの大幅な改訂 | modified | 102 | 35 | 137 | 
| [whats-new.md](#item-53303b) | minor update | Whats Newページの更新および日付の修正 | modified | 6 | 1 | 7 | 


# Modified Contents
## articles/ai-services/openai/assistants-quickstart.md{#item-eaf614}

<details>
<summary>Diff</summary>
````diff
@@ -6,9 +6,9 @@ manager: nitinme
 ms.service: azure-ai-openai
 ms.custom: devx-track-python, devx-track-dotnet, devx-track-extended-java, devx-track-js
 ms.topic: quickstart
-author: mrbullwinkle
-ms.author: mbullwin
-ms.date: 07/18/2024
+author: aahill
+ms.author: aahi
+ms.date: 09/18/2024
 zone_pivot_groups: openai-quickstart-assistants
 recommendations: false
 ---
@@ -18,15 +18,9 @@ recommendations: false
 
 Azure OpenAI Assistants (Preview) allows you to create AI assistants tailored to your needs through custom instructions and augmented by advanced tools like code interpreter, and custom functions.
 
-::: zone pivot="programming-language-studio"
-
-[!INCLUDE [Azure OpenAI Studio quickstart](includes/assistants-studio.md)]
-
-::: zone-end
-
 ::: zone pivot="programming-language-ai-studio"
 
-[!INCLUDE [AI Studio (Preview)](includes/assistants-ai-studio.md)]
+[!INCLUDE [AI Studio](includes/assistants-ai-studio.md)]
 
 ::: zone-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "アーティクルの著者情報と日付の更新"
}
```

### Explanation
このコードの変更は、`assistants-quickstart.md`というドキュメントの著者情報とリリース日付の更新を含んでいます。また、マークダウンファイル内の一部のセクションが削除されており、その結果、全体的な構成も改良されています。具体的には、著者が「mrbullwinkle」から「aahill」に変更され、メタ情報の一部もそれに応じて更新されています。これにより、ドキュメントが最新の情報を反映するようになります。一部のリファレンスは削除されていますが、全体的には内容が整理され、読みやすくなっています。また、AIスタジオに関連する情報が簡素化され、より直感的に理解しやすくされています。

## articles/ai-services/openai/how-to/quota.md{#item-9440c2}

<details>
<summary>Diff</summary>
````diff
@@ -44,13 +44,11 @@ The flexibility to distribute TPM globally within a subscription and region has
 
 When you create a model deployment, you have the option to assign Tokens-Per-Minute (TPM) to that deployment. TPM can be modified in increments of 1,000, and will map to the TPM and RPM rate limits enforced on your deployment, as discussed above.
 
-To create a new deployment from within the Azure AI Studio under **Management** select **Deployments** > **Create new deployment**.
-
-The option to set the TPM is under the **Advanced options** drop-down:
+To create a new deployment from within the Azure AI Studio under **Shared Resources** select **Deployments** > **Deploy model** > **Deploy base model** > **Select Model** > **Confirm**.
 
 :::image type="content" source="../media/quota/deployment.png" alt-text="Screenshot of the deployment UI of Azure AI Studio" lightbox="../media/quota/deployment.png":::
 
-Post deployment you can adjust your TPM allocation by selecting **Edit deployment** under **Management** > **Deployments** in Azure AI Studio. You can also modify this selection within the new quota management experience under **Management** > **Quotas**.
+Post deployment you can adjust your TPM allocation by selecting **Edit** under **Shared resources** > **Deployments** in Azure OpenAI Studio. You can also modify this selection within the new quota management experience under **Management** > **Quotas**.
 
 > [!IMPORTANT]
 > Quotas and limits are subject to change, for the most up-date-information consult our [quotas and limits article](../quotas-limits.md).
@@ -70,10 +68,10 @@ For an all up view of your quota allocations across deployments in a given regio
 
 :::image type="content" source="../media/quota/quota.png" alt-text="Screenshot of the quota UI of Azure AI Studio" lightbox="../media/quota/quota.png":::
 
-- **Quota Name**: There's one quota value per region for each model type. The quota covers all versions of that model.  The quota name can be expanded in the UI to show the deployments that are using the quota.
 - **Deployment**: Model deployments divided by model class.
-- **Usage/Limit**: For the quota name, this shows how much quota is used by deployments and the total quota approved for this subscription and region. This amount of quota used is also represented in the bar graph.
-- **Request Quota**: The icon in this field navigates to a form where requests to increase quota can be submitted.
+- **Quota type**: There's one quota value per region for each model type. The quota covers all versions of that model.  
+- **Quota allocation**: For the quota name, this shows how much quota is used by deployments and the total quota approved for this subscription and region. This amount of quota used is also represented in the bar graph.
+- **Request Quota**: The icon navigates to a form where requests to increase quota can be submitted.
 
 ## Migrating existing deployments
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメント手順の更新とクォータ項目の明確化"
}
```

### Explanation
このコードの変更は、`quota.md`というドキュメント内でのデプロイメント手順の更新とクォータの項目に関する明確化を含みます。具体的には、Azure AI Studioにおける新しいデプロイメントの作成方法が更新され、手順が簡潔に説明されています。また、特定の用語が明確にされ、クォータの各項目についての説明が改善されています。

具体的には、デプロイメントの作成に関して、以前は「Management」セクションから「Create new deployment」を選択していたのが、「Shared Resources」セクションからより直接的な手順に変更されています。また、クォータに関する情報も、用語を整理し、より理解しやすい形に更新しています。これにより、ユーザーはデプロイメントを管理する際のプロセスとクォータの理解がしやすくなります。全体として、ユーザーエクスペリエンスを向上させるための小規模な調整が行われています。

## articles/ai-services/openai/how-to/working-with-models.md{#item-7ec098}

<details>
<summary>Diff</summary>
````diff
@@ -20,7 +20,7 @@ You can get a list of models that are available for both inference and fine-tuni
 
 ## Model updates
 
-Azure OpenAI now supports automatic updates for select model deployments. On models where automatic update support is available, a model version drop-down is visible in Azure OpenAI Studio under **Create new deployment** and **Edit deployment**:
+Azure OpenAI now supports automatic updates for select model deployments. On models where automatic update support is available, a model version drop-down is visible in Azure OpenAI Studio under **Deployments** and **Edit**:
 
 :::image type="content" source="../media/models/auto-update.png" alt-text="Screenshot of the deploy model UI of Azure OpenAI Studio." lightbox="../media/models/auto-update.png":::
 
@@ -44,16 +44,10 @@ For currently deployed models, from Azure OpenAI Studio select **Deployments**:
 
 :::image type="content" source="../media/models/deployments.png" alt-text="Screenshot of the deployment UI of Azure OpenAI Studio." lightbox="../media/models/deployments.png":::
 
-To view retirement dates for all available models in a given region from Azure OpenAI Studio, select **Models** > **Column options** > Select **Deprecation fine tune** and **Deprecation inference**:
-
-:::image type="content" source="../media/models/column-options.png" alt-text="Screenshot of the models UI of Azure OpenAI Studio." lightbox="../media/models/column-options.png":::
-
 ## Model deployment upgrade configuration
 
 You can check what model upgrade options are set for previously deployed models in [Azure OpenAI Studio](https://oai.azure.com). Select **Deployments** > Under the deployment name column select one of the deployment names that are highlighted in blue.
 
-:::image type="content" source="../media/how-to/working-with-models/deployments.png" alt-text="Screenshot of the deployments pane with a deployment name highlighted." lightbox="../media/how-to/working-with-models/deployments.png":::
-
 Selecting a deployment name opens the **Properties** for the model deployment. You can view what upgrade options are set for your deployment under **Version update policy**:
 
 :::image type="content" source="../media/how-to/working-with-models/update-policy.png" alt-text="Screenshot of the model deployments property UI." lightbox="../media/how-to/working-with-models/update-policy.png":::
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメント手順の項目名の変更"
}
```

### Explanation
このコードの変更は、`working-with-models.md`というドキュメントにおいて、Azure OpenAIのデプロイメントに関する手順の表現を更新したものです。具体的には、モデルの自動更新機能に関連する情報がより一貫した用語に変更され、ユーザーが操作を行う際の理解を深めています。

具体的には、「Create new deployment」および「Edit deployment」という用語が、「Deployments」および「Edit」に変更されています。これにより、デプロイメント作成時のインターフェースが簡素化され、ユーザーが必要な操作を容易に見つけられるようになります。また、いくつかのセクションが削除されていますが、重要な情報は保持されており、全体的に文書の明確さが向上しています。この更新により、ユーザーはAzure OpenAI Studio内でのデプロイメント管理がよりスムーズに行えるようになります。

## articles/ai-services/openai/includes/api-surface.md{#item-a25fa2}

<details>
<summary>Diff</summary>
````diff
@@ -38,5 +38,5 @@ Azure OpenAI provides two methods for authentication. You can use  either API Ke
 The service APIs are versioned using the ```api-version``` query parameter. All versions follow the YYYY-MM-DD date structure. For example:
 
 ```http
-POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/completions?api-version=2024-06-01
+POST https://YOUR_RESOURCE_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2024-06-01
 ```
\ No newline at end of file
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "APIエンドポイントの更新"
}
```

### Explanation
このコードの変更は、`api-surface.md`というドキュメント内でのAPIエンドポイントの更新を反映しています。具体的には、Azure OpenAIのエンドポイントが変わり、リクエストが特定のモデルに対応した方法で構成されるようになっています。

変更前は、リクエストパスが「completions」で終わっていたのに対し、変更後は「chat/completions」が使用されています。これにより、チャットに関連した解析機能を示すエンドポイントが明確になり、ユーザーが特定の機能にアクセスしやすくなります。この更新は、APIの使用や実装において重要な部分であり、ユーザーは最新の構造に従ったリクエストを行う必要があります。全体として、APIの整合性と明確さを向上させるための小規模な調整が行われています。

## articles/ai-services/openai/includes/assistants-ai-studio.md{#item-1632e2}

<details>
<summary>Diff</summary>
````diff
@@ -22,6 +22,9 @@ author: mrbullwinkle
 
 ## Go to the Azure AI Studio (Preview)
 
+> [!NOTE]
+> While you can use [Azure OpenAI Studio](https://oai.azure.com/), we recommend using the steps here to use [Azure AI Studio](https://ai.azure.com). AI Studio lets you use Assistants v2 which provides several upgrades such as the [file search](../how-to/file-search.md) tool which is faster and supports more files.
+
 1. Sign in to [Azure AI Studio](https://ai.azure.com).
 1. Go to your project or [create a new project](../../../ai-studio//how-to/create-projects.md) in Azure AI Studio.
 1. From your project overview, select **Assistants**, located under **Project playground**.
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure AI Studioの使用に関する追加情報"
}
```

### Explanation
このコードの変更は、`assistants-ai-studio.md`というドキュメントにおいて、Azure AI Studioの使用を促進するための推奨事項を追加したものです。具体的には、ユーザーがAzure OpenAI StudioとAzure AI Studioのどちらを使用すべきかについての注意書きが新たに加えられています。

追加された内容では、「Azure OpenAI Studio」ではなく「Azure AI Studio」を使うことを推奨しており、その理由として新たに提供される「Assistants v2」や「ファイル検索ツール」といったアップグレード機能を紹介しています。これにより、ユーザーは最新の機能を活用できるため、作業の効率が向上します。全体として、この更新はユーザーが最適な環境を選択するための参考情報を提供することを目的としています。

## articles/ai-services/openai/includes/chatgpt-javascript.md{#item-cbf09f}

<details>
<summary>Diff</summary>
````diff
@@ -11,20 +11,34 @@ ms.author: mbullwin
 ms.date: 05/21/2024
 ---
 
-[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai)
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
 > This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
+## [**TypeScript**](#tab/typescript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
+- An Azure OpenAI Service resource with a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
+
+## [**JavaScript**](#tab/javascript)
+
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
 - An Azure OpenAI Service resource with either a `gpt-35-turbo` or `gpt-4` series models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 > [!div class="nextstepaction"]
 > [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
 
+---
+
 ## Set up
 
 [!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
@@ -52,6 +66,81 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Open a command prompt where you want the new project, and create a new file named ChatCompletion.js. Copy the following code into the ChatCompletion.js file.
 
+## [**TypeScript**](#tab/typescript)
+
+```typescript
+import "dotenv/config";
+import { AzureOpenAI } from "openai";
+import type {
+  ChatCompletion,
+  ChatCompletionCreateParamsNonStreaming,
+} from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+
+function createMessages(): ChatCompletionCreateParamsNonStreaming {
+  return {
+    messages: [
+      { role: "system", content: "You are a helpful assistant." },
+      {
+        role: "user",
+        content: "Does Azure OpenAI support customer managed keys?",
+      },
+      {
+        role: "assistant",
+        content: "Yes, customer managed keys are supported by Azure OpenAI?",
+      },
+      { role: "user", content: "Do other Azure AI services support this too?" },
+    ],
+    model: "",
+  };
+}
+async function printChoices(completion: ChatCompletion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.message);
+  }
+}
+export async function main() {
+  const client = getClient();
+  const messages = createMessages();
+  const result = await client.chat.completions.create(messages);
+  await printChoices(result);
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe Completion.js
+```
+
+## [**JavaScript**](#tab/javascript)
+
 ```javascript
 const { AzureOpenAI } = require("openai");
 
@@ -97,6 +186,8 @@ Run the script with the following command:
 node.exe ChatCompletion.js
 ```
 
+---
+
 ## Output
 
 ```output
@@ -112,6 +203,78 @@ node.exe ChatCompletion.js
 > [!IMPORTANT]
 > In the previous example we are demonstrating key-based authentication. Once you have tested with key-based authentication successfully, we recommend using the more secure [Microsoft Entra ID](/entra/fundamentals/whatis) for authentication which is demonstrated in the next code sample. Getting started with [Microsoft Entra ID] will require some additional [prerequisites](https://www.npmjs.com/package/@azure/identity).
 
+## [**TypeScript**](#tab/typescript)
+
+```typescript
+import {
+  DefaultAzureCredential,
+  getBearerTokenProvider,
+} from "@azure/identity";
+import "dotenv/config";
+import { AzureOpenAI } from "openai";
+import type {
+  ChatCompletion,
+  ChatCompletionCreateParamsNonStreaming,
+} from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-4o-mini"; //This must match your deployment name.
+
+function getClient(): AzureOpenAI {
+  const scope = "https://cognitiveservices.azure.com/.default";
+  const azureADTokenProvider = getBearerTokenProvider(
+    new DefaultAzureCredential(),
+    scope
+  );
+  return new AzureOpenAI({
+    endpoint,
+    azureADTokenProvider,
+    deployment: deploymentName,
+    apiVersion,
+  });
+}
+
+function createMessages(): ChatCompletionCreateParamsNonStreaming {
+  return {
+    messages: [
+      { role: "system", content: "You are a helpful assistant." },
+      {
+        role: "user",
+        content: "Does Azure OpenAI support customer managed keys?",
+      },
+      {
+        role: "assistant",
+        content: "Yes, customer managed keys are supported by Azure OpenAI?",
+      },
+      { role: "user", content: "Do other Azure AI services support this too?" },
+    ],
+    model: "",
+  };
+}
+async function printChoices(completion: ChatCompletion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.message);
+  }
+}
+export async function main() {
+  const client = getClient();
+  const messages = createMessages();
+  const result = await client.chat.completions.create(messages);
+  await printChoices(result);
+}
+
+main().catch((err) => {
+  console.error("The sample encountered an error:", err);
+});
+```
+
+
+## [**JavaScript**](#tab/javascript)
+
 ```javascript
 const { AzureOpenAI } = require("openai");
 const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
@@ -150,6 +313,9 @@ main().catch((err) => {
 
 module.exports = { main };
 ```
+
+---
+
 > [!NOTE]
 > If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPTのJavaScriptおよびTypeScriptサンプルの改善"
}
```

### Explanation
このコードの変更は、`chatgpt-javascript.md`というドキュメントにおいて、ChatGPTのJavaScriptとTypeScriptのサンプルコードを更新し、Azure OpenAIの利用方法を明確にするための情報を追加したものです。主な変更点には、サンプルコードの新しいバージョンの導入、TypeScriptの追加、Microsoft Entra IDによる認証方法に関する情報が含まれています。

新たに追加された要素には、Azure AI APIの利用に必要な前提条件や、環境変数の設定方法が示されています。また、Azure AD認証を介した接続の方法も説明されています。さらに、ユーザーが新しいサンプルコードを実行するにあたり、具体的な手順やコマンドも詳細に記述されています。これにより、開発者はAzure OpenAIを簡単にセットアップし利用できるようになります。この更新は、ユーザーがより最近の技術を活用しやすくすることを目的としています。

## articles/ai-services/openai/includes/chatgpt-studio.md{#item-ab43f3}

<details>
<summary>Diff</summary>
````diff
@@ -6,19 +6,13 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 03/01/2023
+ms.date: 09/19/2024
 ---
 
 ## Prerequisites
 
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true).
-- An Azure OpenAI Service resource with either the `gpt-35-turbo` or the `gpt-4` models deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
-
-> [!div class="nextstepaction"]
-> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=STUDIO&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Prerequisites)
-
-> [!TIP]
-> Try out the new unified [Azure AI Studio (preview)](../../../ai-studio/what-is-ai-studio.md) which brings together capabilities from across multiple Azure AI services.
+- An Azure OpenAI Service resource with either `gpt-4o` or the `gpt-4o-mini` models deployed. We recommend using standard or global standard model [deployment tpyes](../how-to/deployment-types.md) for initial exploration. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 ## Go to Azure OpenAI Studio
 
@@ -34,82 +28,43 @@ Start exploring OpenAI capabilities with a no-code approach through the Azure Op
 
 :::image type="content" source="../media/quickstarts/chatgpt-playground-load.png" alt-text="Screenshot of the Chat playground page." lightbox="../media/quickstarts/chatgpt-playground-load.png":::
 
-### Assistant setup
+### Setup
 
-You can use the **Assistant setup** dropdown to select a few pre-loaded **System message** examples to get started.
+You can use the **Prompt samples* dropdown to select a few pre-loaded **System message** examples to get started.
 
 **System messages** give the model instructions about how it should behave and any context it should reference when generating a response. You can describe the assistant's personality, tell it what it should and shouldn't answer, and tell it how to format responses.
 
-**Add few-shot examples** allows you to provide conversational examples that are used by the model for [in-context learning](../concepts/prompt-engineering.md#basics).
-
 At any time while using the Chat playground you can select **View code** to see Python, curl, and json code samples pre-populated based on your current chat session and settings selections. You can then take this code and write an application to complete the same task you're currently performing with the playground.
 
 ### Chat session
 
-Selecting the **Send** button sends the entered text to the completions API and the results are returned back to the text box.
+Selecting the **Enter** button or selecting the right arrow icon sends the entered text to the chat completions API and the results are returned back to the text box.
 
 Select the **Clear chat** button to delete the current conversation history.
 
-### Settings
+### Key settings
 
 | **Name**            | **Description**   |
 |:--------------------|:-------------------------------------------------------------------------------|
 | Deployments         | Your deployment name that is associated with a specific model. |
+| Add your data | 
+| Parameters | Custom parameters that alter the model responses. When you are starting out we recommend to use the defaults for most parameters |
 | Temperature         | Controls randomness. Lowering the temperature means that the model produces more repetitive and deterministic responses. Increasing the temperature results in more unexpected or creative responses. Try adjusting temperature or Top P but not both. |
-| Max length (tokens) | Set a limit on the number of tokens per model response. The API supports a maximum of 4096 tokens shared between the prompt (including system message, examples, message history, and user query) and the model's response. One token is roughly four characters for typical English text.|
-| Top probabilities   | Similar to temperature, this controls randomness but uses a different method. Lowering Top P narrows the model’s token selection to likelier tokens. Increasing Top P lets the model choose from tokens with both high and low likelihood. Try adjusting temperature or Top P but not both.|
-| Multi-turn conversations | Select the number of past messages to include in each new API request. This helps give the model context for new user queries. Setting this number to 10 results in five user queries and five system responses.|
+| Max response (tokens) | Set a limit on the number of tokens per model response. The API on the latest models supports a maximum of 128,000 tokens shared between the prompt (including system message, examples, message history, and user query) and the model's response. One token is roughly four characters for typical English text.|
+| Top p   | Similar to temperature, this controls randomness but uses a different method. Lowering Top P narrows the model’s token selection to likelier tokens. Increasing Top P lets the model choose from tokens with both high and low likelihood. Try adjusting temperature or Top P but not both.|
 | Stop sequences      | Stop sequence make the model end its response at a desired point. The model response ends before the specified sequence, so it won't contain the stop sequence text. For GPT-35-Turbo, using `<|im_end|>` ensures that the model response doesn't generate a follow-up user query. You can include as many as four stop sequences.|
 
-### Show panels
-
-By default there are three panels: assistant setup, chat session, and settings. **Show panels** allows you to add, remove, and rearrange the panels. If you ever close a panel and need to get it back, use **Show panels** to restore the lost panel.
-
-## Start a chat session
-
-1. From the assistant setup drop-down, select **Xbox customer support agent**
-2. You'll be prompted asking if you want to update the system message, select **Continue**.
-3. In the chat session pane, enter the following question: "I'm interested in buying a new Xbox", and select **Send**.
-4. You'll receive a response similar to:
+## View code
 
-    :::image type="content" source="../media/quickstarts/xbox.png" alt-text="Screenshot of a first question and answer in playground." lightbox="../media/quickstarts/xbox.png":::
+Once you have experimented with chatting with the model select the **</> View Code** button. This will give you a replay of the code behind your entire conversation so far:
 
-5. Enter a follow-up question like: "which models support 4K?"
-
-    :::image type="content" source="../media/quickstarts/models.png" alt-text="Screenshot of follow-up question and answer in playground." lightbox="../media/quickstarts/models.png":::
-
-6. Now that you have a basic conversation select **View code** from under **Assistant setup** and you'll have a replay of the code behind the entire conversation so far:
-
-```python
-#Note: The openai-python library support for Azure OpenAI is in preview.
-import os
-import openai
-openai.api_type = "azure"
-openai.api_base = "https://docs-test-001.openai.azure.com/"
-openai.api_version = "2024-02-01"
-openai.api_key = os.getenv("OPENAI_API_KEY")
-
-response = openai.ChatCompletion.create(
-  engine="gpt-35-turbo", # replace this value with the deployment name you chose when you deployed the associated model.
-  messages = [{"role":"system","content":"You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."},{"role":"user","content":"How much is a PS5?"},{"role":"assistant","content":"I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"},{"role":"user","content":"I am interested in buying an Xbox?"},{"role":"assistant","content":"Great! There are several Xbox models available in the market, including the Xbox Series X, Xbox Series S, and Xbox One. The Xbox Series X is the latest and most powerful console, while the Xbox Series S is a more affordable option that still offers great performance. The Xbox One is the previous generation console, but it still has a large library of games available to play.\n\nBefore purchasing an Xbox, you may want to consider factors such as your budget, the types of games you want to play, and whether you want to play games in 4K resolution. Once you have decided on a console, you can purchase it from a retailer or directly from the Xbox website. Let me know if you have any other questions or concerns!"},{"role":"user","content":"Which models are 4K?"},{"role":"assistant","content":"Both the Xbox Series X and Xbox One X support 4K resolution gaming. The Xbox Series S, on the other hand, supports up to 1440p resolution gaming, but it can upscale games to 4K. It's worth noting that in order to take advantage of 4K gaming, you'll need a 4K TV or monitor that supports HDR (High Dynamic Range) and HDMI 2.0 or higher."}],
-  temperature=0,
-  max_tokens=350,
-  top_p=0.95,
-  frequency_penalty=0,
-  presence_penalty=0,
-  stop=None)
-```
-
-> [!div class="nextstepaction"]
-> [I ran into an issue with the playground.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=STUDIO&Pillar=AOAI&Product=Chatgpt&Page=quickstart&Section=Set-up)
+:::image type="content" source="../media/quickstarts/chat-view-code.png" alt-text="Screenshot of view code experience." lightbox="../media/quickstarts/chat-view-code.png":::
 
 ### Understanding the prompt structure
 
-If you examine the sample from **View code** you'll notice some unique tokens that weren't part of a typical GPT completion call. GPT-35-Turbo was trained to use special tokens to delineate different parts of the prompt. Content is provided to the model in between `<|im_start|>` and `<|im_end|>` tokens. The prompt begins with a system message that can be used to prime the model by including context or instructions for the model. After that, the prompt contains a series of messages between the user and the assistant.
-
-The assistant's response to the prompt will then be returned below the `<|im_start|>assistant` token and will end with `<|im_end|>` denoting that the assistant has finished its response. You can also use the **Show raw syntax** toggle button to display these tokens within the chat session panel.
+If you examine the sample from **View code** you'll notice that the conversation is broken into three distinct roles `system`, `user`, `assistant`. Each time you message the model the entire conversation history up to that point is resent. When using the chat completions API the model has no true memory of what you have sent to it in the past so you provide the conversation history for context to allow the model to respond properly.
 
-The [GPT-35-Turbo & GPT-4 how-to guide](../how-to/chatgpt.md) provides an in-depth introduction into the new prompt structure and how to use the `gpt-35-turbo` model effectively.
+The [Chat completions how-to guide](../how-to/chatgpt.md) provides an in-depth introduction into the new prompt structure and how to use chat completions models effectively.
 
 [!INCLUDE [deploy-web-app](deploy-web-app.md)]
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPT Studioに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`chatgpt-studio.md`というドキュメントに対する修正で、主にAzure OpenAIの使用とChatGPT Studioの使い方に関連する情報が更新されています。変更としては、特に「前提条件」や「セットアップ」セクションにおける情報の整理が行われており、リソースやモデルの名称も最新のものに合わせて調整されています。

具体的には、使用するモデルが`gpt-4`から`gpt-4o`および`gpt-4o-mini`に変更され、モデルの展開に関する推奨事項も明記されています。また、ユーザーインターフェースの操作に関する指示が改訂され、送信ボタンの操作やコード表示機能についても具体的に説明されています。

この変更によって、ユーザーはChatGPT Studioをより効果的に使用できるようになり、特に新たに追加された設定やパラメータの理解が深まることが期待されます。また、文書全体としての一貫性が向上し、最新情報への対応がなされています。

## articles/ai-services/openai/includes/connect-your-data-studio.md{#item-c34da8}

<details>
<summary>Diff</summary>
````diff
@@ -21,6 +21,10 @@ Navigate to [Azure OpenAI Studio](https://oai.azure.com/) and sign-in with crede
 
     :::image type="content" source="../media/use-your-data/bring-your-data-card.png" alt-text="A screenshot of the Azure OpenAI Studio landing page." lightbox="../media/use-your-data/bring-your-data-card.png":::
 
+1. In the **Chat playground**, Select **Add your data** and then **Add a data source**
+
+    :::image type="content" source="../media/use-your-data/chat-playground.png" alt-text="A screenshot of the chat playground in  OpenAI Studio." lightbox="../media/use-your-data/chat-playground.png":::
+
 1. In the pane that appears, select **Upload files (preview)** under **Select data source**. Azure OpenAI needs both a storage resource and a search resource to access and index your data. 
 
     > [!TIP]
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データソース追加の手順を更新"
}
```

### Explanation
このコードの変更は、`connect-your-data-studio.md`というドキュメントにおける手順に関するマイナーな更新です。主に、Azure OpenAI Studioでのデータ追加に関する手順が強化されています。

具体的には、**Chat playground**セクションに「データを追加」する手順が新たに追加され、まず**Add your data**を選択し、続いて**Add a data source**を選ぶことが求められています。この変更により、ユーザーはデータソースの追加プロセスをより明確に理解できるようになります。

また、付随して追加された画像は、ユーザーにとって視覚的な支援を提供し、手順を実行する際の理解を助けることを目的としています。この更新により、ユーザーはデータのインポート手順をよりスムーズに実行できるようになるでしょう。

## articles/ai-services/openai/includes/dall-e-studio.md{#item-439729}

<details>
<summary>Diff</summary>
````diff
@@ -35,24 +35,24 @@ Browse to [Azure OpenAI Studio](https://oai.azure.com/) and sign in with the cre
 
 #### [DALL-E 3](#tab/dalle3)
 
-From the Azure OpenAI Studio landing page, select **DALL·E playground (Preview)** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has your DALL-E 3 deployment selected.
+From the Azure OpenAI Studio landing page, select **Images playground** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has your DALL-E 3 deployment selected.
 
 #### [DALL-E 2 (preview)](#tab/dalle2)
 
-From the Azure OpenAI Studio landing page, select **DALL·E playground (Preview)** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has the default **DALL-E 2** choice selected.
+From the Azure OpenAI Studio landing page, select **Images playground** to use the image generation APIs. Select **Settings** near the top of the page and confirm that the **Deployment** dropdown has the default **DALL-E 2** choice selected.
 
 ---
 
 ## Try out image generation
 
-Start exploring Azure OpenAI capabilities with a no-code approach through the **DALL·E playground (Preview)**. Enter your image prompt into the text box and select **Generate**. When the AI-generated image is ready, it appears on the page.
+Start exploring Azure OpenAI capabilities with a no-code approach through the **Images playground**. Enter your image prompt into the text box and select **Generate**. When the AI-generated image is ready, it appears on the page.
 
 > [!NOTE]
 > The image generation APIs come with a content moderation filter. If Azure OpenAI recognizes your prompt as harmful content, it doesn't return a generated image. For more information, see [Content filtering](../concepts/content-filter.md).
 
 :::image type="content" source="../media/quickstarts/dall-e-studio.png" alt-text="Screenshot of the Azure OpenAI Studio landing page showing the DALL-E playground (Preview) with generated images of polar bears." lightbox="../media/quickstarts/dall-e-studio.png":::
 
-In the **DALL·E playground (Preview)**, you can also view Python and cURL code samples, which are prefilled according to your settings. Select **View code** near the top of the page. You can use this code to write an application that completes the same task.
+In the **Images playground**, you can also view Python and cURL code samples, which are prefilled according to your settings. Select **View code** near the top of the page. You can use this code to write an application that completes the same task.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL-Eのドキュメント名を更新"
}
```

### Explanation
このコードの変更は、`dall-e-studio.md`に対するもので、DALL-Eに関するページの表記が更新されています。主な変更点は、DALL-E Playgroundの名称が「**DALL·E playground (Preview)**」から「**Images playground**」に変更されたことです。この名称の変更は、一貫性を保つために行われたと考えられます。

具体的には、DALL-E 3およびDALL-E 2のセクションで、画像生成APIを使用する際の手順が修正されており、両方のセクションにおいて「Images playground」という新しい名称が適用されています。また、ユーザーが生成した画像を確認する際の操作に関する説明も更新されています。

この変更により、文書全体の用語が統一され、ユーザーがAzure OpenAI Studio内での操作を理解しやすくなります。画像生成機能を使う際の体験が円滑になることが期待されます。

## articles/ai-services/openai/includes/javascript.md{#item-f4828f}

<details>
<summary>Diff</summary>
````diff
@@ -11,20 +11,34 @@ ms.author: mbullwin
 ms.date: 05/20/2024
 ---
 
-[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai)
+[Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 > [!NOTE]
 > This article has been updated to use the [latest OpenAI npm package](https://www.npmjs.com/package/openai) which now fully supports Azure OpenAI. If you are looking for code examples for the legacy Azure OpenAI JavaScript SDK they are currently still [available in this repo](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples/v2-beta/javascript).
 
 ## Prerequisites
 
+## [**TypeScript**](#tab/typescript)
+
 - An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
 - [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- [TypeScript](https://www.typescriptlang.org/download/)
 - An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
 > [!div class="nextstepaction"]
 > [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Prerequisites)
 
+## [**JavaScript**](#tab/javascript)
+
+- An Azure subscription - [Create one for free](https://azure.microsoft.com/free/cognitive-services?azure-portal=true)
+- [LTS versions of Node.js](https://github.com/nodejs/release#release-schedule)
+- An Azure OpenAI Service resource with the `gpt-35-turbo-instruct` model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=JAVASCRIPT&Pillar=AOAI&&Product=gpt&Page=quickstart&Section=Prerequisites)
+
+---
+
 ## Set up
 
 [!INCLUDE [get-key-endpoint](get-key-endpoint.md)]
@@ -50,6 +64,76 @@ Your app's _package.json_ file will be updated with the dependencies.
 
 Open a command prompt where you created the new project, and create a new file named Completion.js. Copy the following code into the Completion.js file.
 
+## [**TypeScript**](#tab/typescript)
+
+```typescript
+import "dotenv/config";
+import { AzureOpenAI } from "openai";
+import { type Completion } from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+const apiKey = process.env["AZURE_OPENAI_API_KEY"] || "<api key>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-35-turbo-instruct";
+
+// Chat prompt and max tokens
+const prompt = ["When was Microsoft founded?"];
+const maxTokens = 128;
+
+function getClient(): AzureOpenAI {
+  return new AzureOpenAI({
+    endpoint,
+    apiKey,
+    apiVersion,
+    deployment: deploymentName,
+  });
+}
+async function getCompletion(
+  client: AzureOpenAI,
+  prompt: string[],
+  max_tokens: number
+): Promise<Completion> {
+  return client.completions.create({
+    prompt,
+    model: "",
+    max_tokens,
+  });
+}
+async function printChoices(completion: Completion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.text);
+  }
+}
+export async function main() {
+  console.log("== Get completions Sample ==");
+
+  const client = getClient();
+  const completion = await getCompletion(client, prompt, maxTokens);
+  await printChoices(completion);
+}
+
+main().catch((err) => {
+  console.error("Error occurred:", err);
+});
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe Completion.js
+```
+
+## [**JavaScript**](#tab/javascript)
+
 ```javascript
 const { AzureOpenAI } = require("openai");
 
@@ -90,6 +174,8 @@ Run the script with the following command:
 node.exe Completion.js
 ```
 
+---
+
 ## Output
 
 ```output
@@ -103,6 +189,86 @@ Microsoft was founded on April 4, 1975.
 > [!IMPORTANT]
 > In the previous example we are demonstrating key-based authentication. Once you have tested with key-based authentication successfully, we recommend using the more secure [Microsoft Entra ID](/entra/fundamentals/whatis) for authentication which is demonstrated in the next code sample. Getting started with [Microsoft Entra ID] will require some additional [prerequisites](https://www.npmjs.com/package/@azure/identity).
 
+## [**TypeScript**](#tab/typescript)
+
+```typescript
+import {
+  DefaultAzureCredential,
+  getBearerTokenProvider,
+} from "@azure/identity";
+import "dotenv/config";
+import { AzureOpenAI } from "openai";
+import { type Completion } from "openai/resources/index";
+
+// You will need to set these environment variables or edit the following values
+const endpoint = process.env["AZURE_OPENAI_ENDPOINT"] || "<endpoint>";
+
+// Required Azure OpenAI deployment name and API version
+const apiVersion = "2024-08-01-preview";
+const deploymentName = "gpt-35-turbo-instruct";
+
+// Chat prompt and max tokens
+const prompt = ["When was Microsoft founded?"];
+const maxTokens = 128;
+
+function getClient(): AzureOpenAI {
+  const scope = "https://cognitiveservices.azure.com/.default";
+  const azureADTokenProvider = getBearerTokenProvider(
+    new DefaultAzureCredential(),
+    scope
+  );
+  return new AzureOpenAI({
+    endpoint,
+    azureADTokenProvider,
+    deployment: deploymentName,
+    apiVersion,
+  });
+}
+async function getCompletion(
+  client: AzureOpenAI,
+  prompt: string[],
+  max_tokens: number
+): Promise<Completion> {
+  return client.completions.create({
+    prompt,
+    model: "",
+    max_tokens,
+  });
+}
+async function printChoices(completion: Completion): Promise<void> {
+  for (const choice of completion.choices) {
+    console.log(choice.text);
+  }
+}
+export async function main() {
+  console.log("== Get completions Sample ==");
+
+  const client = getClient();
+  const completion = await getCompletion(client, prompt, maxTokens);
+  await printChoices(completion);
+}
+
+main().catch((err) => {
+  console.error("Error occurred:", err);
+});
+
+```
+
+Build the script with the following command:
+
+```cmd
+tsc
+```
+
+Run the script with the following command:
+
+```cmd
+node.exe Completion.js
+```
+
+
+## [**JavaScript**](#tab/javascript)
+
 ```javascript
 const { AzureOpenAI } = require("openai");
 const { DefaultAzureCredential, getBearerTokenProvider } = require("@azure/identity");
@@ -136,6 +302,8 @@ main().catch((err) => {
 module.exports = { main };
 ```
 
+---
+
 > [!NOTE]
 > If your receive the error: *Error occurred: OpenAIError: The `apiKey` and `azureADTokenProvider` arguments are mutually exclusive; only one can be passed at a time.* You may need to remove a pre-existing environment variable for the API key from your system. Even though the Microsoft Entra ID code sample is not explicitly referencing the API key environment variable, if one is present on the system executing this sample, this error will still be generated.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "JavaScriptおよびTypeScriptのサンプルコードを更新"
}
```

### Explanation
このコードの変更は、`javascript.md`に関連するもので、JavaScriptおよびTypeScriptのサンプルコードが大幅に更新されています。主な変更点として、Azure OpenAIサービスを使用するための新しいサンプルコードが追加され、最新のOpenAI npmパッケージに対応した内容となっています。

具体的には、TypeScriptセクションにおいて、環境変数の設定やAzure OpenAIのデプロイメント名、APIバージョンの設定方法が示されています。また、Azure OpenAIを呼び出すための `getClient` 関数や、生成された結果を出力する `printChoices` 関数の実装が含まれています。この新しい実装は、よりモダンな認証方式であるMicrosoft Entra IDに基づいたコードを利用した例も盛り込まれています。

この更新により、ユーザーは最新の技術とベストプラクティスに従ったコードを参照しやすくなり、スムーズにAzure OpenAIサービスを利用することができるようになります。また、環境変数の設定やエラーメッセージの取り扱いに関する注意が追加され、実用性が向上しています。全体として、非常に有益な情報が追加され、開発者の利便性が高まっています。

## articles/ai-services/openai/includes/studio.md{#item-eeeaff}

<details>
<summary>Diff</summary>
````diff
@@ -5,20 +5,14 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 manager: nitinme
 ms.service: azure-ai-openai
 ms.topic: include
-ms.date: 11/15/2023
+ms.date: 09/19/2023
 ---
 
 ## Prerequisites
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
 - An Azure OpenAI resource with a model deployed. For more information about model deployment, see the [resource deployment guide](../how-to/create-resource.md).
 
-> [!div class="nextstepaction"]
-> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=STUDIO&Pillar=AOAI&Product=gpt&Page=quickstart&Section=Prerequisites)
-
-> [!TIP]
-> Try out the new unified [Azure AI Studio (preview)](../../../ai-studio/what-is-ai-studio.md) which brings together capabilities from across multiple Azure AI services.
-
 ## Go to the Azure OpenAI Studio
 
 Navigate to Azure OpenAI Studio at <a href="https://oai.azure.com/" target="_blank">https://oai.azure.com/</a> and sign-in with credentials that have access to your Azure OpenAI resource. During or after the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.
@@ -27,8 +21,6 @@ From the Azure OpenAI Studio landing page navigate further to explore examples f
 
 :::image type="content" source="../media/quickstarts/studio-start.png" alt-text="Screenshot of the Azure OpenAI Studio landing page." lightbox="../media/quickstarts/studio-start.png":::
 
-Go to the [Playground](#playground) for experimentation and fine-tuning workflow.
-
 ## Playground
 
 Start exploring Azure OpenAI capabilities with a no-code approach through the GPT-3 Playground. It's simply a text box where you can submit a prompt to generate a completion. From this page, you can quickly iterate and experiment with the capabilities. 
@@ -45,30 +37,23 @@ You can experiment with the configuration settings such as temperature and pre-r
 
 Azure OpenAI also performs content moderation on the prompt inputs and generated outputs. The prompts or responses may be filtered if harmful content is detected. For more information, see the [content filter](../concepts/content-filter.md) article.
 
-In the GPT-3 playground you can also view Python and curl code samples pre-filled according to your selected settings. Just select **View code** next to the examples dropdown. You can write an application to complete the same task with the OpenAI Python SDK, curl, or other REST API client.
+In the Completions playground you can also view Python and curl code samples pre-filled according to your selected settings. Just select **View code** next to the examples dropdown. You can write an application to complete the same task with the OpenAI Python SDK, curl, or other REST API client.
 
 ### Try text summarization
 
-To use the Azure OpenAI for text summarization in the GPT-3 Playground, follow these steps:
+To use the Azure OpenAI for text summarization in the Completions playground, follow these steps:
 
 1. Sign in to [Azure OpenAI Studio](https://oai.azure.com).
 1. Select the subscription and OpenAI resource to work with. 
-1. Select **GPT-3 Playground** at the top of the landing page.
+1. Select **Completions playground** on the landing page.
 1. Select your deployment from the **Deployments** dropdown. If your resource doesn't have a deployment, select **Create a deployment** and then revisit this step.
-1. Select **Summarize Text** from the **Examples** dropdown. 
+1. Enter a prompt for the model.
 
-    :::image type="content" source="../media/quickstarts/summarize-text.png" alt-text="Screenshot of the playground page of the Azure OpenAI Studio with the Summarize Text dropdown selection visible" lightbox="../media/quickstarts/summarize-text.png":::
+    :::image type="content" source="../media/quickstarts/summarize-text.png" alt-text="Screenshot of the playground page of the Azure OpenAI Studio with a text summarization example." lightbox="../media/quickstarts/summarize-text.png":::
 
 1. Select `Generate`. Azure OpenAI will attempt to capture the context of text and rephrase it succinctly. You should get a result that resembles the following text:
 
-    ```
-    Tl;dr A neutron star is the collapsed core of a supergiant star. These incredibly dense objects are incredibly fascinating due to their strange properties and their potential for phenomena such as extreme gravitational forces and a strong magnetic field.
-    ```
-
-The accuracy of the response can vary per model. The Davinci based model in this example is well-suited to this type of summarization, whereas a Codex based model wouldn't perform as well at this particular task.
-
-> [!div class="nextstepaction"]
-> [I ran into an issue with the playground.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=STUDIO&Pillar=AOAI&Product=gpt&Page=quickstart&Section=Set-up)
+The accuracy of the response can vary per model. The `gpt-35-turbo-instruct` based model in this example is well-suited to this type of summarization, though in general we recommend using the alternate chat completions API unless you have a particular use case that is particularly suited to the completions API.
 
 ## Clean up resources
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Azure OpenAI Studioに関するドキュメントの更新"
}
```

### Explanation
このコードの変更は、`studio.md`に関連し、Azure OpenAI Studioに関するドキュメントの一部が更新されました。主な変更内容は、スタジオの使い方を明確にするために、言葉の使い方と構造を改善した点です。

具体的には、日付が更新され、いくつかのフレーズが変更されて「GPT-3 Playground」という表現が「Completions playground」に置き換えられています。この更新によって、ユーザーがAzure OpenAI Studioの機能や使用手順をより理解しやすくなっています。また、サンプルコードの表示やテキスト要約の実行手順についても、現在使用されているモデルに基づいて具体的な指示が与えられています。

さらに、役立つ情報やリソースへのリンクが整理されており、ユーザーが直面する可能性のある課題に対するサポートが強化されています。全体的に、この更新によってドキュメントがより使いやすく、明確な情報を提供する内容になっています。

## articles/ai-services/openai/media/deployment-types/deploy-models.png{#item-c9e3a5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイモデルに関する画像の更新"
}
```

### Explanation
この変更は、`deploy-models.png`という画像ファイルに関連しており、内容の変更はありませんが、画像が更新されました。画像の更新に伴い、デプロイモデルに関するビジュアル情報が最新化されている可能性があります。

この視覚資料は、ユーザーがAzure OpenAIサービスのデプロイメントに関する理解を深めるために重要な役割を果たします。正確で最新の画像を提供することで、ユーザーがより効果的に様々なデプロイメントの種類やそのプロセスを把握できるようになります。

全体として、これは特に重要な情報を視覚的に伝えるための更新であり、ユーザーの学びや体験を向上させることを目的としています。

## articles/ai-services/openai/media/how-to/dynamic-quota/dynamic-quota.png{#item-eaf5dc}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ダイナミッククォータに関する画像の更新"
}
```

### Explanation
この変更は、`dynamic-quota.png`という画像ファイルに関連しており、内容自体の変更はありませんが、画像が更新されました。この更新により、ダイナミッククォータに関する視覚的情報が最新のものとなり、ユーザーにとってより有益な内容になっている可能性があります。

ダイナミッククォータに関する画像は、Azure OpenAIサービスの機能や設定を理解するための重要なリソースであり、ユーザーがその機能を正確に把握できるようにサポートします。最新の画像を提供することで、ユーザーはより効果的にこれらの概念を視覚的に理解できるようになります。

この変更は、Azure OpenAIにおけるユーザーの体験を向上させるための小規模な改善ですが、特に視覚的な情報が重要な役割を果たす分野では価値のある更新です。

## articles/ai-services/openai/media/how-to/working-with-models/update-policy.png{#item-ad6800}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルの更新ポリシーに関する画像の更新"
}
```

### Explanation
この変更は、`update-policy.png`という画像ファイルに関するもので、内容は変更されていませんが、画像が更新されました。この更新により、モデルの更新ポリシーについての視覚的資料が最新化され、より明確な情報をユーザーに提供することができます。

モデルの更新ポリシーに関する画像は、ユーザーがAzure OpenAIサービスを利用する際に、モデル管理や更新に関する理解を深めるために重要です。更新された画像は、視覚的に情報を整理し、ユーザーがプロセスを理解しやすくするために役立つでしょう。

このようなマイナーな更新であっても、視覚的な情報が持つ重要性を考慮すると、ユーザーの体験や学習の質を向上させるための価値ある取り組みです。

## articles/ai-services/openai/media/models/auto-update.png{#item-4e03a7}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "自動更新に関する画像の更新"
}
```

### Explanation
この変更は、`auto-update.png`という画像ファイルに関するもので、内容は変更されていないものの、画像が更新されました。この更新により、自動更新に関する情報が最新化され、Azure OpenAIサービスに関心のあるユーザーに対して、より効果的な視覚的資料を提供します。

自動更新の機能は、ユーザーがシステムやモデルの更新をスムーズに行えるようにするために重要です。更新された画像は、自動更新プロセスやその利点を示すための視覚的なガイダンスを提供し、ユーザーが操作を理解しやすくなるように役立ちます。

このようなマイナーな更新でも、特に技術的な内容では視覚的な情報が大変重要であり、ユーザーの理解を助けるための価値のあるフィードバックとなります。

## articles/ai-services/openai/media/models/column-options.png{#item-768cad}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "カラムオプションに関する画像の削除"
}
```

### Explanation
この変更は、`column-options.png`という画像ファイルが削除されたことを示しています。この変更により、特定のカラムオプションに関する視覚的な情報がもはや利用できなくなり、ユーザーがその内容を参照することができなくなります。

カラムオプションは、ユーザーがデータモデルを操作する際に重要な要素であるため、この画像が削除されることは、ドキュメンテーションやユーザーガイドにおいて情報の欠落を意味します。ユーザーは、カラムオプションについての理解を深めるための追加の資料や情報を必要とする場合があります。

そのため、このような重大な変更は、他の関連コンテンツや資料を補完することが求められるかもしれません。ユーザーに対して、より具体的な情報を提供するための代替案や更新されたリソースを検討する必要があります。

## articles/ai-services/openai/media/models/deployments.png{#item-7217ff}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントに関する画像の更新"
}
```

### Explanation
この変更は、`deployments.png`という画像ファイルが更新されたことを示しています。具体的な変更内容は記載されていませんが、画像が新しい情報やデザインを反映するためにアップデートされた可能性があります。

デプロイメントは、AI サービスやモデルを実稼働環境に展開する際に非常に重要なステップです。この画像の更新により、自動化されたプロセスやベストプラクティスを示すための視覚的な支援が提供され、ユーザーの理解を深めることが期待されます。

この種のマイナーな更新は、特に技術文書やユーザーガイドにおいて、最新の情報を反映させることが重要であり、ユーザーが自信を持ってデプロイメントの作業を進められるよう助ける役割を果たします。更新された画像は、視覚的に分かりやすく、読む人にとっての情報の浸透を助けるでしょう。

## articles/ai-services/openai/media/quickstarts/assistant-session.png{#item-8cb4f9}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アシスタントセッションに関する画像の削除"
}
```

### Explanation
この変更は、`assistant-session.png`という画像ファイルが削除されたことを示しています。この画像は、アシスタントセッションの操作や設定に関連する視覚的なリソースであったと考えられます。そのため、この削除により、ユーザーがアシスタントセッションに関する情報を理解するための重要なビジュアルを失うことになります。

アシスタントセッションは、AI システムとユーザーとの間のインタラクションを管理するための重要な要素です。この画像が削除されることで、ドキュメンテーションやクイックスタートガイドに対して、関係する情報が欠落し、ユーザーがその機能を効果的に利用する際に困難を感じる可能性があります。

このような重要な変更は、ユーザー向けの補完的な情報やリソースの提供を促すものとなります。削除された画像に代わる新しい画像や他の情報源を検討し、ユーザーに適切なサポートを提供することが求められるでしょう。

## articles/ai-services/openai/media/quickstarts/assistants-playground.png{#item-211017}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アシスタントプレイグラウンドに関する画像の削除"
}
```

### Explanation
この変更は、`assistants-playground.png`という画像ファイルが削除されたことを示しています。この画像は、アシスタントプレイグラウンドに関連するインターフェースや機能を視覚的に説明するためのものであったと考えられます。そのため、この削除により、ユーザーがアシスタントプレイグラウンドを利用する際の理解を助ける重要なリソースが失われることになります。

アシスタントプレイグラウンドは、ユーザーが AI モデルとダイレクトに対話し、実験的な操作を行うためのスペースです。この画像の削除は、該当するドキュメントやクイックスタートガイドにおいて、視覚的な手助けがなくなることを意味し、特に新規ユーザーにとっては使い方の把握が難しくなる可能性があります。

このような変更により、補完的な情報や代替の視覚素材が必要とされることになるでしょう。画像に代わる説明や他のリソースを検討し、ユーザーが引き続きアシスタントプレイグラウンドの機能を最大限に活用できるよう、適切な情報提供が求められるでしょう。

## articles/ai-services/openai/media/quickstarts/assistants-studio.png{#item-8f1ba9}

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "アシスタントスタジオに関する画像の削除"
}
```

### Explanation
この変更は、`assistants-studio.png`という画像ファイルが削除されたことを示しています。この画像は、アシスタントスタジオの使い方や機能を視覚的に示すために重要な役割を果たしていたと考えられます。そのため、この削除により、ユーザーがアシスタントスタジオを理解し、利用する際の手助けが減ることになります。

アシスタントスタジオは、AI モデルの構築や調整を行うためのインターフェースであり、ユーザーはここで様々な設定を行います。この画像が削除されることで、ドキュメンテーションやクイックスタートガイドにおいて、アシスタントスタジオの利用方法を視覚的にサポートする情報がなくなるため、特に新しいユーザーはその機能を十分に理解することが難しくなる可能性があります。

このような重要な変更は、代替のビジュアル素材や補完的な情報を提供する必要性を高めるため、今後のドキュメント更新において考慮されるべきです。ユーザーが引き続きアシスタントスタジオの機能を有効に活用できるよう、適切なサポートが求められます。

## articles/ai-services/openai/media/quickstarts/chat-playground.png{#item-cb74b5}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "チャットプレイグラウンドに関する画像の更新"
}
```

### Explanation
この変更は、`chat-playground.png`という画像ファイルが修正されたことを示しています。この画像は、チャットプレイグラウンドに関連する機能やインターフェースを視覚的に説明するために使用されている重要なリソースです。画像の修正により、内容が最新の情報やデザインに合わせて調整されることが期待されます。

チャットプレイグラウンドは、ユーザーが AI モデルと対話する体験を提供するためのプラットフォームです。この画像の更新は、ユーザーに対する視覚的な手助けを強化し、使用方法や機能の理解を助けることを目的としています。修正によって、最新のインターフェースや機能が正確に反映された場合、ユーザー体験が向上し、利用者がより容易にツールを利用できるようになります。

このようなマイナーな更新は、継続的な改善の一環として非常に重要であり、ドキュメント全体のクオリティを向上させる要素となります。ユーザーにとって魅力的で利用しやすい情報を提供し続けることで、彼らの学習や作業がより効果的に支援されることでしょう。

## articles/ai-services/openai/media/quickstarts/chat-view-code.png{#item-74bc20}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "チャットビューコードに関する画像の追加"
}
```

### Explanation
この変更は、新しく`chat-view-code.png`という画像ファイルが追加されたことを示しています。この画像は、チャット機能のコードビューに関連するビジュアル資料であり、ユーザーがより深く理解できるようにするための重要なリソースです。

チャットビューコードは、AIモデルとの対話において、ユーザーが実際に参照することができるコードの表示を提供します。この新しい画像の追加により、ユーザーはチャット機能を具体的に理解し、インタラクションの実装方法についての視覚的なガイダンスを得ることができます。これにより、開発者やデータサイエンティストは、実際のコード例を通じてチャット機能の利用方法を習得しやすくなります。

このような新機能の追加は、ドキュメントの質を向上させるばかりでなく、ユーザーにとっても実践的かつ使いやすい情報を提供することに寄与します。今後の学習やプロジェクトにおいて、特に初心者にとって不可欠な参考資料となるでしょう。

## articles/ai-services/openai/media/quickstarts/chatgpt-playground-load.png{#item-77b058}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPTプレイグラウンドの読み込みに関する画像の更新"
}
```

### Explanation
この変更は、`chatgpt-playground-load.png`という画像ファイルが修正されたことを示しています。この画像は、ChatGPTプレイグラウンドの読み込みプロセスに関連したビジュアル資料です。画像が更新されることで、ユーザーがイメージしやすくなり、チャット体験の準備状況やインターフェースの変化を明確に理解できるようになります。

ChatGPTプレイグラウンドは、ユーザーがAIモデルと効果的に対話できるよう設計されています。この画像の更新は、最新のインターフェースや機能の改訂を反映するためのものであり、ユーザーがプレイグラウンドを使用する際に直面する可能性のある状況を視覚的に示すものです。特に新しいユーザーにとって、このようなビジュアルガイドは非常に有益であり、操作の流れをスムーズに理解する助けとなります。

このマイナーな更新は、ドキュメント全体の品質向上に寄与し、ユーザーの体験を向上させる重要な要素です。ユーザーが具体的なイメージを持ちながら、プレイグラウンドを最大限に活用できるようにすることが目的です。

## articles/ai-services/openai/media/quickstarts/chatgpt-playground.png{#item-ad29b9}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ChatGPTプレイグラウンドの画像の更新"
}
```

### Explanation
この変更は、`chatgpt-playground.png`という画像ファイルが修正されたことを示しています。この画像は、ChatGPTプレイグラウンドの全体的なインターフェースや機能を視覚化したものであり、ユーザーがこのツールを利用する際の理解を助ける重要な資源です。

画像の更新により、プレイグラウンドの最新のデザインや機能に関する情報が反映され、ユーザーは新しいインタフェースを利用する際に、より正確なビジュアルガイドを得ることができます。このような更新は特に、ユーザーがツールを初めて利用する際や、新しい機能を探求している際に有用です。

また、ユーザーがスムーズにChatGPTプレイグラウンドの操作を行うためには、視覚的な情報が役立ちます。このマイナーな更新は、ドキュメントの整合性と最新性を保つために必要なものであり、全体的なユーザー体験の向上に寄与します。

## articles/ai-services/openai/media/quickstarts/dall-e-studio.png{#item-fe085c}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "DALL·Eスタジオに関する画像の更新"
}
```

### Explanation
この変更は、`dall-e-studio.png`という画像ファイルが修正されたことを示しています。この画像は、DALL·Eスタジオの使用方法やインターフェースを視覚的に示すもので、ユーザーがDALL·Eを通じて生成したいコンテンツを簡単に操作できる手助けをします。

画像の更新は、DALL·Eスタジオの最新の機能やデザインの変更を反映しており、ユーザーがより効果的にツールを利用できるようにするための重要なステップです。この変更により、新しいユーザーは特に、既存のインターフェースの理解を深め、ユーザー体験を向上させることができます。

さらに、DALL·Eスタジオは、AIを使用して画像を生成するための強力なツールであるため、視覚的な資料を用いることは、ユーザーがその機能を最大限に活用する上で重要です。このマイナーな更新は、ドキュメントの整合性と正確性を保つためのものであり、全体的なユーザー体験の向上に寄与しています。

## articles/ai-services/openai/media/quickstarts/playground-load.png{#item-e248f0}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "プレイグラウンドのロード画面に関する画像の更新"
}
```

### Explanation
この変更は、`playground-load.png`という画像ファイルが修正されたことを示しています。この画像は、AIサービスのプレイグラウンドが読み込まれている状態を示しており、ユーザーがインターフェースにアクセスした際の体験を具体的に視覚化する役割を果たします。

画像の更新により、プレイグラウンドの最新状態や読み込みプロセスに関する情報が反映され、ユーザーはより正確な表現を基に操作することができます。新しいビジュアル情報は、特に初めてプレイグラウンドを使用するユーザーにとって、導入の手助けとなる重要な要素です。

また、この変更はドキュメントの整合性を保持し、ユーザーが最新のインターフェースに安心してアクセスできるようにするために必要です。全体として、このマイナーな更新は、ユーザー体験の向上とAIサービスの利用促進に寄与しています。

## articles/ai-services/openai/media/quickstarts/studio-start.png{#item-a3bf0f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "スタジオの開始画面に関する画像の更新"
}
```

### Explanation
この変更は、`studio-start.png`という画像ファイルが修正されたことを示しています。この画像は、AIサービスのスタジオ機能が開始される際の画面を示しており、ユーザーがアプリケーションの利用を開始する際の視覚的なガイドとして重要です。

画像の更新により、新しいデザインや機能が反映されている可能性があり、特に新しいユーザーにとって、スタジオのインターフェースを理解する手助けとなります。更新内容は、使いやすさや見た目の改善を目的としたもので、ユーザー体験の向上に寄与します。

このマイナーな変更は、ドキュメント内のビジュアルコンテンツを最新の状態に保つことに寄与し、ユーザーに対してより正確かつ魅力的な情報を提供する役割を果たします。全体として、この画像の更新は、AIサービスの利用を促進し、効果的な導入を示す重要な要素と言えます。

## articles/ai-services/openai/media/quickstarts/summarize-text.png{#item-675e86}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "テキスト要約機能に関する画像の更新"
}
```

### Explanation
この変更は、`summarize-text.png`という画像ファイルが修正されたことを示しています。この画像は、AIサービスのテキスト要約機能を操作する際の画面を視覚的に示しており、ユーザーがその機能の利用方法を理解する手助けをします。

画像の更新によって、テキスト要約機能の最新のインターフェースや使用例が反映されていると考えられます。これにより、新しいユーザーが機能にアクセスする際の理解が深まり、実際の操作に役立つ情報が提供されます。

このマイナーな変更は、ドキュメントのビジュアル要素を最新の状態に保ち、ユーザーに対してより正確で魅力的な情報を提供する重要な役割を果たします。全体として、この画像の更新は、利用者の体験を向上させ、テキスト要約機能の使用を促進するための貴重な要素となります。

## articles/ai-services/openai/media/quota/deployment.png{#item-59cbb2}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "デプロイメントに関する画像の更新"
}
```

### Explanation
この変更は、`deployment.png`という画像ファイルが修正されたことを示しています。この画像は、AIサービスにおけるデプロイメントのプロセスを視覚的に示しており、ユーザーがデプロイメントの流れや要件を理解するのに役立ちます。

画像の更新により、最新のインターフェースや手順が反映されている可能性があり、新規ユーザーがデプロイメントを効果的に行うためのサポートが期待されます。特に、AIサービスの利用方法を示す視覚的ガイドは、ユーザー体験を向上させる重要な要素です。

このマイナーな変更は、ドキュメント内のビジュアルコンテンツを最新の情報にアップデートすることで、ユーザーに対してより正確で魅力的な情報を提供します。全体として、この画像の更新は、デプロイメントの理解を深め、サービスの利用促進に寄与する要素となります。

## articles/ai-services/openai/media/quota/quota.png{#item-b7e319}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クオータに関する画像の更新"
}
```

### Explanation
この変更は、`quota.png`という画像ファイルが修正されたことを示しています。この画像は、AIサービスにおけるクオータの概念や使用方法を視覚的に説明する役割を持っています。

この画像の更新により、ユーザーがクオータに関して持つ可能性のある疑問や理解を深めるための最新の情報が提供されていると考えられます。具体的には、クオータの制限やリソースの使用状況を把握するための重要な視覚補助として機能することが期待されます。

このマイナーな変更は、ドキュメントのビジュアルコンテンツを最新の状態に保つために重要であり、ユーザーに対して正確かつ魅力的な情報を提供します。全体として、この画像の更新は、クオータの理解を深め、AIサービスの利用時の不安を軽減するための貴重な要素となります。

## articles/ai-services/openai/media/use-your-data/bring-your-data-card.png{#item-2e0a7f}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データカードに関する画像の更新"
}
```

### Explanation
この変更は、`bring-your-data-card.png`という画像ファイルが修正されたことを示しています。この画像は、ユーザーが自分のデータをAIサービスに持ち込む際のガイドラインや注意点を視覚的に説明しています。

画像の更新により、最新の情報や手順が反映されている可能性があり、ユーザーが自分のデータを適切に使用できるよう支援する役割を果たします。この視覚的資料は、以下のような重要な情報を伝えるために役立ちます：

- データの持ち込み方法
- データの形式や要件
- ユーザーが知っておくべきベストプラクティス

このマイナーな変更は、ドキュメントのビジュアルコンテンツを常に最新の状態に保つことで、ユーザーに対してより正確で理解しやすい情報を提供します。全体として、この画像の更新は、ユーザーがデータを持ち込む際のプロセスを理解しやすくし、サービスの利用を円滑にするための重要な要素となります。

## articles/ai-services/openai/media/use-your-data/chat-playground.png{#item-fd6d6f}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "チャットプレイグラウンドに関する画像の追加"
}
```

### Explanation
この変更は、`chat-playground.png`という新しい画像ファイルが追加されたことを示しています。この画像は、AIサービスにおけるチャットプレイグラウンドの使用方法を視覚的に説明する役割を果たします。

新たに追加されたこの画像は、ユーザーに対して以下のような情報を提供することを目的としています：

- チャットプレイグラウンドのインターフェイス
- AIモデルとのインタラクションの方法
- 実際の使用例やヒント

この新機能により、ユーザーはチャットプレイグラウンドをより効果的に利用できるようになり、AIとの対話をスムーズに行えることが期待されます。画像は、理解を助けるための視覚的な補助として機能し、特に新たにAIサービスを利用し始めるユーザーにとって有用です。

全体として、この変更は、AIサービスの使いやすさを向上させ、ユーザーが新しい機能をより簡単に理解できるようにするための重要なアップデートです。

## articles/ai-services/openai/quickstart.md{#item-7d1656}

<details>
<summary>Diff</summary>
````diff
@@ -5,7 +5,7 @@ description: Walkthrough on how to get started with Azure OpenAI and make your f
 #services: cognitive-services
 manager: nitinme
 ms.service: azure-ai-openai
-ms.custom: devx-track-dotnet, devx-track-python, devx-track-extended-java, devx-track-js, devx-track-go
+ms.custom: devx-track-dotnet, devx-track-python, devx-track-extended-java, devx-track-js, devx-track-go, devx-track-ts
 ms.topic: quickstart
 author: mrbullwinkle
 ms.author: mbullwin
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "クイックスタートガイドにTypeScriptトラッキングの追加"
}
```

### Explanation
この変更は、`quickstart.md`というファイルの内容が修正され、TypeScript（TS）に関するトラッキング情報が追加されたことを示しています。この文書は、Azure OpenAIを使い始めるための手順を説明するガイドです。

具体的には、`ms.custom`の行に`devx-track-ts`というエントリが追加されました。この変更により、TypeScriptを使用する開発者がこのクイックスタートガイドを参照しやすくなり、開発プロセスの効率が向上します。

このようなマイナーなアップデートは、さまざまなプログラミング言語やフレームワークに対するサポートが強化されることを示しており、特に新しいユーザーや開発者が必要なリソースを見つけやすくするための重要な措置です。全体として、この変更はユーザーに対する情報の包括性を高め、より多くの開発者がこのサービスを利用できるように配慮された内容となっています。

## articles/ai-services/openai/use-your-data-quickstart.md{#item-52c1f4}

<details>
<summary>Diff</summary>
````diff
@@ -16,33 +16,71 @@ zone_pivot_groups: openai-use-your-data
 
 # Quickstart: Chat with Azure OpenAI models using your own data
 
-::: zone pivot="programming-language-spring"
+In this quickstart, you can use your own data with Azure OpenAI models. Using Azure OpenAI's models on your data can provide you with a powerful conversational AI platform that enables faster and more accurate communication.
 
-[Source code](https://github.com/spring-projects-experimental/spring-ai)| [Source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai) | [Sample](https://github.com/rd-1-2022/ai-azure-retrieval-augmented-generation)
+::: zone pivot="programming-language-studio"
 
-::: zone-end
 
-::: zone pivot="programming-language-javascript"
+## Prerequisites
 
-[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+
+> [!div class="nextstepaction"]
+> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=OVERVIEW&Pillar=AOAI&Product=ownData&Page=quickstart&Section=Prerequisites)
+
+
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+
+[!INCLUDE [Studio quickstart](includes/use-your-data-studio.md)]
 
 ::: zone-end
 
-::: zone pivot="programming-language-python"
+::: zone pivot="programming-language-csharp"
 
-[Reference](https://platform.openai.com/docs/api-reference?lang=python) | [Source code](https://github.com/openai/openai-python) | [Package (pypi)](https://pypi.org/project/openai/) | [Samples](https://github.com/openai/openai-cookbook/)
+## Prerequisites
 
-These links reference the OpenAI API for Python. There's no Azure-specific OpenAI Python SDK. [Learn how to switch between the OpenAI services and Azure OpenAI services](/azure/ai-services/openai/how-to/switching-endpoints).
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+- The [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
+
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+
+[!INCLUDE [Csharp quickstart](includes/use-your-data-dotnet.md)]
 
 ::: zone-end
 
-::: zone pivot="programming-language-go"
+::: zone pivot="programming-language-spring"
 
-[Reference](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go) | [Source code](https://github.com/Azure/azure-sdk-for-go) | [Package (Go)](https://pkg.go.dev/github.com/azure/azure-dev) | [Samples](https://github.com/azure-samples/azure-sdk-for-go-samples)
+[Source code](https://github.com/spring-projects-experimental/spring-ai)| [Source code](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai) | [Sample](https://github.com/rd-1-2022/ai-azure-retrieval-augmented-generation)
+
+## Prerequisites
+
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+    
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+
+[!INCLUDE [Spring quickstart](includes/use-your-data-spring.md)]
 
 ::: zone-end
 
-In this quickstart, you can use your own data with Azure OpenAI models. Using Azure OpenAI's models on your data can provide you with a powerful conversational AI platform that enables faster and more accurate communication.
+::: zone pivot="programming-language-javascript"
 
 ## Prerequisites
 
@@ -59,6 +97,7 @@ In this quickstart, you can use your own data with Azure OpenAI models. Using Az
 
 - Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
+
 #### [JavaScript](#tab/javascript)
 
 - An Azure subscription - <a href="https://azure.microsoft.com/free/cognitive-services" target="_blank">Create one for free</a>.
@@ -71,64 +110,92 @@ In this quickstart, you can use your own data with Azure OpenAI models. Using Az
 
 ---
 
-::: zone pivot="programming-language-javascript"
+[Reference documentation](https://platform.openai.com/docs/api-reference/chat) | [Source code](https://github.com/openai/openai-node) | [Package (npm)](https://www.npmjs.com/package/openai) | [Samples](https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai/samples)
 
 
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
-- [Long Term Support (LTS) versions of Node.js](https://github.com/nodejs/release#release-schedule)
+[!INCLUDE [JavaScript quickstart](includes/use-your-data-javascript.md)]
 
 ::: zone-end
 
-> [!div class="nextstepaction"]
-> [I ran into an issue with the prerequisites.](https://microsoft.qualtrics.com/jfe/form/SV_0Cl5zkG3CnDjq6O?PLanguage=OVERVIEW&Pillar=AOAI&Product=ownData&Page=quickstart&Section=Prerequisites)
-
+::: zone pivot="programming-language-python"
 
-[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+## Prerequisites
 
-::: zone pivot="programming-language-studio"
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
-[!INCLUDE [Studio quickstart](includes/use-your-data-studio.md)]
+[Reference](https://platform.openai.com/docs/api-reference?lang=python) | [Source code](https://github.com/openai/openai-python) | [Package (pypi)](https://pypi.org/project/openai/) | [Samples](https://github.com/openai/openai-cookbook/)
 
-::: zone-end
+These links reference the OpenAI API for Python. There's no Azure-specific OpenAI Python SDK. [Learn how to switch between the OpenAI services and Azure OpenAI services](/azure/ai-services/openai/how-to/switching-endpoints).
 
-::: zone pivot="programming-language-csharp"
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
-[!INCLUDE [Csharp quickstart](includes/use-your-data-dotnet.md)]
+[!INCLUDE [Python quickstart](includes/use-your-data-python.md)]
 
 ::: zone-end
 
-::: zone pivot="programming-language-spring"
+::: zone pivot="programming-language-powershell"
 
-[!INCLUDE [Spring quickstart](includes/use-your-data-spring.md)]
 
-::: zone-end
+## Prerequisites
 
-::: zone pivot="programming-language-javascript"
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
-[!INCLUDE [JavaScript quickstart](includes/use-your-data-javascript.md)]
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
-::: zone-end
+[!INCLUDE [PowerShell quickstart](includes/use-your-data-powershell.md)]
 
-::: zone pivot="programming-language-python"
+::: zone-end
 
-[!INCLUDE [Python quickstart](includes/use-your-data-python.md)]
+::: zone pivot="programming-language-go"
 
-::: zone-end
 
-::: zone pivot="programming-language-powershell"
+## Prerequisites
 
-[!INCLUDE [PowerShell quickstart](includes/use-your-data-powershell.md)]
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
 
-::: zone-end
+[Reference](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go) | [Source code](https://github.com/Azure/azure-sdk-for-go) | [Package (Go)](https://pkg.go.dev/github.com/azure/azure-dev) | [Samples](https://github.com/azure-samples/azure-sdk-for-go-samples)
 
-::: zone pivot="programming-language-go"
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
 
 [!INCLUDE [Go quickstart](includes/use-your-data-go.md)]
 
 ::: zone-end
 
 ::: zone pivot="rest-api"
 
+
+## Prerequisites
+
+The following resources: 
+- [Azure OpenAI](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)
+- [Azure Blob Storage](https://portal.azure.com/#create/Microsoft.StorageAccount-ARM)
+- [Azure AI Search](https://portal.azure.com/#create/Microsoft.Search)
+- An [Azure OpenAI resource](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) deployed in a [supported region and with a supported model](./concepts/use-your-data.md#regional-availability-and-model-support).
+    - Be sure that you're assigned at least the [Cognitive Services Contributor](./how-to/role-based-access-control.md#cognitive-services-contributor) role for the Azure OpenAI resource.
+- Download the example data from [GitHub](https://github.com/Azure-Samples/cognitive-services-sample-data-files/blob/master/openai/contoso_benefits_document_example.pdf) if you don't have your own data.
+
+[!INCLUDE [Connect your data to OpenAI](includes/connect-your-data-studio.md)]
+
 [!INCLUDE [REST API quickstart](includes/use-your-data-rest.md)]
 
 ::: zone-end
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "データ利用に関するクイックスタートガイドの大幅な改訂"
}
```

### Explanation
この変更は、`use-your-data-quickstart.md`ファイルの内容が大幅に改訂されたことを示しています。主な改定点は、クイックスタートガイドの情報がより明確かつ豊富になったことです。具体的には、次のような追加と改善が行われています。

1. **概要の追加**: クイックスタートの冒頭部分に、Azure OpenAIモデルとユーザーのデータを使用することが可能であり、どのようにその機能がコミュニケーションを改善するかについて詳細が追加されました。

2. **必須条件のリスト化**: ユーザーがデータを使用するための前提条件が明確にリスト化され、必要なリソースや役割についての詳細が提供されました。例えば、Azure OpenAIリソースをデプロイするためには、適切な地域でSupportedモデルが必要であることが説明されています。

3. **データダウンロードのリンク**: ユーザーがサンプルデータを使えるように、GitHubからの例データリンクが追加されました。これにより、ユーザーは自分のデータを持っていない場合でもすぐに実験を始めることができます。

4. **プログラミング言語別のセクション**: 必須条件が各プログラミング言語セクション毎に明記され、パワーシェルやJavaScript、Pythonなど、さまざまな言語に対する具体的なガイダンスが提供されるようになりました。

このように、変更は主にユーザーにとっての利便性を向上させることを目的としています。また、具体的なリソースやリンクを通じて、ユーザーがより容易に情報にアクセスし、プロジェクトに取り組むことができるようになりました。全体として、この改訂はユーザーの体験を大幅に向上させるものであると評価されます。

## articles/ai-services/openai/whats-new.md{#item-53303b}

<details>
<summary>Diff</summary>
````diff
@@ -10,7 +10,7 @@ ms.custom:
   - ignite-2023
   - references_regions
 ms.topic: whats-new
-ms.date: 9/12/2024
+ms.date: 9/19/2024
 recommendations: false
 ---
 
@@ -20,6 +20,11 @@ This article provides a summary of the latest releases and major documentation u
 
 ## September 2024
 
+### Azure OpenAI Studio UX updates
+
+On September 19, when you access the [Azure OpenAI Studio](https://oai.azure.com/) you'll begin to no longer see the legacy studio UI by default. If needed you'll still be able to go back to the previous experience by using the **Switch to the old look** toggle in the top bar of the UI for the next couple of weeks. If you switch back to legacy Studio UI, it helps if you fill out the feedback form to let us know why. We're actively monitoring this feedback to improve the new experience.
+
+
 ### GPT-4o 2024-08-06 provisioned deployments
 GPT-4o 2024-08-06 is now available for provisioned deployments in East US, East US 2, North Central US, and Sweden Central. It is also available for global provisioned deployments.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "Whats Newページの更新および日付の修正"
}
```

### Explanation
この変更は、`whats-new.md`ファイルの内容に対して行われたマイナーな更新を示しています。主な改訂点は次の通りです。

1. **更新日付の修正**: ドキュメントの最終更新日が2024年9月12日から2024年9月19日に変更されました。これにより、新しい情報が発表されたことが明示されています。

2. **Azure OpenAI StudioのUXアップデートの追加**: 2024年9月19日に、Azure OpenAI Studioにおいてレガシーユーザーインターフェースがデフォルトで表示されなくなる旨の情報が追加されました。ただし、ユーザーは「**Switch to the old look**」トグルを使用して、旧インターフェースに戻ることができることが説明されています。また、フィードバックを求めるフォームの案内も含まれており、ユーザーの意見を反映させる意図が示されています。これにより、新しいユーザーインターフェースへの移行をスムーズに行うためのサポートが提供されています。

3. **GPT-4oのプロビジョニングデプロイメントの情報**: GPT-4oモデル（2024-08-06版）が東アメリカ地域及びスウェーデン中央で利用可能であることが記載されています。これにより、ユーザーは最新のマシンラーニングモデルを利用するための地域やバージョン情報を把握できます。

これらの更新は、ユーザーに対して最新情報を提供し、Azure OpenAIサービスに関する透明性を高めることを目的としています。また、UXの変更に関してユーザーからのフィードバックを重視している姿勢も示されています。全体として、この修正はユーザー体験の向上と、サービスの最新の動向についての理解を促進するものです。


