---
date: '2025-07-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2645652...MicrosoftDocs:1d05d59
summary: |-
  この報告の要約は以下の通りです。

  言語スタジオのクイックスタートマニュアルに、Azure AI Languageリソースを利用する際のストレージアクセス権に関する説明が追加されました。この変更は「Storage Blob Data Contributor」ロールの重要性を強調しており、特にAzureに不慣れなユーザーが適切にアクセス権を設定する手助けとなります。破壊的な変更はなく、全体としてドキュメントのユーザビリティが向上し、Azure AI Languageリソースの効果的な運用を支援します。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:2645652...MicrosoftDocs:1d05d59){target="_blank"}

<format>
# ハイライト
言語スタジオのクイックスタートマニュアルに、Azure AI Languageリソース利用時のストレージアクセス権についての説明が追加されました。この変更は、必要なストレージアカウントの「Storage Blob Data Contributor」ロールの重要性を強調しています。

## 新機能
この更新自体は新機能の追加ではありませんが、ユーザーの理解を助けるための情報が追加されました。

## 破壊的変更
特に破壊的な変更はありません。

## その他の更新
説明の追加により、ユーザーガイドがより詳しくなりました。

# インサイト
この変更はユーザーエクスペリエンスの向上を目的としています。Azure AI Languageサービスを活用する際にはリソースを正しく設定する必要があり、その設定の一部としてストレージアカウントへのアクセス権限の設定が求められます。この更新によって、特にAzureに不慣れなユーザーでも適切にアクセス権を設定する方法を理解しやすくなります。

具体的には、ストレージアカウント関連の設定として「Storage Blob Data Contributor」ロールを追加しなければならないことを念押しすることで、後々のアクセスエラーやトラブルを回避する手助けをします。この細やかな配慮が、開発者や管理者が日常的に直面する問題を事前に防ぐ効果をもたらします。

結論として、この更新はドキュメントのユーザビリティを向上させるものであり、Azure AI Languageリソースの迅速かつ効果的な運用に寄与するものです。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [language-studio.md](#item-1caefc) | minor update | 言語スタジオのクイックスタートにストレージアクセス権の説明を追加 | modified | 2 | 0 | 2 | 


# Modified Contents
## articles/ai-services/language-service/custom-text-classification/includes/quickstarts/language-studio.md{#item-1caefc}

<details>
<summary>Diff</summary>
````diff
@@ -23,6 +23,8 @@ Before you can use custom text classification, you'll need to create an Azure AI
 > To quickly get started, we recommend creating a new Azure AI Language resource using the steps provided in this article. Using the steps in this article will let you create the Language resource and storage account at the same time, which is easier than doing it later.
 >
 > If you have a [pre-existing resource](../../how-to/create-project.md#using-a-pre-existing-language-resource) that you'd like to use, you will need to connect it to storage account.
+>
+> Adding the role **Storage Blob Data Contributor** is essential for interacting with *any resource* that utilizes the storage account.
 
 [!INCLUDE [create a new resource from the Azure portal](../resource-creation-azure-portal.md)]
     
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語スタジオのクイックスタートにストレージアクセス権の説明を追加"
}
```

### Explanation
このコードの変更は、「言語スタジオ」のクイックスタートマニュアルに2行の説明を追加する内容です。具体的には、Azure AI Languageリソースを使用する際に必要なストレージアカウントへのアクセス権限について触れています。変更内容としてはストレージアカウントを利用する際に「Storage Blob Data Contributor」ロールを追加する重要性を強調しています。この更新により、ユーザーがリソースにアクセスするために必要な設定を理解しやすくなります。


