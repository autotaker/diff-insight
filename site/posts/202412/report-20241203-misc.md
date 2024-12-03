---
date: '2024-12-03'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fffd4c5...MicrosoftDocs:3b6e85f
summary: このコード差分では、AIスタジオ関連のドキュメントに対して複数の変更が行われ、主に新機能の追加、破壊的変更、そしてマイナーなアップデートが含まれています。特に、コンテンツフィルターに関連する重要な情報が削除された一方で、フィルターの作成手順が新たに詳述されたことが注目されます。また、リダイレクション設定の追加やドキュメントの整合性向上が図られ、ユーザーにとってより使いやすいリソースが提供されるよう改善されています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:fffd4c5...MicrosoftDocs:3b6e85f){target="_blank"}

# Highlights

このコード差分では、AIスタジオ関連のドキュメントに対する複数の変更が行われています。主なハイライトとして、新しい機能の追加や破壊的変更、マイナーなアップデートが含まれます。特に注目すべきは、コンテンツフィルター関連の大幅な削除と新規追加です。これにより、ユーザーは新たに提供されたリソースを活用しやすくなる一方で、一部の情報が削除された影響も受けます。

## New features

- `articles/ai-studio/includes/create-content-filter.md`の新規追加により、コンテンツフィルターの作成手順が詳述されました。
- `articles/ai-studio/media/content-safety/content-filter/`ディレクトリに新しい画像ファイルが追加され、入力フィルター、複数フィルター、および出力フィルターの設定が視覚的にサポートされました。

## Breaking changes

- `articles/ai-studio/concepts/content-filtering.md`では、コンテンツフィルターの設定に関する内容が大幅に削除され、ユーザーがフィルタリング機能を十分に理解するための情報が減少しました。

## Other updates

- `articles/ai-studio/.openpublishing.redirection.ai-studio.json`に新たなリダイレクション設定が追加され、関連する記事へのアクセスが改善されました。
- モデルライフサイクル関連のファイル名変更によりリンクが修正され、ドキュメント間の整合性が向上しました。
- `articles/ai-studio/media/concepts/ai-studio-architecture.png`の画像が更新され、情報の明確さが改善されました。

# Insights

このコード差分は、AIスタジオに関連するドキュメントやメディア資源について多角的な改善を目指しています。具体的には、ユーザーが新しいリソースをより直感的に利用できるようにするための更新がいくつか含まれています。以下に、各変更の背景や意図について詳しく見ていきます。

まず、`articles/ai-studio/.openpublishing.redirection.ai-studio.json`へのリダイレクション設定の追加は、ユーザーが関連するコンテンツにスムーズにアクセスできることを目的としています。モデルライフサイクルや退役に関する重要な情報を逃すことなく、利用者が必要な資料を見つけやすくするための工夫です。

次に、コンテンツフィルターに関するドキュメントの大幅な削除は、旧カンテンツの再編成や簡素化を試みた可能性がありますが、これにより一部の具体的な情報が欠落し、ユーザーの理解を阻害するリスクがあります。その空白を埋めるために、`articles/ai-studio/includes/create-content-filter.md`が新たに追加され、フィルター作成の具体的な方法を詳細に説明している点は評価できます。これにより、ユーザーは新しいフィルターを自信を持って設定・活用できるように支援されています。

加えて、視覚素材として新たに提供された画像は、コンテンツフィルターの使用を視覚的に導く役割を果たします。こうしたビジュアルコンテンツにより、ユーザーは文書だけでは理解しづらかった設定手順をより直感的に把握でき、実用性が高まります。

また、ファイル名の変更や目次ファイルのアップデートは、ドキュメント全体の一貫性を確保し、ナビゲーションの精度を向上させるための修正です。このような細かい修正作業が、ユーザーエクスペリエンスを高め、文書の管理のしやすさを向上させます。

