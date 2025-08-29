---
date: '2025-08-29'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:06c258e...MicrosoftDocs:315e4a8
summary: この変更では、新機能の追加はありませんが、重要な更新が行われました。「プロジェクトを作成する方法」ドキュメントから18行分の手順やナビゲーションが削除され、より簡素化された形で提示されています。また、Markdown要素に関するドキュメントの著者が「tonyeiyalla」から「lajanuar」に変更されました。これにより、組織の透明性やコンテンツの正確性が向上します。ユーザーは新しいガイドラインに従って、新しいプロジェクト作成方法を理解するために再度学習する必要があります。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:06c258e...MicrosoftDocs:315e4a8){target="_blank"}

# ハイライト

## 新機能
- 現在の変更には新機能の追加は含まれていません。

## 重大な変更
- 「プロジェクトを作成する方法」ドキュメントにおいて、特定の手順やナビゲーションに関する18行分の大幅な削除。

## その他の更新
- Markdown要素に関するドキュメントの著者名が「tonyeiyalla」から「lajanuar」に更新されました。

# インサイト

今回の変更において、2つのドキュメントに異なるタイプの更新が加えられました。一つは比較的小さな変更で、もう一つはユーザーに大きなインパクトを与える可能性があります。

まず、Markdown要素に関するドキュメントでの著者の名前が更新されました。これは単にドキュメントの著者情報を最新の状態に保つためのものであり、コンテンツ自体には影響を及ぼしません。しかし、組織の透明性とコンテンツの正確性を維持する上で重要な更新です。このような変更は、むしろ内部のドキュメント管理や著者の責任範囲を明確にすることを目的としています。

次に、「プロジェクトを作成する方法」に関するドキュメントの刷新についてです。この変更は、従来のガイドラインに基づく手順の多くを削除し、ドキュメントをより簡素化した形で提示することを意図しています。これにより、ユーザーが必要な情報に迅速にアクセスしやすくなる一方で、手順が大幅に削除されたため、ユーザーは新しいプロジェクト作成方法を理解するため、現在の操作手順や更新されたガイドラインに関する新しい学習が必要となります。この種の変更は、新しいシステムや手順の導入に伴うものである可能性が高く、最新のプラットフォーム変更に追随するための準備が必要であることを示唆しています。そのため、ユーザーは新しい文書を熟読し、変更点を理解することが求められます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [markdown-elements.md](#item-ec4b62) | minor update | 著者の名前を更新 | modified | 1 | 1 | 2 | 
| [create-project.md](#item-58b2dd) | breaking change | 手順の大幅な削除 | modified | 0 | 18 | 18 | 


# Modified Contents
## articles/ai-services/document-intelligence/concept/markdown-elements.md{#item-ec4b62}

<details>
<summary>Diff</summary>
````diff
@@ -7,7 +7,7 @@ manager: nitinme
 ms.service: azure-ai-document-intelligence
 ms.topic: conceptual
 ms.date: 05/05/2025
-ms.author: tonyeiyalla
+ms.author: lajanuar
 
 ---
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "著者の名前を更新"
}
```

### Explanation
この変更は、Markdown要素に関するドキュメントにおいて、著者名を更新する小的な修正です。具体的には、元の著者名である「tonyeiyalla」が「lajanuar」に置き換えられました。この変更は、ドキュメントの管理をしている担当者の更新を反映するものであり、他の要素は変更されていません。この修正は、ドキュメントの著者情報を最新の状態に保つために重要です。

## articles/ai-services/language-service/conversational-language-understanding/how-to/create-project.md{#item-58b2dd}

<details>
<summary>Diff</summary>
````diff
@@ -53,24 +53,6 @@ A Conversational Language Understanding (CLU) fine-tuning task is a workspace pr
 
 1. In **Create CLU fine-tuning task** window, complete the **Name** and **Language** fields. If you're planning to fine-tune a model using the free **Standard Training** mode, select **English** for the language field.
 
-1. Navigate to the [Azure AI Foundry](https://ai.azure.com/).
-1. If you aren't already signed in, the portal prompts you to do so with your Azure credentials.
-1. Once signed in, you can create or access your existing projects within Azure AI Foundry.
-1. If you're not already at your project for this task, select it.
-1. Select Fine-tuning from the left navigation panel.
-
-    :::image type="content" source="../media/select-fine-tuning.png" alt-text="Screenshot of fine-tuning selector in the Azure AI Foundry.":::
-
-1. Select **the AI Service fine-tuning** tab and then **+ Fine-tune** button.
-
-    :::image type="content" source="../media/fine-tune-button.png" alt-text="Screenshot of fine-tuning button in the Azure AI Foundry.":::
-
-1. From **Create service fine-tuning** window, choose the **Conversational language understanding** tab then select **Next**.
-
-    :::image type="content" source="../media/select-project.png" alt-text="Screenshot of conversational language understanding selection card in the Azure AI Foundry.":::
-
-1. In **Create CLU fine tuning task** window, select your **Connected service** from the drop-down menu, then complete the **Name** and **Language** fields. If you're using the free **Standard Training** mode, select **English** for the language field.
-
 1. Select the  **Create** button. It can take a few minutes for the *creating* operation to complete.
 
 
````
</details>

### Summary

```json
{
    "modification_type": "breaking change",
    "modification_title": "手順の大幅な削除"
}
```

### Explanation
この変更は、「プロジェクトを作成する方法」についてのドキュメントにおける18行の手順を削除する大幅な変更です。具体的には、Azure AI Foundryにおける特定の手順、ナビゲーション、そして画像の追加情報が削除されました。この変更により、読者はCLTファインチューニングタスクの作成手順を簡潔に理解できるようになりましたが、削除された手順は以前のガイドラインに基づくものであったため、理解する上での参照が失われてしまいます。これにより、ユーザーが新しい情報に基づいてプロジェクトを作成する方法を再検討する必要があります。


