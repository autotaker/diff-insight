---
date: '2025-07-13'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:acf364a...MicrosoftDocs:3f50d3b
summary: この変更は、Azureポータルにおけるドキュメントインテリジェンスサービスのリソース作成に関する説明文の用語を微調整し、一貫性を高めることを目的としています。新しい機能は追加されておらず、互換性を損なう変更もありません。主な用語の変更は「特定のAzureサーバー地域」から「特定のAzure地域」への修正です。この微細な変更は、技術文書の用語の一貫性を確保し、利用者がより明確に内容を理解する手助けとなります。また、フェイルオーバーや負荷分散に関する情報には変更がなく、文書の質が向上していることが示されています。全体として、利用者がAzure環境を設定する際に正確な情報に基づいて判断できるよう、文書の改善に注力しています。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:acf364a...MicrosoftDocs:3f50d3b){target="_blank"}

<format>
# ハイライト
この変更は、Azureポータルでのドキュメントインテリジェンスサービスのリソース作成についての説明文における用語の微調整を行うもので、主に用語の一貫性を高めることを目的としています。

## 新機能
特に新しい機能は追加されていません。

## 互換性を損なう変更
ありません。

## その他の更新
用語の変更のみで、他の内容には影響を及ぼさない修正です。

# インサイト
Azureのドキュメントインテリジェンスサービスに関するこの微細な変更は、主に説明文をより明確にし、一貫性を持たせるためのものです。具体的には「特定のAzureサーバー地域」が「特定のAzure地域」と修正されました。この変更は非常に些細に見えるかもしれませんが、技術文書においては用語の一貫性が重要です。用語が統一されることで、利用者はより直感的にシステムを理解することができ、不必要な混乱を避けることができます。

また、本文にはフェイルオーバーや負荷分散に関する情報が含まれていますが、それらの内容には一切変更は加えられておらず、ドキュメント作成のためのガイドラインもしっかりと継続しています。このように、基本機能やユーザーエクスペリエンスに影響を与えない範囲で、文書の品質が向上していると言えます。つまり、利用者がAzure環境を設定する際に正確な情報に基づいて判断を下せるよう、文書の改善に注力していることが伺えます。
</format>

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [disaster-recovery.md](#item-97e0e7) | minor update | ドキュメントインテリジェンスのリソース作成に関する説明の修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/ai-services/document-intelligence/how-to-guides/disaster-recovery.md{#item-97e0e7}

<details>
<summary>Diff</summary>
````diff
@@ -33,7 +33,7 @@ ms.author: lajanuar
 
 ::: moniker range=">= doc-intel-2.1.0"
 
-When you create a Document Intelligence resource in the Azure portal, you specify a region. From then on, your resource and all of its operations stay associated with that particular Azure server region. It's rare, but not impossible, to encounter a network issue that hits an entire region. If your solution needs to always be available, then you should design it to either fail-over into another region or split the workload between two or more regions. Both approaches require at least two Document Intelligence resources in different regions and the ability to sync custom models and classifiers across regions.
+When you create a Document Intelligence resource in the Azure portal, you specify a region. From then on, your resource and all of its operations stay associated with that particular Azure region. It's rare, but not impossible, to encounter a network issue that hits an entire region. If your solution needs to always be available, then you should design it to either fail-over into another region or split the workload between two or more regions. Both approaches require at least two Document Intelligence resources in different regions and the ability to sync custom models and classifiers across regions.
 
 The Copy API enables this scenario by allowing you to copy custom models and classifiers from one Document Intelligence account or into others, which can exist in any supported geographical region. This guide shows you how to use the Copy REST API with cURL for custom models. You can also use an HTTP request service to issue the requests.
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ドキュメントインテリジェンスのリソース作成に関する説明の修正"
}
```

### Explanation
この変更は、Azureポータルでのドキュメントインテリジェンスリソース作成時における地域に関連する説明文の微修正です。具体的には、「特定のAzureサーバー地域」という表現から「特定のAzure地域」という用語に変更されています。これにより、用語の一貫性が向上し、文書全体の明瞭性が強化されます。この修正は、他の地域へのフェイルオーバーや負荷の分散に関する情報を含んだ内容に影響を与えず、APIの使用経験に関する指針も提供されています。


