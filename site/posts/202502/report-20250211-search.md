---
date: '2025-02-11'
permalink: https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:879fbd3...MicrosoftDocs:f57bd77
summary: この変更は、`articles/search/search-faq-frequently-asked-questions.yml`のリンクが修正されたマイナーアップデートです。具体的には、Python用のバックアップと復元に関するサンプルコードのリンクが更新され、正確性が向上しました。互換性を損なう重要な変更はなく、ユーザーが正しく情報にアクセスできるようになりました。この修正は、技術文書のリンクの正確性を保ち、ユーザーの混乱を防ぐために重要です。
title: Diff Insight Report - search

---

[View Diff on GitHub](https://github.com/MicrosoftDocs/azure-ai-docs/compare/MicrosoftDocs:879fbd3...MicrosoftDocs:f57bd77){target="_blank"}

# ハイライト
この変更は、`articles/search/search-faq-frequently-asked-questions.yml`のリンクが修正されたマイナーアップデートです。具体的には、Python用のバックアップと復元に関するサンプルコードのリンクが更新されました。

## 新機能
- 特に新しい機能の追加はありませんが、リンクの正確性が向上しました。

## 互換性の破壊的変更
- 互換性を損なうような重要な変更はありません。

## その他の更新
- ファイルパスの修正により、ユーザーが正しくPythonのサンプルコードにアクセスできるようになりました。

# 洞察
今回の更新はリンクの修正に関するもので、ユーザーエクスペリエンスを円滑にするための重要な調整です。リンク変更前のパス（`/demo-python/code/index-backup-restore/azure-search-backup-and-restore.ipynb`）は、おそらくリポジトリ構成変更やディレクトリ再編により無効になっていた可能性があります。修正後のパス（`/demo-python/code/utilities/index-backup-and-restore/azure-search-backup-and-restore.ipynb`）により、正しい場所にユーザーを誘導することで、目的の情報に効果的にアクセスできるようになりました。

このようなリンク修正は、特に技術文書やサンプルリソースを頻繁に更新する環境では、リソースへのアクセスの一貫性を保つために必要不可欠です。リンクが正しくないと、ユーザーは望む情報にたどり着けず、混乱を招く原因となります。この変更は、そのような問題を未然に防ぎ、ユーザーが求める技術的な指針を迅速に提供する助けとなるでしょう。

# Summary Table
|  Filename  | Type |    Title    | Status | A  | D  | M  |
|------------|------|-------------|--------|----|----|----|
| [search-faq-frequently-asked-questions.yml](#item-eab2ba) | minor update | FAQのリンク修正 | modified | 1 | 1 | 2 | 


# Modified Contents
## articles/search/search-faq-frequently-asked-questions.yml{#item-eab2ba}

<details>
<summary>Diff</summary>
````diff
@@ -79,7 +79,7 @@ sections:
         answer: |
           There's no native support for porting indexes. Search indexes are considered downstream data structures, accepting content from other data sources that collect operational data. As such, there's no built-in support for backing up and restoring indexes because the expectation is that you would rebuild an index from source data if you deleted it, or wanted to move it.
           
-          However, if you want to move an index between search services, you can try the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities). There's also a [Python version of backup and restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/index-backup-restore/azure-search-backup-and-restore.ipynb).
+          However, if you want to move an index between search services, you can try the **index-backup-restore** sample code in this [Azure AI Search .NET sample repo](https://github.com/Azure-Samples/azure-search-dotnet-utilities). There's also a [Python version of backup and restore](https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/utilities/index-backup-restore/azure-search-backup-and-restore.ipynb).
                    
       - question: |
           Can I restore my index or service once it's deleted?
````
</details>

### Summary

```json
{
    "modification_type": "minor update",
    "modification_title": "FAQのリンク修正"
}
```

### Explanation
この修正では、`articles/search/search-faq-frequently-asked-questions.yml`ファイル内のリンクが更新されました。具体的には、Pythonによるバックアップと復元のサンプルコードへのリンクのパスが変更されました。元のパスは、`/demo-python/code/index-backup-restore/azure-search-backup-and-restore.ipynb` でしたが、修正後は `/demo-python/code/utilities/index-backup-and-restore/azure-search-backup-and-restore.ipynb` となっています。この変更は、正しいリンクを提供するためのものであり、特にPythonバージョンに関連するサンプルコードを探す際の利便性を向上させています。


