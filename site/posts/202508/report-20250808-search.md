---
date: '2025-08-08'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:09b644a...MicrosoftDocs:ba81df5
summary: このコード差分は、ネットワークセキュリティパーメーターに関する文書の軽微な更新を行ったものです。著者情報の修正、文書の最終更新日の変更、重要な注意事項の表現修正が含まれていますが、新機能や破壊的変更はありません。この更新は、文書の信頼性を高め、ユーザーエクスペリエンスを向上させることを目的としています。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:09b644a...MicrosoftDocs:ba81df5){target="_blank"}

# ハイライト
このコード差分は、ネットワークセキュリティパーメーターの検索サービスに関する文書の軽微な更新を行ったものです。更新には、著者情報の修正や文書の最終更新日の変更、重要な注意事項の表現修正が含まれています。また、特に新しい機能や破壊的変更については報告されていません。

## 新機能
- 特に新機能の追加は記載されていません。

## 破壊的変更
- なし。

## その他の更新
- 著者情報がMattGotteinerからhaileytapに変更。
- 文書の最終更新日が2025年5月29日から2025年8月7日に変更。
- 重要な通知文の改良により、サービスの一般提供に関する内容が明確化。

# 洞察
この更新は、ネットワークセキュリティパーメーターに関する文書をより分かりやすくすることを目的として行われています。まず、著者情報が変更されることで、現在この文書を管理する担当者が明示されました。これにより、内部的な責任の所在が明確になり、文書の管理がしやすくなると考えられます。

また、最終更新日を新しい日に変更することで、最新の情報に基づいて文書が更新されていることが利用者に伝わります。これにより、ユーザーは情報の鮮度に信頼を置きやすくなります。

さらに、重要な通知文が一般提供を明確に示すように改善され、公開プレビュー中の機能である点が強調されています。これは、ユーザーが製品の開発段階を理解し、適切な判断をもとにサービスを利用するための重要な情報です。全体として、この更新はドキュメントの信頼性と理解を向上させ、ユーザーエクスペリエンスを向上するために寄与しています。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-security-network-security-perimeter.md](#item-49c0d7) | minor update | ネットワークセキュリティパーメーターの検索サービスの追加に関する文書の更新 | modified | 5 | 6 | 11 | 


# Modified Contents
## articles/search/search-security-network-security-perimeter.md{#item-49c0d7}

<details>
<summary>Diff</summary>
````diff
@@ -2,23 +2,22 @@
 title: Add a search service to a network security perimeter
 titleSuffix: Azure AI Search
 description: Add a search service to a network security perimeter for a secure connection
-author: MattGotteiner
-ms.author: magottei
+author: haileytap
+ms.author: haileytapia
 manager: nitinme
 ms.service: azure-ai-search
 ms.custom:
   - ignite-2024
 ms.topic: how-to
-ms.date: 05/29/2025
+ms.date: 08/07/2025
 ---
 
 # Add a search service to a network security perimeter
 
 > [!IMPORTANT]
-> Azure AI Search support for network security perimeter is in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). It's available in [regions providing the feature](/azure/private-link/network-security-perimeter-concepts).
-> This preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
+> Although network security perimeter is generally available, its implementation in Azure AI Search remains in public preview under [supplemental terms of use](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). This preview is provided without a service-level agreement and isn't recommended for production workloads. Certain features might be unsupported or have constrained capabilities.
 >
->  Review the [limitations and considerations](#limitations-and-considerations) section before you start.
+> This article and [What's new in Azure AI Search](whats-new.md) will announce when network security perimeter becomes generally available for Azure AI Search.
 
 This article explains how to join an Azure AI Search service to a [network security perimeter](/azure/private-link/network-security-perimeter-concepts) to control network access to your search service. By joining a network security perimeter, you can:
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "ネットワークセキュリティパーメーターの検索サービスの追加に関する文書の更新"
}
```

### Explanation
この変更では、`search-security-network-security-perimeter.md`という文書に対して、著者情報や日付の更新、重要な注意点の表現の修正が行われました。具体的には、記事の著者がMattGotteinerからhaileytapに変更され、著者のイニシャルも合わせて修正されています。また、文書の最終更新日も2025年5月29日から2025年8月7日に変更されました。

内容に関しては、ネットワークセキュリティパーメーターの機能が一般提供されていることを明確に示すために重要な通知が改良され、一般公開の条件としての製品サポートに関する注意事項が明確にされました。これにより、サービス利用者はこの機能が公開プレビュー中であることを認識し、製品ワークロードに対する推奨使用状況についても理解できるようになっています。全体として、ユーザーへのメッセージを明確にすることで、ドキュメントの信頼性と理解を向上させることが狙いです。


