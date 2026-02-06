---
date: '2026-02-06'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f5997cf...MicrosoftDocs:ad7cfc9
summary: このドキュメントの更新では、カスタムモデルと言語サービスの移行に関するマニュアルが微調整されました。特に、バージョンや移行日程の明確化に焦点を当てて、利用者に正確な情報を提供しています。具体的には、`doc-intel-4.0.0`のバージョンに対応するカスタムモデルのセクションが明確になりました。また、移行日程が2026年2月16日から2027年3月20日に修正されたことで、ユーザーはスケジュール調整を行う必要があります。これらの変更により、ユーザーが適切なバージョン情報に基づいてカスタムモデルの機能を理解できるようになり、移行準備期間も確保されるため、安定した運営が期待されます。全体として、今回の更新はユーザーと開発者の連携をスムーズにする重要な要素です。
title: Diff Insight Report - misc

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:f5997cf...MicrosoftDocs:ad7cfc9){target="_blank"}

# ハイライト
このドキュメントの更新では、カスタムモデルと言語サービスの移行に関するマニュアルが微調整されました。特に、バージョンや移行日程の明確化という点で利用者に正確な情報を提供することに重きを置いています。

## 新機能
- `doc-intel-4.0.0`のバージョンに対応するカスタムモデルのセクションが明確化されました。

## 互換性の破棄
- 明示されていませんが、移行日程が変更されたため、ユーザーはスケジュール調整の必要があります。

## その他の更新
- マイクロソフトファウンドリーへの移行日程が2026年2月16日から2027年3月20日に修正されました。

# インサイト
今回の変更は、ユーザーマニュアルの中で特定のバージョンや移行に関する情報を最新のものにアップデートすることを目的としています。ドキュメントインテリジェンスの部分では、`doc-intel-4.0.0`という新しいバージョン指定が加わることで、ユーザーが適切なバージョン情報に基づいてカスタムモデルの機能を理解できるようにしています。このような明確化により、誤った設定や互換性の問題を事前に防ぐことが可能になります。

また、言語サービスのセクションでは、前もって移行日程の変更を通知することにより、企業や開発者が適切に次のシステムへと移行するための準備期間を確保することができます。具体的には、移行日程が一年以上延長されたことで、組織は長期的な移行戦略を策定する余裕が生まれ、結果的に安定した運営が期待されます。

これらの調整は、ユーザーにとって過去のドキュメントの混乱を避け、また将来的な技術の進化に対応するために必要不可欠です。全体的に見て、小さな更新であっても、ドキュメントやマニュアルは開発者と利用者の連携を円滑にする重要な要素となり得ます。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [custom-model.md](#item-27c3b9) | minor update | カスタムモデルに関するドキュメントの更新 | modified | 1 | 0 | 1 | 
| [migration-studio-to-foundry.md](#item-12d575) | minor update | 言語スタジオからマイクロソフトファウンドリーへの移行日程変更 | modified | 3 | 3 | 6 | 


# Modified Contents
## articles/ai-services/document-intelligence/train/custom-model.md{#item-27c3b9}

<details>
<summary>Diff</summary>
````diff
@@ -14,6 +14,7 @@ monikerRange: '<=doc-intel-4.0.0'
 
 # Document Intelligence custom models
 
+::: moniker range="doc-intel-4.0.0"
 [!INCLUDE [applies to v4.0](../includes/applies-to-v40.md)]
 ::: moniker-end
 
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "カスタムモデルに関するドキュメントの更新"
}
```

### Explanation
この変更は、ドキュメントインテリジェンスに関するカスタムモデルのマニュアルにおいて、`moniker`の範囲を指定する新しい行を追加したものです。具体的には、`doc-intel-4.0.0`のバージョンに対応するセクションが追加されました。この小さな更新により、特定のバージョンに関してより明確な情報が提供され、利用者がどのバージョンが適用できるかを理解しやすくなります。

## articles/ai-services/language-service/migration-studio-to-foundry.md{#item-12d575}

<details>
<summary>Diff</summary>
````diff
@@ -6,13 +6,13 @@ author: laujan
 manager: nitinme
 ms.service: azure-ai-language
 ms.topic: upgrade-and-migration-article
-ms.date: 01/26/2026
+ms.date: 02/05/2026
 ms.author: lajanuar
 ---
 <!-- markdownlint-disable MD025 -->
 # Migrate from Language Studio to Microsoft Foundry
 
-Azure Language Studio will migrate to Microsoft Foundry on February 16, 2026. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. After February 16, 2026, Language Studio will no longer be available, but none of your existing projects, data, or service endpoints are impacted. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
+Azure Language Studio will migrate to Microsoft Foundry on March 20, 2027. All existing capabilities, along with new feature enhancements, are fully available in Microsoft Foundry. After March 20, 2027, Language Studio will no longer be available, but none of your existing projects, data, or service endpoints are impacted. This guide provides step-by-step migration instructions to ensure uninterrupted access to Azure AI Language features and seamless project continuity within the Foundry environment.
 
 ## Why migrate to Microsoft Foundry?
 
@@ -213,7 +213,7 @@ After importing your projects, validate that the migration is successful:
 
 > [!IMPORTANT]
 >
-> **Post-retirement project recreation**. After the February 16, 2026 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
+> **Post-retirement project recreation**. After the March 20, 2027 retirement date, Language Studio export functionality is no longer available. However, you can recreate your custom projects directly in Microsoft Foundry:
 >
 > * **Existing Azure Language resources**. You can access and continue to use your current Azure Language resources within the Microsoft Foundry portal by creating a **Foundry hub** and an associated **hub-based project**. For more information, *see* [Create a hub in the Azure portal](/azure/ai-foundry/how-to/create-azure-ai-resource?view=foundry-classic&preserve-view=true&tabs=portal#create-a-hub-in-the-azure-portal).
 >
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "言語スタジオからマイクロソフトファウンドリーへの移行日程変更"
}
```

### Explanation
この変更は、言語サービスに関する「言語スタジオからマイクロソフトファウンドリーへの移行」というドキュメントの内容を更新しています。具体的には、移行日程が2026年2月16日から2027年3月20日に変更されており、それに伴い、関連する文言も修正されています。この更新により、ユーザーには新しい移行日程が通知され、移行手続きが円滑に行われることが期待されます。また、移行後の利用に関する注意点も明確に記載されており、ユーザーが計画的に対応できるよう配慮されています。