最後に、AIスタジオのアーキテクチャ画像の更新に関しては、視覚的な情報の明確さを高めるためのものと推測されます。具体的な変更内容が公開されていないため、ユーザーには新しい画像を確認してもらうのが良いでしょう

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [.openpublishing.redirection.ai-studio.json](#item-c75c21) | minor update | AIスタジオのリダイレクション設定の更新 | modified | 5 | 0 | 5 | 
| [content-filtering.md](#item-91b372) | breaking change | コンテンツフィルターの設定大幅削除 | modified | 1 | 53 | 54 | 
| [model-lifecycle-retirement.md](#item-f0fc21) | minor update | モデルライフサイクルの退役に関するファイル名変更 | renamed | 0 | 0 | 0 | 
| [create-content-filter.md](#item-2ecb6b) | new feature | コンテンツフィルター作成手順の新規追加 | added | 76 | 0 | 76 | 
| [ai-studio-architecture.png](#item-a522c6) | minor update | AIスタジオアーキテクチャ画像の修正 | modified | 0 | 0 | 0 | 
| [input-filter.png](#item-83c3ae) | new feature | 入力フィルターの新しい画像追加 | added | 0 | 0 | 0 | 
| [multiple.png](#item-47ca54) | new feature | 複数コンテンツフィルターの新しい画像追加 | added | 0 | 0 | 0 | 
| [output-filter.png](#item-8376b9) | new feature | 出力フィルターの新しい画像追加 | added | 0 | 0 | 0 | 
| [toc.yml](#item-2745cd) | minor update | 目次ファイルのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-studio/.openpublishing.redirection.ai-studio.json{#item-c75c21}

<details>
<summary>Diff</summary>
````diff
@@ -110,6 +110,11 @@
             "redirect_url": "/azure/ai-studio/concepts/model-benchmarks",
             "redirect_document_id": true
         },
+        {
+            "source_path_from_root": "/articles/ai-studio/concepts/model-lifecycle-and-retirement.md",
+            "redirect_url": "/azure/ai-studio/concepts/model-lifecycle-retirement",
+            "redirect_document_id": true
+        },
         {
             "source_path_from_root": "/articles/ai-studio/how-to/llmops-azure-devops-prompt-flow.md",
             "redirect_url": "/azure/machine-learning/prompt-flow/how-to-end-to-end-llmops-with-prompt-flow",
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオのリダイレクション設定の更新"
}
```

### Explanation
この変更は、`articles/ai-studio/.openpublishing.redirection.ai-studio.json`ファイルにおけるリダイレクション設定のマイナーな更新を示しています。具体的には、5つの行が追加されていますが、削除はありません。新たに追加されたリダイレクション設定は、モデルのライフサイクルや退役に関する記事へのリンクを提供します。この変更により、ユーザーは新しいリダイレクションURLを通じて、より関連性の高いコンテンツにアクセスできるようになります。

## articles/ai-studio/concepts/content-filtering.md{#item-91b372}

<details>
<summary>Diff</summary>
````diff
@@ -69,59 +69,7 @@ You can also enable the following special output filters:
 - Protected material for code: Protected material code describes source code that matches a set of source code from public repositories, which can be outputted by large language models without proper citation of source repositories.
 - Groundedness: The groundedness detection filter detects whether the text responses of large language models (LLMs) are grounded in the source materials provided by the users.
 
-## Create a content filter
-
-For any model deployment in [Azure AI Foundry](https://ai.azure.com), you can directly use the default content filter, but you might want to have more control. For example, you could make a filter stricter or more lenient, or enable more advanced capabilities like prompt shields and protected material detection.
-
-Follow these steps to create a content filter:
-
-1. Go to AI Foundry and navigate to your project/ hub. Then select the Safety+ Security tab on the left nav and select the Content Filters.
-    :::image type="content" source="../media/content-safety/content-filter/create-content-filter.png" alt-text="Screenshot of the button to create a new content filter." lightbox="../media/content-safety/content-filter/create-content-filter.png":::
-
-1. On the **Basic information** page, enter a name for your content filter. Select a connection to associate with the content filter. Then select **Next**.
-
-    :::image type="content" source="../media/content-safety/content-filter/create-content-filter-basic.png" alt-text="Screenshot of the option to select or enter basic information such as the filter name when creating a content filter." lightbox="../media/content-safety/content-filter/create-content-filter-basic.png":::
-
-1. Select **Create content filter**.
-1. On the **Input filters** page, you can set the filter for the input prompt. Set the action and severity level threshold for each filter type. You configure both the default filters and other filters (like Prompt Shields for jailbreak attacks) on this page. Then select **Next**.
-
-    :::image type="content" source="../media/content-safety/content-filter/configure-threshold.png" alt-text="Screenshot of the option to select input filters when creating a content filter." lightbox="../media/content-safety/content-filter/configure-threshold.png":::
-
-    Content will be annotated by category and blocked according to the threshold you set. For the violence, hate, sexual, and self-harm categories, adjust the slider to block content of high, medium, or low severity.
-
-1. On the **Output filters** page, you can configure the output filter, which will be applied to all output content generated by your model. Configure the individual filters as before. This page also provides the Streaming mode option, which lets you filter content in near-real-time as it's generated by the model, reducing latency. When you're finished select **Next**. 
-    
-    Content will be annotated by each category and blocked according to the threshold. For violent content, hate content, sexual content, and self-harm content category, adjust the threshold to block harmful content with equal or higher severity levels.
-
-1. Optionally, on the **Deployment** page, you can associate the content filter with a deployment. If a selected deployment already has a filter attached, you must confirm that you want to replace it. You can also associate the content filter with a deployment later. Select **Create**.
-
-    :::image type="content" source="../media/content-safety/content-filter/create-content-filter-deployment.png" alt-text="Screenshot of the option to select a deployment when creating a content filter." lightbox="../media/content-safety/content-filter/create-content-filter-deployment.png":::
-
-    Content filtering configurations are created at the hub level in AI Foundry portal. Learn more about configurability in the [Azure OpenAI docs](/azure/ai-services/openai/how-to/content-filters).
-
-1. On the **Review** page, review the settings and then select **Create filter**.
-
-### Use a blocklist as a filter
-
-You can apply a blocklist as either an input or output filter, or both. Enable the **Blocklist** option on the **Input filter** and/or **Output filter** page. Select one or more blocklists from the dropdown, or use the built-in profanity blocklist. You can combine multiple blocklists into the same filter.
-
-## Apply a content filter
-
-The filter creation process gives you the option to apply the filter to the deployments you want. You can also change or remove content filters from your deployments at any time.
-
-Follow these steps to apply a content filter to a deployment:
-
-1. Go to [Azure AI Foundry](https://ai.azure.com) and select a hub and project.
-1. Select **Models + endpoints** on the left pane and choose one of your deployments, then select **Edit**.
-
-    :::image type="content" source="../media/content-safety/content-filter/deployment-edit.png" alt-text="Screenshot of the button to edit a deployment." lightbox="../media/content-safety/content-filter/deployment-edit.png":::
-
-1. In the **Update deployment** window, select the content filter you want to apply to the deployment.
-
-    :::image type="content" source="../media/content-safety/content-filter/apply-content-filter.png" alt-text="Screenshot of apply content filter." lightbox="../media/content-safety/content-filter/apply-content-filter.png":::
-
-Now, you can go to the playground to test whether the content filter works as expected.
-
+[!INCLUDE [create-content-filter](../includes/create-content-filter.md)]
 
 ### Configurability (preview)
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "コンテンツフィルターの設定大幅削除"
}
```

### Explanation
この変更は、`articles/ai-studio/concepts/content-filtering.md`ファイルに対して行われた重要な変更を示しており、53行の削除と1行の追加が含まれています。その結果として、全体で54行の変更が加えられました。主な変更点は、コンテンツフィルターの設定に関する詳細な手順や説明が大幅に削除されたことです。これにより、ユーザーは以前のバージョンに比べてフィルタリング機能の使用方法についての具体的な情報を失ってしまいます。新たに追加された行は、フィルター作成に関する重要な情報を示していますが、全体としては情報量が大幅に減少しています。この変更は、ドキュメントの内容に大きな影響を与える可能性があります。

## articles/ai-studio/concepts/model-lifecycle-retirement.md{#item-f0fc21}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "モデルライフサイクルの退役に関するファイル名変更"
}
```

### Explanation
この変更は、`articles/ai-studio/concepts/model-lifecycle-and-retirement.md`というファイルの名前が変更され、新しい名前は`articles/ai-studio/concepts/model-lifecycle-retirement.md`となったことを示しています。この変更には追加や削除はなく、内容の変更も行われていません。そのため、ドキュメントの内容に影響はありませんが、ファイル名がより簡潔になっています。このファイル名の変更は、モデルライフサイクルの退役に関する情報の整理や、利用者にとっての可読性向上を目的としている可能性があります。

## articles/ai-studio/includes/create-content-filter.md{#item-2ecb6b}

<details>
<summary>Diff</summary>
````diff
@@ -0,0 +1,76 @@
+---
+title: include file
+description: include file
+author: PatrickFarley
+ms.reviewer: pafarley
+ms.author: pafarley
+ms.service: azure-ai-studio
+ms.topic: include
+ms.date: 11/25/2024
+ms.custom: include
+---
+
+
+## Create a content filter in Azure AI Foundry
+
+For any model deployment in [Azure AI Foundry](https://ai.azure.com), you can directly use the default content filter, but you might want to have more control. For example, you could make a filter stricter or more lenient, or enable more advanced capabilities like prompt shields and protected material detection.
+
+> [!TIP]
+> For guidance with content filters in your Azure AI Foundry project, you can read more at [Azure AI Foundry content filtering](/azure/ai-studio/concepts/content-filtering).
+
+Follow these steps to create a content filter:
+
+1. Go to [Azure AI Foundry](https://ai.azure.com) and navigate to your project. Then select the **Safety + security** page from the left menu and select the **Content filters** tab.
+
+    :::image type="content" source="../media/content-safety/content-filter/create-content-filter.png" alt-text="Screenshot of the button to create a new content filter." lightbox="../media/content-safety/content-filter/create-content-filter.png":::
+1. Select **+ Create content filter**.
+1. On the **Basic information** page, enter a name for your content filtering configuration. Select a connection to associate with the content filter. Then select **Next**.
+
+    :::image type="content" source="../media/content-safety/content-filter/create-content-filter-basic.png" alt-text="Screenshot of the option to select or enter basic information such as the filter name when creating a content filter." lightbox="../media/content-safety/content-filter/create-content-filter-basic.png":::
+
+    Now you can configure the input filters (for user prompts) and output filters (for model completion). 
+1. On the **Input filters** page, you can set the filter for the input prompt. For the first four content categories there are three severity levels that are configurable: Low, medium, and high. You can use the sliders to set the severity threshold if you determine that your application or usage scenario requires different filtering than the default values. 
+    Some filters, such as Prompt Shields and Protected material detection, enable you to determine if the model should annotate and/or block content. Selecting **Annotate only** runs the respective model and return annotations via API response, but it will not filter content. In addition to annotate, you can also choose to block content.
+
+    If your use case was approved for modified content filters, you receive full control over content filtering configurations and can choose to turn filtering partially or fully off, or enable annotate only for the content harms categories (violence, hate, sexual and self-harm).
+
+    Content will be annotated by category and blocked according to the threshold you set. For the violence, hate, sexual, and self-harm categories, adjust the slider to block content of high, medium, or low severity.
+
+    :::image type="content" source="../media/content-safety/content-filter/input-filter.png" alt-text="Screenshot of input filter screen.":::
+1. On the **Output filters** page, you can configure the output filter, which will be applied to all output content generated by your model. Configure the individual filters as before. This page also provides the Streaming mode option, which lets you filter content in near-real-time as it's generated by the model, reducing latency. When you're finished select **Next**. 
+    
+    Content will be annotated by each category and blocked according to the threshold. For violent content, hate content, sexual content, and self-harm content category, adjust the threshold to block harmful content with equal or higher severity levels.
+
+    :::image type="content" source="../media/content-safety/content-filter/output-filter.png" alt-text="Screenshot of output filter screen.":::
+1. Optionally, on the **Deployment** page, you can associate the content filter with a deployment. If a selected deployment already has a filter attached, you must confirm that you want to replace it. You can also associate the content filter with a deployment later. Select **Create**.
+
+    :::image type="content" source="../media/content-safety/content-filter/create-content-filter-deployment.png" alt-text="Screenshot of the option to select a deployment when creating a content filter." lightbox="../media/content-safety/content-filter/create-content-filter-deployment.png":::
+
+    Content filtering configurations are created at the hub level in the Azure AI Foundry portal. Learn more about configurability in the [Azure OpenAI Service documentation](/azure/ai-services/openai/how-to/content-filters).
+
+
+1. On the **Review** page, review the settings and then select **Create filter**.
+
+### Use a blocklist as a filter
+
+You can apply a blocklist as either an input or output filter, or both. Enable the **Blocklist** option on the **Input filter** and/or **Output filter** page. Select one or more blocklists from the dropdown, or use the built-in profanity blocklist. You can combine multiple blocklists into the same filter.
+
+## Apply a content filter
+
+The filter creation process gives you the option to apply the filter to the deployments you want. You can also change or remove content filters from your deployments at any time.
+
+Follow these steps to apply a content filter to a deployment:
+
+1. Go to [Azure AI Foundry](https://ai.azure.com) and select a project.
+1. Select **Models + endpoints** on the left pane and choose one of your deployments, then select **Edit**.
+
+    :::image type="content" source="../media/content-safety/content-filter/deployment-edit.png" alt-text="Screenshot of the button to edit a deployment." lightbox="../media/content-safety/content-filter/deployment-edit.png":::
+
+1. In the **Update deployment** window, select the content filter you want to apply to the deployment. Then select **Save and close**.
+
+    :::image type="content" source="../media/content-safety/content-filter/apply-content-filter.png" alt-text="Screenshot of apply content filter." lightbox="../media/content-safety/content-filter/apply-content-filter.png":::
+
+    You can also edit and delete a content filter configuration if required. Before you delete a content filtering configuration, you will need to unassign and replace it from any deployment in the **Deployments** tab.
+
+Now, you can go to the playground to test whether the content filter works as expected.
+
````
</details>

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "コンテンツフィルター作成手順の新規追加"
}
```

### Explanation
この変更は、`articles/ai-studio/includes/create-content-filter.md`ファイルに76行分の新しい内容が追加されたことを示しています。この新規追加により、Azure AI Foundryにおけるコンテンツフィルターの作成手順や設定オプションに関する詳細なガイドが提供されています。具体的には、フィルターの構成方法、入力と出力のフィルター設定、ブロックリストの使用方法、フィルターをデプロイメントに適用する手順などが説明されています。また、スクリーンショットを用いて各ステップを視覚的にサポートする内容も含まれています。この新しいコンテンツは、ユーザーがコンテンツフィルターを効果的に作成・管理するための貴重なリソースとなります。

## articles/ai-studio/media/concepts/ai-studio-architecture.png{#item-a522c6}

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "AIスタジオアーキテクチャ画像の修正"
}
```

### Explanation
この変更は、`articles/ai-studio/media/concepts/ai-studio-architecture.png`ファイルが修正されたことを示しています。この修正には具体的な行の追加や削除はありませんが、画像が更新されたことにより、ファイル内容に何らかの改善が加えられたと考えられます。おそらく、視覚的なデザインや情報の明確さを向上させるための変更が行われており、利用者がAIスタジオのアーキテクチャを理解しやすくするための意図があります。具体的な変更点の内容は提供されていないため、画像を直接確認することが推奨されます。

## articles/ai-studio/media/content-safety/content-filter/input-filter.png{#item-83c3ae}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "入力フィルターの新しい画像追加"
}
```

### Explanation
この変更は、`articles/ai-studio/media/content-safety/content-filter/input-filter.png`という新しい画像ファイルが追加されたことを示しています。この画像は、コンテンツフィルターの入力フィルター設定に関連しており、ユーザーが設定プロセスを視覚的に理解しやすくするための補助材料となります。具体的な内容やデザインは示されていませんが、画像が提供されることにより、手順の説明がより明確になり、利用者にとって情報が把握しやすくなります。この新しい視覚素材は、コンテンツフィルター機能の使い方を説明するドキュメントの品質を向上させることが期待されます。

## articles/ai-studio/media/content-safety/content-filter/multiple.png{#item-47ca54}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "複数コンテンツフィルターの新しい画像追加"
}
```

### Explanation
この変更は、`articles/ai-studio/media/content-safety/content-filter/multiple.png`という新しい画像ファイルが追加されたことを示しています。この画像は、複数のコンテンツフィルターの設定や機能に関連している可能性が高く、ユーザーがそれらをより効果的に利用するための参考資料となります。具体的な画像の内容は提供されていませんが、追加されたことにより、複雑な設定や選択肢に関する理解が促進され、利用者に対して視覚的な手助けを提供することが期待されます。この新しい素材により、AIスタジオのコンテンツフィルター機能に関するドキュメントの充実度が向上し、ユーザーエクスペリエンスが改善されるでしょう。

## articles/ai-studio/media/content-safety/content-filter/output-filter.png{#item-8376b9}

### Summary

```json
{
    "modification_type": "new feature",
    "modification_title": "出力フィルターの新しい画像追加"
}
```

### Explanation
この変更は、`articles/ai-studio/media/content-safety/content-filter/output-filter.png`という新しい画像ファイルが追加されたことを示しています。この画像は、コンテンツフィルターの出力フィルター機能に関連していると考えられ、ユーザーが出力設定を理解するためのビジュアルガイドとして機能します。具体的な内容は示されていないものの、画像の追加により、利用者が設定手順や結果を視覚的に把握しやすくなります。これにより、AIスタジオのコンテンツフィルターの使用に関するドキュメントの理解度と質が向上することが期待されます。新しい画像は、ユーザーが出力フィルターを効果的に活用できるよう支援する要素ともなるでしょう。

## articles/ai-studio/toc.yml{#item-2745cd}

<details>
<summary>Diff</summary>
````diff
@@ -92,7 +92,7 @@ items:
     - name: Data, privacy, and security for Model Catalog
       href: how-to/concept-data-privacy.md
     - name: Model lifecycle and retirement
-      href: concepts/model-lifecycle-and-retirement.md
+      href: concepts/model-lifecycle-retirement.md
     - name: Model benchmarks
       href: how-to/model-benchmarks.md
     - name: Model benchmarking
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "目次ファイルのリンク修正"
}
```

### Explanation
この変更は、`articles/ai-studio/toc.yml`という目次ファイルの修正を示しています。具体的には、「Model lifecycle and retirement」という項目のリンクが更新されており、ファイル名が`concepts/model-lifecycle-and-retirement.md`から`concepts/model-lifecycle-retirement.md`に変更されています。この修正により、リンク先のドキュメントの名前が正確に反映され、ユーザーが適切な情報にアクセスしやすくなります。また、全体のリストの整合性が保たれ、文書の質が向上することが期待されます。目次はユーザーにとって重要なナビゲーション要素であるため、この変更は文書の使いやすさを大幅に改善するでしょう。


